from aiohttp.hdrs import (COOKIE, REFERER)
import base64
import requests
import json

hostname = '192.168.0.1'
username = 'admin'
password = 'alphatango'

def get_base64_cookie_string():
    username_password = '{}:{}'.format(username, password)
    b64_encoded_username_password = base64.b64encode(
        username_password.encode('ascii')
    ).decode('ascii')
    return 'Authorization=Basic {}'.format(b64_encoded_username_password)

def req_parse(body):
    bodyStr = ''
    for b in body:
        bodyStr += b + '\r\n'
    return bodyStr

def res_parse(res,key):
    items = [] if key == '' else {}
    item = {}
    for b in res.splitlines()[1:]:
        print(b)
        if '=' in b:
            item[b[0:b.index('=')]] = b[b.index('=')+1:]
        if b[0] == '[':
            if key == '':
                items.append(item.copy())
            else:
                items[item[key] if key in item else key] = item.copy()
            item = {}

    print('\n')
    if key == '':
        return items[0] if len(items) < 2 else items[0]
    else:
        return items

cookie = get_base64_cookie_string()

referer = 'http://{}'.format(hostname)

with open('params.json') as f:
  ref = json.load(f)

def get(item):
    items = {}
    for i in ref['get'][item]:
        page = requests.post(
            'http://{}/cgi?{}'.format(hostname,i['path']),
            headers={REFERER: referer, COOKIE: cookie},
            data=(req_parse(i['body'])),
            timeout=4)
            
        if page.status_code == 200:
            items = { **items, **res_parse(page.text, i['key'] if 'key' in i else '') }
        else:
            print(page.status_code)
    return items

# for d in get('dhcp_clients')[0]:
#     print(d['hostName'])

print(get('info'))
