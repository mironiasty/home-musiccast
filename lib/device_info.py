"""
Device Info class
"""
from .call_api import call_api


class DeviceInfo:
    '''
    Device info -> set of function to get information about single Music Cast device
    '''
    ENDPOINTS = {
        'getDeviceInfo': 'system/getDeviceInfo',
        'getFeatures': 'system/getFeatures'
    }

    device_addressa = ""

    def __init__(self, base_url, control_url='/YamahaExtendedControl/v1/'):
        self.base_url = base_url
        self.control_url = control_url

    def __api(self, endpoint):
        return call_api(self.base_url,
                        endpoint, self.control_url)

    def get_device_info(self):
        return self.__api(DeviceInfo.ENDPOINTS['getDeviceInfo'])

    def get_features(self):
        return self.__api(DeviceInfo.ENDPOINTS['getFeatures'])
