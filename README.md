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

# Return
{
    '[1,1,0,0,0,0]0': {'name': 'wlan0', 'SSID': 'myssid 2.4Ghz', 'enable': '1', 'X_TP_Configuration_Modified': '1', 'beaconType': '11i', 'standard': 'n', 'WEPEncryptionLevel': 'Disabled,40-bits,104-bits', 'WEPKeyIndex': '1', 'basicEncryptionModes': 'None', 'basicAuthenticationMode': 'None', 'WPAEncryptionModes': 'TKIPandAESEncryption', 'WPAAuthenticationMode': 'PSKAuthentication', 'IEEE11iEncryptionModes': 'AESEncryption', 'IEEE11iAuthenticationMode': 'PSKAuthentication', 'X_TP_PreSharedKey': 'password', 'X_TP_GroupKeyUpdateInterval': '0', 'X_TP_RadiusServerIP': '', 'X_TP_RadiusServerPort': '1812', 'X_TP_RadiusServerPassword': ''}, 
    '[1,2,0,0,0,0]0': {'name': 'wlan5', 'SSID': 'myssid 5Ghz', 'enable': '1', 'X_TP_Configuration_Modified': '0', 'beaconType': '11i', 'standard': 'ac', 'WEPEncryptionLevel': 'Disabled,40-bits,104-bits', 'WEPKeyIndex': '1', 'basicEncryptionModes': 'None', 'basicAuthenticationMode': 'None', 'WPAEncryptionModes': 'TKIPandAESEncryption', 'WPAAuthenticationMode': 'PSKAuthentication', 'IEEE11iEncryptionModes': 'AESEncryption', 'IEEE11iAuthenticationMode': 'PSKAuthentication', 'X_TP_PreSharedKey': 'password', 'X_TP_GroupKeyUpdateInterval': '0', 'X_TP_RadiusServerIP': '', 'X_TP_RadiusServerPort': '1812', 'X_TP_RadiusServerPassword': ''}
}
```
```python
router._get('version')

# Return
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
Enable/Disable WAN PPPoE:
```python
# Enable
router._set('wan', [{}, {'[WAN_PPP_CONN#1,1,1,0,0,0#0,0,0,0,0,0]1,19': {'enable': '1'}}, {}])

# Disable
router._set('wan', [{}, {'[WAN_PPP_CONN#1,1,1,0,0,0#0,0,0,0,0,0]1,19': {'enable': '0'}}])
```

Return Format: Boolean
Return: 
 - `true` if all sub-tasks were successful
 - `false` if any of the sub-tasks fails
 
*`_set()` only updates the keys passed in argument 2. All other values are either fetched from the router wherever available.*

#### Note 1: Value Format
All key/values passed in Argument 2 of `_set()` must be strings.  
Argument 2 passed to `_set()` **must** be a List of Dictionaries.

#### Note 2: Positional Arguments
Each list item in Argument 2 of `_set()` directly corresponds to each subtask in the process.  
Omitting an item in the list will ignore that subtask. (See Example: Disable WAN PPPoE, index[2] omitted)  
To run a subtask without updating any of its values, pass an empty dictionary in its position.
