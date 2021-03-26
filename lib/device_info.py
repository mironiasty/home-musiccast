"""
Device Info class
"""
from .call_api import call_api

__DEFAULT_CONTROL_URL = '/YamahaExtendedControl/v1/'


class DeviceInfo:
    '''
    Device info -> base class to get basic iformation about device
    '''

    device_addressa = ""

    def __init__(self, device):
        self.base_url = device if isinstance(
            device, str) else device['base_url']
        self.control_url = __DEFAULT_CONTROL_URL if isinstance(
            device, str) else device['control_url']

    def ___str__(self):
        return self.base_url

    def api(self, name, endpoint):
        path = '{name}/{endpoint}'.format(name=name, endpoint=endpoint)
        return call_api(self.base_url,
                        path, self.control_url)

    def get_url(self):
        return self.base_url


class DeviceInfoSystem(DeviceInfo):
    '''
    Device Info System -> set of function to get system information about single Music Cast device
    '''

    def __system_api(self, endpoint):
        return self.api('system', endpoint)

    def get_device_info(self):
        return self.__system_api('getDeviceInfo')

    def get_features(self):
        return self.__system_api('getFeatures')


class DeviceInfoNetusb(DeviceInfo):
    '''
    Device Info System -> set of function to get system information about single Music Cast device
    '''

    def __system_api(self, endpoint):
        return self.api('netusb', endpoint)

    def get_preset_info(self):
        return self.__system_api('getPresetInfo')

    def get_play_info(self):
        return self.__system_api('getPlayInfo')
