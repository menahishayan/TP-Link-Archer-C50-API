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

def parse_get_req(body):
    bodyStr = ''
    for b in body:
        bodyStr += b + '\r\n'
    return bodyStr

def parse_set_req(items):
    bodyStr = ''
    for item in items:
        bodyStr += item + '\r\n'
        for i in items[item]:
            bodyStr += i + '=' + items[item][i] + '\r\n'
    return bodyStr

def parse_response(res):
    items = {}
    key = '0'
    for b in res.splitlines():
        if b[0] == '[' and 'error' not in b:
            key = b
            items[key] = {}
        if '=' in b:
            items[key][b[0:b.index('=')]] = b[b.index('=')+1:]

    return items

def get_template(body):
    items = {}
    key = '0'
    for b in body:
        if b[0] == '[':
            key = b
            items[key] = {}
        else:
            items[key][b] = ''

    return items

cookie = get_base64_cookie_string()
referer = 'http://{}'.format(hostname)

with open('params.json') as f:
  ref = json.load(f)

def _get(item):
    items = {}
    for i in ref['get'][item]:
        page = requests.post(
            'http://{}/cgi?{}'.format(hostname,i['path']),
            headers={REFERER: referer, COOKIE: cookie},
            data=(parse_get_req(i['body'])),
            timeout=4)
            
        if page.status_code == 200:
            items = { **items, **parse_response(page.text) }
        else:
            print(page.status_code)
    return items

def _set(item,data):
    template = {}
    require_fetch = False

    for i in ref['set'][item]:
        fetched_template = get_template(i['body'])
        template = { **template, **fetched_template }
        if len(fetched_template) == len(data):
            for f in fetched_template:
                if not len(fetched_template[f]) == len(data[f]):
                    require_fetch = True

    if not len(data) == len(template):
        require_fetch = True
            
    # fetch
    current = {}
    if require_fetch:
        for i in ref['set'][item]:
            for src in i['sources']:
                fetched_data = _get(src['item'])
                for key in src['keys']:
                    current = { **current, **fetched_data[key] }
    for d in data:
        if require_fetch:
            for t in template[d]:
                if t in current:
                    template[d][t] = current[t]
                elif t in src['mappings']:
                    template[d][t] = current[src['mappings'][t]]
            # template[d].update(current)
        template[d].update(data[d])

    print(template)
    # print(parse_set_req(template))
    # page = requests.post(
    #         'http://{}/cgi?{}'.format(hostname,i['path']),
    #         headers={REFERER: referer, COOKIE: cookie},
    #         data=(parse_set_req(template)),
    #         timeout=4)
    # print(page.text)

# for d in get('wlan').values():
#     print(d['SSID'])
#     print(d['X_TP_PreSharedKey'])

# get('restart')

_set('24ghz',{'[LAN_WLAN#1,1,0,0,0,0#0,0,0,0,0,0]0,5':{'X_TP_PreSharedKey':'notbazingaa'}})
# print(_get('wlan')['[1,1,0,0,0,0]0'])