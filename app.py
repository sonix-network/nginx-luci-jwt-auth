#!/usr/bin/env python3
import collections
import flask
import json
import pathlib
import secrets
import socket
import ubus

import ctypes
import json
import jwt
import time


jwt_public_key = '''
-----BEGIN PUBLIC KEY-----
MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE/H6ctMmPwKnSC4dqeBAkrP28zj8J
wniLZHDeSbxG5F68C8aGSJ7uqBfQcYYzUGWVS8OqHcVDgsKo5Yu4Dx8kGA==
-----END PUBLIC KEY-----
'''


class InvalidJWT(Exception):
    pass


def check_jwt(jwt_str, hostname):
    jv = ctypes.POINTER(jwt.struct_jwt_valid)()
    jw = ctypes.POINTER(jwt.struct_jwt)()
    assert jwt.jwt_valid_new(ctypes.byref(jv), jwt.JWT_ALG_ES256) == 0, 'jwt_valid_new failed'

    jwt.jwt_valid_set_headers(jv, 1)
    jwt.jwt_valid_set_now(jv, int(time.time()))
    ret = jwt.jwt_decode(ctypes.byref(jw), jwt_str, jwt_public_key, len(jwt_public_key))
    if ret != 0:
        print('failed to decode jwt, invalid key?')
        raise InvalidJWT('could not decode jwt')

    user = None
    try:
        jwt.jwt_valid_add_grants_json(jv, json.dumps({
            'aud': f'{hostname}.local.sonix.network',
            }))
        err = jwt.jwt_validate(jw, jv)
        if err == jwt.JWT_VALIDATION_GRANT_MISMATCH:
            jwt.jwt_valid_add_grants_json(jv, json.dumps({
                'aud': f'{hostname}-fallback.local.sonix.network',
                }))
            err = jwt.jwt_validate(jw, jv)
        if err != 0:
            print('failed to validate jwt:', jwt.jwt_exception_str(err))
            raise InvalidJWT('could not decode jwt')
        user = jwt.jwt_get_grant(jw, "user").decode()
    finally:
        jwt.jwt_free(jw)
        jwt.jwt_valid_free(jv)
    return user


def merge_acl(acls, acl, name):
    for scope, perms in acl.items():
        if isinstance(perms, list):
            perms = {k: [name] for k in perms}
        for path, funcs in perms.items():
            acls[scope][path].update(funcs)
    return acls


def load_acl_grants():
    acls = collections.defaultdict(lambda: collections.defaultdict(set))
    for aclp in pathlib.Path('/usr/share/rpcd/acl.d/').glob('*.json'):
        with open(aclp, 'r') as f:
            for k, acl in json.load(f).items():
                if 'read' in acl:
                    acls['access-group'][k].add('read')
                    acls = merge_acl(acls, acl['read'], 'read')
                if 'write' in acl:
                    acls['access-group'][k].add('write')
                    acls = merge_acl(acls, acl['write'], 'write')
    scopes = {}
    for scope, objects in acls.items():
        flat_objects = []
        for obj, paths in objects.items():
            for path in paths:
                flat_objects.append((obj, path))
        scopes[scope] = flat_objects
    return scopes


app = flask.Flask(__name__)

@app.route('/')
def luci_login():
    hostname = socket.gethostname()
    jwt_assertion = flask.request.headers.get('X-Pomerium-Jwt-Assertion', None)
    response = flask.make_response(flask.redirect('/cgi-bin/luci'))
    if not jwt_assertion:
        # No JWT, redirect to login page
        return response
    try:
        user = check_jwt(jwt_assertion, hostname)
    except InvalidJWT:
        return 'Invalid JWT\n', 403

    ubus.connect('/var/run/ubus/ubus.sock')
    try:
        session_id = flask.request.cookies.get('sysauth_https')
        if session_id:
            try:
                ubus.call('session', 'get', {'ubus_rpc_session': session_id, 'keys': ['data']})
            except RuntimeError:
                # expired
                session_id = None
        if session_id is None:
            session_id = ubus.call('session', 'create', {'timeout': 3600})[0]['ubus_rpc_session']
            ubus.call('session', 'set', {'ubus_rpc_session': session_id, 'values': {'username': user}})
            ubus.call('session', 'set', {'ubus_rpc_session': session_id, 'values': {'token': secrets.token_hex(16)}})
            for scope, objects in load_acl_grants().items():
                ubus.call('session', 'grant', {'ubus_rpc_session': session_id, 'scope': scope, 'objects': objects})

            response.set_cookie('sysauth_https', session_id, secure=True, httponly=True)
    finally:
        ubus.disconnect()
    return response


if __name__ == '__main__':
    app.run(port=9998, debug=False, host='::1')
