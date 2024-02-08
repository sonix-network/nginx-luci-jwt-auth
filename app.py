#!/usr/bin/env python3
import collections
import flask
import json
import pathlib
import secrets
import socket
import ubus

import jwt


jwt_public_key = '''
-----BEGIN PUBLIC KEY-----
MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE/H6ctMmPwKnSC4dqeBAkrP28zj8J
wniLZHDeSbxG5F68C8aGSJ7uqBfQcYYzUGWVS8OqHcVDgsKo5Yu4Dx8kGA==
-----END PUBLIC KEY-----
'''


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
    if not jwt:
        return 'No JWT provided\n', 403
    try:
        claims = jwt.decode(
                jwt_assertion,
                jwt_public_key,
                audience=f'{hostname}.local.sonix.network',
                strict_aud=True,
                algorithms=['ES256'])
    except jwt.exceptions.PyJWTError:
        return 'Invalid JWT\n', 403

    ubus.connect('/var/run/ubus/ubus.sock')
    response = flask.make_response(flask.redirect('/cgi-bin/luci'))
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
            ubus.call('session', 'set', {'ubus_rpc_session': session_id, 'values': {'username': claims['user']}})
            ubus.call('session', 'set', {'ubus_rpc_session': session_id, 'values': {'token': secrets.token_hex(16)}})
            for scope, objects in load_acl_grants().items():
                ubus.call('session', 'grant', {'ubus_rpc_session': session_id, 'scope': scope, 'objects': objects})

            response.set_cookie('sysauth_https', session_id, secure=True, httponly=True)
    finally:
        ubus.disconnect()
    return response


if __name__ == '__main__':
    app.run(port=9998, debug=False, host='::1')
