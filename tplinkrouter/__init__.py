import base64
import requests

__version__ = '1.0.0'

class C50:
    def __init__(self,hostname,username,password,logger=None):
        self.hostname = hostname
        self.auth = { 'username': username, 'password': password }
        self.cookie = self.get_base64_cookie_string()
        self.referer = 'http://{}'.format(self.hostname)
        self.logger = logger
        self.ref = {
            'get': {
                'about': [{'path': '1&1&1&8', 'body': ['[IGD_DEV_INFO#0,0,0,0,0,0#0,0,0,0,0,0]0,3', 'modelName', 'description', 'X_TP_isFD', '[ETH_SWITCH#0,0,0,0,0,0#0,0,0,0,0,0]1,1', 'numberOfVirtualPorts', '[SYS_MODE#0,0,0,0,0,0#0,0,0,0,0,0]2,1', 'mode', '[/cgi/info#0,0,0,0,0,0#0,0,0,0,0,0]3,0']}],
                'version': [{'path': '1', 'body': ['[IGD_DEV_INFO#0,0,0,0,0,0#0,0,0,0,0,0]0,2', 'hardwareVersion', 'softwareVersion']}],
                'dhcp_settings': [{'path': '1&6', 'body': ['[LAN_HOST_CFG#1,0,0,0,0,0#0,0,0,0,0,0]0,0', '[LAN_IP_INTF#0,0,0,0,0,0#1,0,0,0,0,0]1,3', 'IPInterfaceIPAddress', 'IPInterfaceSubnetMask', '__ifName']}],
                'dhcp_clients': [{'path': '5', 'body': ['[LAN_HOST_ENTRY#0,0,0,0,0,0#0,0,0,0,0,0]0,4', 'leaseTimeRemaining', 'MACAddress', 'hostName', 'IPAddress']}],
                'restart': [{'path': '7', 'body': ['[ACT_REBOOT#0,0,0,0,0,0#0,0,0,0,0,0]0,0']}],
                'logout': [{'path': '8', 'body': ['[/cgi/logout#0,0,0,0,0,0#0,0,0,0,0,0]0,0']}],
                'info': [{'path': '1&1&1&5&5&5&5&5&5&5', 'body': ['[SYS_MODE#0,0,0,0,0,0#0,0,0,0,0,0]0,1', 'mode', '[IGD#0,0,0,0,0,0#0,0,0,0,0,0]1,1', 'LANDeviceNumberOfEntries', '[IGD_DEV_INFO#0,0,0,0,0,0#0,0,0,0,0,0]2,3', 'softwareVersion', 'hardwareVersion', 'upTime', '[WAN_COMMON_INTF_CFG#0,0,0,0,0,0#0,0,0,0,0,0]3,1', 'WANAccessType', '[WAN_IP_CONN#0,0,0,0,0,0#0,0,0,0,0,0]4,0', '[WAN_PPP_CONN#0,0,0,0,0,0#0,0,0,0,0,0]5,0', '[WAN_L2TP_CONN#0,0,0,0,0,0#0,0,0,0,0,0]6,0', '[WAN_PPTP_CONN#0,0,0,0,0,0#0,0,0,0,0,0]7,0', '[L2_BRIDGING_ENTRY#0,0,0,0,0,0#0,0,0,0,0,0]8,1', 'bridgeName', '[LAN_WLAN#0,0,0,0,0,0#0,0,0,0,0,0]9,12', 'status', 'SSID', 'BSSID', 'channel', 'autoChannelEnable', 'standard', 'beaconType', 'basicEncryptionModes', 'X_TP_Bandwidth', 'possibleDataTransmitRates', 'WPAAuthenticationMode', 'IEEE11iAuthenticationMode']}, {'path': '1&1&5&5&5', 'body': ['[LAN_WLAN_WDSBRIDGE#1,1,0,0,0,0#0,0,0,0,0,0]0,1', 'BridgeEnable', '[LAN_WLAN_WDSBRIDGE#1,2,0,0,0,0#0,0,0,0,0,0]1,1', 'BridgeEnable', '[LAN_WLAN_TASK_SCHEDULE#0,0,0,0,0,0#0,0,0,0,0,0]2,2', 'enable', 'isUsrCtrl', '[LAN_IP6_HOST_CFG#0,0,0,0,0,0#0,0,0,0,0,0]3,0', '[LAN_IP6_INTF#0,0,0,0,0,0#0,0,0,0,0,0]4,0']}, {'path': '5&5', 'body': ['[LAN_IP_INTF#0,0,0,0,0,0#0,0,0,0,0,0]0,3', 'IPInterfaceIPAddress', 'IPInterfaceSubnetMask', 'X_TP_MACAddress', '[LAN_HOST_CFG#0,0,0,0,0,0#0,0,0,0,0,0]1,1', 'DHCPServerEnable']}],
                'wlan': [{'path': '5', 'body': ['[LAN_WLAN#0,0,0,0,0,0#0,0,0,0,0,0]0,18', 'name', 'Standard', 'SSID', 'RegulatoryDomain', 'PossibleChannels', 'RegulatoryDomain', 'AutoChannelEnable', 'Channel', 'X_TP_Bandwidth', 'Enable', 'SSIDAdvertisementEnabled', 'BeaconType', 'BasicEncryptionModes', 'WPAEncryptionModes', 'IEEE11iEncryptionModes', 'X_TP_Configuration_Modified', 'WMMEnable', 'X_TP_FragmentThreshold']}, {'path': '5', 'body': ['[LAN_WLAN#0,0,0,0,0,0#0,0,0,0,0,0]0,19', 'name', 'SSID', 'Enable', 'X_TP_Configuration_Modified', 'beaconType', 'Standard', 'WEPEncryptionLevel', 'WEPKeyIndex', 'BasicEncryptionModes', 'BasicAuthenticationMode', 'WPAEncryptionModes', 'WPAAuthenticationMode', 'IEEE11iEncryptionModes', 'IEEE11iAuthenticationMode', 'X_TP_PreSharedKey', 'X_TP_GroupKeyUpdateInterval', 'X_TP_RadiusServerIP', 'X_TP_RadiusServerPort', 'X_TP_RadiusServerPassword']}],
                'guest_24ghz': [{'path': '1', 'body': ['[LAN_WLAN_WDSBRIDGE#1,1,0,0,0,0#0,0,0,0,0,0]0,8', 'BridgeEnable', 'BridgeAddrMode', 'BridgeBSSID', 'BridgeSSID', 'BridgeAuthMode', 'BridgeEncryptMode', 'BridgeKey', 'BridgeWepKeyIndex']}, {'path': '6&1', 'body': ['[LAN_WLAN_MSSIDENTRY#0,0,0,0,0,0#1,1,0,0,0,0]0,18', 'Name', 'Enable', 'SSID', 'SSIDAdvertisementEnable', 'isolateClients', 'BeaconType', 'BasicAuthenticationMode', 'WEPKeyIndex', 'BasicEncryptionModes', 'WPAEncryptionModes', 'WPAAuthenticationMode', 'IEEE11iEncryptionModes', 'IEEE11iAuthenticationMode', 'PreSharedKey', 'GroupKeyUpdateInterval', 'radiusServerIP', 'radiusServerPort', 'radiusServerPassword', '[LAN_WLAN_GUESTNET#1,1,0,0,0,0#0,0,0,0,0,0]1,1']}],
                'guest_5ghz': [{'path': '1', 'body': ['[LAN_WLAN_WDSBRIDGE#1,2,0,0,0,0#0,0,0,0,0,0]0,8', 'BridgeEnable', 'BridgeAddrMode', 'BridgeBSSID', 'BridgeSSID', 'BridgeAuthMode', 'BridgeEncryptMode', 'BridgeKey', 'BridgeWepKeyIndex']}, {'path': '6&1', 'body': ['[LAN_WLAN_MSSIDENTRY#0,0,0,0,0,0#1,2,0,0,0,0]0,18', 'Name', 'Enable', 'SSID', 'SSIDAdvertisementEnable', 'isolateClients', 'BeaconType', 'BasicAuthenticationMode', 'WEPKeyIndex', 'BasicEncryptionModes', 'WPAEncryptionModes', 'WPAAuthenticationMode', 'IEEE11iEncryptionModes', 'IEEE11iAuthenticationMode', 'PreSharedKey', 'GroupKeyUpdateInterval', 'radiusServerIP', 'radiusServerPort', 'radiusServerPassword', '[LAN_WLAN_GUESTNET#1,2,0,0,0,0#0,0,0,0,0,0]1,1']}],
                'wan': [{'path': '1&1', 'body': ['[WAN_PPP_CONN#1,1,1,0,0,0#0,0,0,0,0,0]0,0', '[WAN_IP_CONN#1,1,2,0,0,0#0,0,0,0,0,0]1,0']}],
                'bands': [{'path': '5', 'body': ['[LAN_WLAN#0,0,0,0,0,0#0,0,0,0,0,0]0,5', 'name', 'enable', 'X_TP_Configuration_Modified', 'X_TP_Band', '__syncApStatus']}], 
                'wlan_info': [{'path': '1&1&1&1&6&6', 'body': ['[LAN_WLAN_TASK_SCHEDULE#1,1,0,0,0,0#0,0,0,0,0,0]0,3', 'enable', 'isTimeSet', 'isUsrCtrl', '[LAN_WLAN_TASK_SCHEDULE#1,2,0,0,0,0#0,0,0,0,0,0]1,3', 'enable', 'isTimeSet', 'isUsrCtrl', '[LAN_WLAN_MULTISSID#1,1,0,0,0,0#0,0,0,0,0,0]2,1', 'MultiSSIDEnable', '[LAN_WLAN_MULTISSID#1,2,0,0,0,0#0,0,0,0,0,0]3,1', 'MultiSSIDEnable', '[LAN_WLAN_MSSIDENTRY#0,0,0,0,0,0#0,0,0,0,0,0]4,7', 'Enable', 'Name', 'SSID', 'SSIDAdvertisementEnable', 'BeaconType', 'WPAEncryptionModes', 'IEEE11iEncryptionModes', '[LAN_WLAN_MSSIDENTRY#0,0,0,0,0,0#0,0,0,0,0,0]5,7', 'Enable', 'Name', 'SSID', 'SSIDAdvertisementEnable', 'BeaconType', 'WPAEncryptionModes', 'IEEE11iEncryptionModes']}]
            },
            'set': {
                '24ghz': [{'path': '2', 'sources': [{'item': 'wlan', 'keys': ['[1,1,0,0,0,0]0'], 'mappings': {'BeaconType': 'beaconType'}}], 'body': ['[LAN_WLAN#1,1,0,0,0,0#0,0,0,0,0,0]0,5', 'BeaconType', 'IEEE11iAuthenticationMode', 'IEEE11iEncryptionModes', 'X_TP_PreSharedKey', 'X_TP_GroupKeyUpdateInterval']}],
                '5ghz': [{'path': '2', 'sources': [{'item': 'wlan', 'keys': ['[1,2,0,0,0,0]0'], 'mappings': {'BeaconType': 'beaconType'}}], 'body': ['[LAN_WLAN#1,2,0,0,0,0#0,0,0,0,0,0]0,5', 'BeaconType', 'IEEE11iAuthenticationMode', 'IEEE11iEncryptionModes', 'X_TP_PreSharedKey', 'X_TP_GroupKeyUpdateInterval']}],
                'wan': [{'path': '2', 'sources': [{'item': 'wan', 'keys': ['[1,1,1,0,0,0]0']}], 'body': ['[WAN_ETH_INTF#1,0,0,0,0,0#0,0,0,0,0,0]0,1', 'enable']}, {'path': '2&2&2', 'sources': [{'item': 'wan', 'keys': ['[1,1,1,0,0,0]0']}], 'defaults': {'[WAN_ETH_INTF#1,0,0,0,0,0#0,0,0,0,0,0]0,1': {'X_TP_lastUsedIntf': 'pppoe_eth3_d'}, '[WAN_IP_CONN#1,1,1,0,0,0#0,0,0,0,0,0]2,12': {'subnetMask': '255.255.255.255', 'maxMTUSize': '1500', 'externalIPAddress': '169.254.1.1', 'defaultGateway': '0.0.0.0', 'DNSServers': '0.0.0.0,0.0.0.0'}}, 'body': ['[WAN_ETH_INTF#1,0,0,0,0,0#0,0,0,0,0,0]0,1', 'X_TP_lastUsedIntf', '[WAN_PPP_CONN#1,1,1,0,0,0#0,0,0,0,0,0]1,19', 'username', 'password', 'connectionTrigger', 'PPPAuthenticationProtocol', 'PPPoEACName', 'PPPoEServiceName', 'maxMRUSize', 'NATEnabled', 'X_TP_FullconeNATEnabled', 'X_TP_FirewallEnabled', 'X_TP_IGMPProxyEnabled', 'X_TP_IGMPForceVersion', 'X_TP_UseStaticIP', 'PPPLCPEcho', 'DNSOverrideAllowed', 'DNSServers', 'X_TP_IPv4Enabled', 'secondConnection', 'enable', '[WAN_IP_CONN#1,1,1,0,0,0#0,0,0,0,0,0]2,12', 'externalIPAddress', 'subnetMask', 'defaultGateway', 'DNSOverrideAllowed', 'DNSServers', 'NATEnabled', 'X_TP_FullconeNATEnabled', 'X_TP_FirewallEnabled', 'X_TP_IGMPProxyEnabled', 'X_TP_IGMPForceVersion', 'maxMTUSize', 'enable']}, {'path': '2', 'sources': [{'item': 'wan', 'keys': ['[1,1,1,0,0,0]0'], 'mappings': {'__ifAliasName': 'name'}}], 'body': ['[L3_FORWARDING#0,0,0,0,0,0#0,0,0,0,0,0]0,3', '__ifAliasName', '__ifName', 'defaultConnectionService']}],
                '24ghz_band': [{'path': '2&2&2&2', 'sources': [{'item': 'wlan_info', 'keys': ['[1,1,0,0,0,0]0']}, {'item': 'bands', 'keys': ['[1,1,0,0,0,0]0']}], 'body': ['[LAN_WLAN#1,1,0,0,0,0#0,0,0,0,0,0]0,2', 'Enable', '__syncApStatus', '[LAN_WLAN_TASK_SCHEDULE#1,1,0,0,0,0#0,0,0,0,0,0]1,1', 'isUsrCtrl', '[LAN_WLAN_MSSIDENTRY#1,1,1,0,0,0#0,0,0,0,0,0]2,1', 'enable', '[LAN_WLAN_MSSIDENTRY#1,2,1,0,0,0#0,0,0,0,0,0]3,1', 'enable']}],
                '5ghz_band': [{'path': '2&2&2&2', 'sources': [{'item': 'wlan_info', 'keys': ['[1,2,0,0,0,0]1']}, {'item': 'bands', 'keys': ['[1,2,0,0,0,0]0']}], 'body': ['[LAN_WLAN#1,2,0,0,0,0#0,0,0,0,0,0]0,2', 'Enable', '__syncApStatus', '[LAN_WLAN_TASK_SCHEDULE#1,2,0,0,0,0#0,0,0,0,0,0]1,1', 'isUsrCtrl', '[LAN_WLAN_MSSIDENTRY#1,1,1,0,0,0#0,0,0,0,0,0]2,1', 'enable', '[LAN_WLAN_MSSIDENTRY#1,2,1,0,0,0#0,0,0,0,0,0]3,1', 'enable']}]
            }
        }
        self.__name__ = ''
        self.description = ''
        self.__version__ = ''

        try:
            about = self._get('about')['[0,0,0,0,0,0]0']
            self.__name__ = about['modelName']
            self.description = about['description']
            self.__version__ = self._get('version')['[0,0,0,0,0,0]0']['softwareVersion'].split()[4]
        except:
            self.log("Metadata Update Error.")

    def log(self,msg):
        if self.logger:
            self.logger.error(msg)
        else:
            print(msg)

    def get_base64_cookie_string(self):
        username_password = '{}:{}'.format(self.auth['username'], self.auth['password'])
        b64_encoded_username_password = base64.b64encode(
            username_password.encode('ascii')
        ).decode('ascii')
        return 'Authorization=Basic {}'.format(b64_encoded_username_password)


    def parse_get_req(self,body):
        bodyStr = ''
        for b in body:
            bodyStr += b + '\r\n'
        return bodyStr


    def parse_set_req(self,items):
        bodyStr = ''
        for item in items:
            bodyStr += item + '\r\n'
            for i in items[item]:
                bodyStr += i + '=' + items[item][i] + '\r\n'
        return bodyStr


    def parse_response(self,res):
        items = {}
        key = '0'
        for b in res.splitlines():
            if b[0] == '[' and 'error' not in b:
                key = b
                items[key] = {}
            if '=' in b:
                items[key][b[0:b.index('=')]] = b[b.index('=')+1:]

        return items


    def get_template(self,body):
        items = {}
        key = '0'
        for b in body:
            if b[0] == '[':
                key = b
                items[key] = {}
            else:
                items[key][b] = ''

        return items


    def _get(self,item):
        items = {}
        for i in self.ref['get'][item]:
            try:
                page = requests.post(
                    'http://{}/cgi?{}'.format(self.hostname, i['path']),
                    headers={'referer': self.referer, 'cookie': self.cookie},
                    data=(self.parse_get_req(i['body'])),
                    timeout=4)

                items = {**items, 'status_code':page.status_code}
                if page.status_code == 200:
                    items = {**items, **self.parse_response(page.text)}
                else:
                    self.log('{} Get Error: {}'.format(self.__name__, page.status_code))
                    return items
            except:
                items = {**items, 'status_code':-1}
                return items
        if not item == 'logout':
            self._get('logout')
        return items


    def _set(self,item, data):
        index = 0
        for i in self.ref['set'][item]:
            require_fetch = False
            template = self.get_template(i['body'])

            if len(template) == len(data[index]):
                for f in template:
                    if f not in data[index] or not len(template[f]) == len(data[index][f]):
                        require_fetch = True
            else:
                require_fetch = True

            current = {}
            if require_fetch:
                for src in i['sources']:
                    fetched_data = self._get(src['item'])
                    for key in src['keys']:
                        current = {**current, **fetched_data[key]}

            for d in template:
                if require_fetch:
                    for t in template[d]:
                        if t in current:
                            template[d][t] = current[t]
                        elif 'mappings' in src and t in src['mappings']:
                            template[d][t] = current[src['mappings'][t]]
                        if 'defaults' in i and d in i['defaults']:
                            if t in i['defaults'][d]:
                                template[d][t] = i['defaults'][d][t]
                if d in data[index]:
                    template[d].update(data[index][d])

            try:
                page = requests.post(
                    'http://{}/cgi?{}'.format(self.hostname, i['path']),
                    headers={'referer': self.referer, 'cookie': self.cookie},
                    data=(self.parse_set_req(template)),
                    timeout=18)

                if not page.text == '[error]0':
                    self.log(page.text)
                    return False
            except:
                self.log("Request Error")
                return False

            index = index+1
            if index == len(data):
                break
        
        self._get('logout')
        return True

    def about(self):
        try:
            return self._get('about')['[0,0,0,0,0,0]0']
        except:
            return None

    def get_version(self):
        try:
            return self._get('version')['[0,0,0,0,0,0]0']
        except:
            return None

    def get_clients(self):
        try:
            data = self._get('dhcp_clients')
            clients = {}

            data.pop('status_code')

            for c in data.values():
                clients[c['hostName']] = c
            
            return clients
        except:
            return {}

    def get_clients_by_mac(self):
        try:
            data = self._get('dhcp_clients')
            clients = {}

            data.pop('status_code')

            for c in data.values():
                clients[c['MACAddress']] = c
            
            return clients
        except:
            return {}

    def get_wlans(self):
        try:
            main = self._get('wlan')
            guest24 = self._get('guest_24ghz')
            guest5 = self._get('guest_5ghz')

            main.pop('status_code')
            guest24.pop('status_code')
            guest5.pop('status_code')

            main['guest24'] = { **guest24['[1,1,0,0,0,0]0'], **guest24['[1,1,1,0,0,0]0']}
            main['guest5'] = { **guest5['[1,2,0,0,0,0]0'], **guest5['[1,2,1,0,0,0]0']}

            wlans = {}

            for w in main.values():
                if 'X_TP_PreSharedKey' in  w or 'preSharedKey' in w:
                    w['Password'] = w['X_TP_PreSharedKey' if 'X_TP_PreSharedKey' in  w else 'preSharedKey'] if w['WPAAuthenticationMode'] == 'PSKAuthentication' else ''
                wlans[w['name']] = w

            return wlans
        except:
            return {}

    def get_ssids(self):
        try:
            wlans = self.get_wlans()
            ssids = []

            for w in wlans.values():
                ssids.append(w['SSID'])

            return ssids
        except:
            return None

    def get_password(self,ssid):
        try:
            wlans = self.get_wlans()

            for w in wlans.values():
                if w['SSID'] == ssid:
                    return w['Password']

            return None
        except:
            return None

    def set_password(self,ssid,password):
        try:
            main = self._get('wlan')
            key = ''

            main.pop('status_code')

            for i, m in main.items():
                if m['SSID'] == ssid:
                    key = i[1:12]

            return self._set('5ghz' if '2' in key else'24ghz', [{'[LAN_WLAN#{}#0,0,0,0,0,0]0,5'.format(key): {'X_TP_PreSharedKey': password}}])
        except:
            return False

    def set_ssid_state(self,ssid,state):
        try:
            main = self._get('wlan')
            key = ''

            main.pop('status_code')

            for i, m in main.items():
                if m['SSID'] == ssid:
                    key = i[1:12]

            return self._set('5ghz' if '2' in key else'24ghz', [{'[LAN_WLAN#{}#0,0,0,0,0,0]0,5'.format(key): {'enable': '1' if state else '0'}}])
        except:
            return False

    def set_band(self,band,state):
        try:
            bands = self._get('bands')
            key = ''

            bands.pop('status_code')

            for i, m in bands.items():
                if m['X_TP_Band'].lower() == band.lower():
                    key = i[1:12]

            return self._set('{}_band'.format(band.lower().replace('.','')), [{'[LAN_WLAN#{}#0,0,0,0,0,0]0,2'.format(key):{'Enable':'1' if state else '0'}}])
        except:
            return False

    def is_on(self):
        try:
            status = self._get('logout')['status_code']
            return True if not status == -1 else False
        except:
            return False

    def restart(self):
        try:
            return self._get('restart')
        except:
            return False

    def logout(self):
        try:
            return True if self._get('logout')['status_code'] == 200 else False
        except:
            return False