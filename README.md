## Installation

```
ssh root@oob-lab-sw1.local.sonix.network 'mkdir -p /opt/jwt-auth/'
scp jwt-authd root@oob-lab-sw1.local.sonix.network:/etc/init.d/
scp -r app.py jwt/ root@oob-lab-sw1.local.sonix.network:/opt/jwt-auth/
scp jwt-auth.locations root@oob-lab-sw1.local.sonix.network:/etc/nginx/conf.d/
ssh root@oob-lab-sw1.local.sonix.network 'opkg install python3-flask'
ssh root@oob-lab-sw1.local.sonix.network 'opkg install python3-ubus'
ssh root@oob-lab-sw1.local.sonix.network 'opkg install python3-cryptography'
ssh root@oob-lab-sw1.local.sonix.network 'service jwt-authd enable'
ssh root@oob-lab-sw1.local.sonix.network 'service jwt-authd start'
ssh root@oob-lab-sw1.local.sonix.network 'service nginx restart'
```
