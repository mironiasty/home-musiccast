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

    def __init__(self, deviceAddress):
        self.device_addressa = deviceAddress

    def get_device_info(self):
        return call_api(self.device_addressa, DeviceInfo.ENDPOINTS['getDeviceInfo'])

    def get_features(self):
        return call_api(self.device_addressa, DeviceInfo.ENDPOINTS['getFeatures'])
