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

def res_parse(res):
    itemContainer = []
    items = {}
    for b in res.splitlines()[1:]:
        if '=' in b:
            items[b[0:b.index('=')]] = b[b.index('=')+1:]
        if b[0] == '[':
            itemContainer.append(items.copy())
            items = {}
    return itemContainer

cookie = get_base64_cookie_string()

referer = 'http://{}'.format(hostname)

with open('params.json') as f:
  ref = json.load(f)

def get(item):
    items = []
    for i in ref['get'][item]:
        page = requests.post(
            'http://{}/cgi?{}'.format(hostname,i['path']),
            headers={REFERER: referer, COOKIE: cookie},
            data=(req_parse(i['body'])),
            timeout=4)
            
        if page.status_code == 200:
            items.append(res_parse(page.text).copy())
        else:
            print(page.status_code)
    return items

print(get('5ghz'))