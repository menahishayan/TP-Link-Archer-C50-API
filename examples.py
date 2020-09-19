import tplinkrouter

router = tplinkrouter.C50('192.168.0.1','admin','password')

# Get SSID and Password of 2.4Ghz and 5Ghz
for d in router._get('wlan').values():
    print(d['SSID'])
    print(d['X_TP_PreSharedKey'])

print(router._get('version'))

router._set('wan', [{}, {'[WAN_PPP_CONN#1,1,1,0,0,0#0,0,0,0,0,0]1,19': {'enable': '1'}}, {}])
router._set('24ghz', [{'[LAN_WLAN#1,1,0,0,0,0#0,0,0,0,0,0]0,5': {'X_TP_PreSharedKey': 'pass'}}])
router._set('5ghz', [{'[LAN_WLAN#1,2,0,0,0,0#0,0,0,0,0,0]0,5': {'X_TP_PreSharedKey': 'pass'}}])

router._get('restart')
