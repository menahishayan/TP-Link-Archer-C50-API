# TP-Link Archer C50 API
 HTTP based python package for API access and router management of the TP-Link Archer C50

**Version 1.0.0**

## Installation
`pip install tplinkrouter`

## Dependencies
 - [requests](https://pypi.org/project/requests/)

## Usage
### Initialize
Enter your hostname/IP & credentials used to log in to your router management page
```python
import tplinkrouter  

router = tplinkrouter.C50('hostname','username','password')
```

**OPTIONAL:** You may also pass a logger as `tplinkrouter.C50('hostname','username','password',_LOGGER)` to log errors instead of printing them

### Built-in Functions (v0.3.0+)
```python
router.about()

# Return
{
     'modelName': 'Archer C50',
     'description': 'TP-Link Archer C50 AC1200 Dual-Band'
}
```

```python
router.get_clients()

# Return
['johns-iphone','macbook-pro','android-c78df7av3c5d4ba43cad65c6']
```

```python
router.get_password('MYSSID1')

# Return
'mypassword24ghz'
```

```python
router.set_password('MYSSID1','bobsyouruncle')
```

```python
# Disable SSID broadcast of MYSSID2
router.set_ssid_state('MYSSID2',False)
```

```python
# Disable 5GHz Band
router.set_band('5GHz',False)
```

| Function | Args | Description | Return |
--- | --- | --- | ---
| **`about`** | | Gets basic info about the router | `{ 'modelName', 'description' }` |
| **`get_version`** | | Gets hardware and software version of the router | `{ 'hardwareVersion', 'softwareVersion' }` |
| **`get_clients`** | | Gets list of connected clients (host name) including DHCP & permanent leases, across both wifi and LAN | List of strings |
| **`get_clients_by_mac`** | | Gets list of connected clients (MAC Address) including DHCP & permanent leases, across both wifi and LAN | List of strings |
**`get_wlans`** | | Gets details of wlans (by internal wlan name) including guest network wlans on both bands | Dict of Dicts
**`get_ssids`** | | Gets list of ssids including guest network wlans on both bands | List of strings
**`get_password`** | ssid -> `str: required` | Gets WPA2 PSK of specified SSID | string
**`set_password`** | ssid -> `str: required`  password -> `str: required` | Sets new WPA2 PSK of specified SSID | boolean
**`set_ssid_state`** | ssid -> `str: required`  state -> `boolean: required` | Enables/disables SSID broadcast of the specified SSID | boolean
**`set_band`** | band -> `2.4GHz` or `5GHz`  state -> `boolean: required` | Enables/disables specified band | boolean
**`is_on`** | | Returns whether or not the device is powered on | boolean
**`restart`** | | Does what it says on the can | boolean
**`logout`** | | Does what it says on the can | boolean

### Internal Function: _get()
Internal function used to access different named commands. You may use this if you want direct access to the router's return data without the cleanup done by built-in functions
```python
router._get('wlan')
```

Supported Parameters:
 - `about`
 - `version`
 - `info`
 - `bands`
 - `wan`
 - `wlan`
 - `wlan_info`
 - `guest_24ghz`
 - `guest_5ghz`
 - `dhcp_settings`
 - `dhcp_clients`
 - `restart`
 - `logout`

Return Format: Dictionary

### Internal Function: _set()
Internal function used to run different **set** processes. You may use this if you want to directly set the router's parameters without the processing done by built-in functions  

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
 
Supported Parameters:
 - `wan`
 - `24ghz`
 - `5ghz`
 - `24ghz_band`
 - `5ghz_band`
 
*`_set()` only updates the keys passed in argument 2. All other values are either fetched from the router wherever available.*

#### Note 1: Value Format
All key/values passed in Argument 2 of `_set()` must be strings.  
Argument 2 passed to `_set()` **must** be a List of Dictionaries.

#### Note 2: Positional Arguments
Each list item in Argument 2 of `_set()` directly corresponds to each subtask in the process.  
Omitting an item in the list will ignore that subtask. (See Example: Disable WAN PPPoE, index[2] omitted)  
To run a subtask without updating any of its values, pass an empty dictionary in its position.

#### Note 3: Status Code
Internal functions return an additional key `status_code` with the HTTP status code of the request. Remember to ignore this key before iterating through returned Lists or Dicts.

<hr/>

## Models
This has only been tested on the TP-Link Archer C50 V1 running firmware 160411.  
Supported Models (known):
 - TP-Link Archer C50 V1
 - TP-Link N600
You're free to test on other models and report them in the Issues tab.
 
## Error 500 & Login Limit
The TP-Link Web Interface only supports upto 1 user logged in at a time (for security reasons, apparently) which is the most common reason to recieve `HTTP ERROR 500`. As a workaround, you must log out from all other devices/browsers and try again. Additionally, you may also run `router._get('logout')`

## Troubleshooting/Error Reporting/Contributing
 - If you face an error, you may debug using a HTTP Requests tool/monitor on your router's configuration webpage. Additionally, you may open a new issue on this repo prefixed by [Bug]
 - If you would like to help improve the package, request features or add support for more models, open an issue prefixed by [Feature Request] or [Improvement]

## PRs and Commit Template
PRs and commits that you make to this repo must include the following:  
- Type: bug-fix or enhancement
- Description: Brief description about what the commit achieves
- Notes: (heads ups/pointers to other developers if necessary)

<hr/>

## Changelog
### v1.0.0
 - First major release!
 - Cleanup 
### v0.3.0
 - Logging support
 - New return format that adds `status_code`
 - Performance Optimization: Logout session after commands to minimize Error 500 instances
 - Remove unnecessary I/O
### v0.2.1
 - Add band control toggles
### v0.2.0
 - Introducing built in functions! Predefined commands for the most commonly used tasks, so you don't have to manually figure out the payloads.
### v0.1.3
 - Fix pip deploy bug
### v0.1.2
 - Fix pip import bug
### v0.1.1
 - Remove AIOHTTP Dependency
### v0.1.0
 - Python Package
