# TP-Link Archer C50 API
 HTTP based python package for API access and router management of the TP-Link Archer C50

**Version 0.1.0**

## Usage
### Initialize
Enter your hostname/IP & credentials used to log in to your router management page
```python
import tplinkrouter  

router = tplinkrouter.C50('hostname','username','password')
```
### Get
```python
router._get('wlan')

# Result
# {
#    '[1,1,0,0,0,0]0': {'name': 'wlan0', 'SSID': 'myssid 2.4Ghz', 'enable': '1', 'X_TP_Configuration_Modified': '1', 'beaconType': '11i', 'standard': 'n', 'WEPEncryptionLevel': 'Disabled,40-bits,104-bits', 'WEPKeyIndex': '1', 'basicEncryptionModes': 'None', 'basicAuthenticationMode': 'None', 'WPAEncryptionModes': 'TKIPandAESEncryption', 'WPAAuthenticationMode': 'PSKAuthentication', 'IEEE11iEncryptionModes': 'AESEncryption', 'IEEE11iAuthenticationMode': 'PSKAuthentication', 'X_TP_PreSharedKey': 'password', 'X_TP_GroupKeyUpdateInterval': '0', 'X_TP_RadiusServerIP': '', 'X_TP_RadiusServerPort': '1812', 'X_TP_RadiusServerPassword': ''}, 
#    '[1,2,0,0,0,0]0': {'name': 'wlan5', 'SSID': 'myssid 5Ghz', 'enable': '1', 'X_TP_Configuration_Modified': '0', 'beaconType': '11i', 'standard': 'ac', 'WEPEncryptionLevel': 'Disabled,40-bits,104-bits', 'WEPKeyIndex': '1', 'basicEncryptionModes': 'None', 'basicAuthenticationMode': 'None', 'WPAEncryptionModes': 'TKIPandAESEncryption', 'WPAAuthenticationMode': 'PSKAuthentication', 'IEEE11iEncryptionModes': 'AESEncryption', 'IEEE11iAuthenticationMode': 'PSKAuthentication', 'X_TP_PreSharedKey': 'password', 'X_TP_GroupKeyUpdateInterval': '0', 'X_TP_RadiusServerIP': '', 'X_TP_RadiusServerPort': '1812', 'X_TP_RadiusServerPassword': ''}
# }
```
```python
router._get('version')

# Result
{
     '[0,0,0,0,0,0]0': {
          'hardwareVersion': 'Archer C50 v1 00000002', 
          'softwareVersion': '0.9.1 3.0 v0045.0 Build 160411 Rel.42416n'
     }
}
```
Supported Parameters:
 - `about`
 - `version`
 - `info`
 - `wan`
 - `wlan`
 - `24ghz`
 - `5ghz`
 - `dhcp_settings`
 - `dhcp_clients`
 - `restart`
 - `logout`

Return Format: Dictionary

### Set
Change Password of 2.4Ghz Network:
```python
router._set('24ghz', [{'[LAN_WLAN#1,1,0,0,0,0#0,0,0,0,0,0]0,5': {'X_TP_PreSharedKey': 'new_password'}}])
```
