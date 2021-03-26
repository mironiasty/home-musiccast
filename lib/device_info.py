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

    def api(self, endpoint):
        return call_api(self.base_url,
                        endpoint, self.control_url)

    def get_url(self):
        return self.base_url


class DeviceInfoSystem(DeviceInfo):
    '''
    Device Info System -> set of function to get system information about single Music Cast device
    '''

    __ENDPOINTS = {
        'getDeviceInfo': 'system/getDeviceInfo',
        'getFeatures': 'system/getFeatures'
    }

    def get_device_info(self):
        return self.api(self.__ENDPOINTS['getDeviceInfo'])

    def get_features(self):
        return self.api(self.__ENDPOINTS['getFeatures'])


class DeviceInfoNetusb(DeviceInfo):
    '''
    Device Info System -> set of function to get system information about single Music Cast device
    '''

    __ENDPOINTS = {
        'getPresetInfo': 'netusb/getPresetInfo',
        'getPlayInfo': 'netusb/getPlayInfo'
    }

    def get_preset_info(self):
        return self.api(self.__ENDPOINTS['getPresetInfo'])

    def get_play_info(self):
        return self.api(self.__ENDPOINTS['getPlayInfo'])
