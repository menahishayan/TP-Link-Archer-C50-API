import tplinkrouter

router = tplinkrouter.C50('192.168.0.1','admin','password')

# Get SSID and Password of 2.4Ghz and 5Ghz
for ssid in router.get_ssids():
    print(ssid, router.get_password(ssid))

print(router.__version__)

# enable/disable WAN
router._set('wan', [{}, {'[WAN_PPP_CONN#1,1,1,0,0,0#0,0,0,0,0,0]1,19': {'enable': '1'}}, {}])

# enable disable 2.4GHz band
router.set_band('2.4GHz',True)

# change 5GHz password
router.set_password('SSID 5GHz','newpassword')

# restart
router.restart()

# logout
router.logout()
