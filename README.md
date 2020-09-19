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
Examples:
```python
router._get('wlan')
```
```python
router._get('version')
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
