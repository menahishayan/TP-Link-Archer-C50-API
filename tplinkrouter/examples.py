import tplinkrouter

r = tplinkrouter.C50('192.168.0.1','admin','alphatango')

# Get SSID and Password of 2.4Ghz and 5Ghz
for d in r._get('wlan').values():
    print(d['SSID'])
    print(d['X_TP_PreSharedKey'])

# get('restart')
r._set('wan', [{}, {'[WAN_PPP_CONN#1,1,1,0,0,0#0,0,0,0,0,0]1,19': {'enable': '1'}}, {}])
# _set('24ghz', [{'[LAN_WLAN#1,1,0,0,0,0#0,0,0,0,0,0]0,5': {'X_TP_PreSharedKey': 'pass'}}])
# _set('5ghz', [{'[LAN_WLAN#1,2,0,0,0,0#0,0,0,0,0,0]0,5': {'X_TP_PreSharedKey': 'pass'}}])
