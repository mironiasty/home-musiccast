
from .call_api import call_api


class DeviceInfo:
    ENDPOINTS = {
        'getDeviceInfo': 'system/getDeviceInfo',
        'getFeatures': 'system/getFeatures'
    }

    deviceAddress = ""

    def __init__(self, deviceAddress):
        self.deviceAddress = deviceAddress

    def getDeviceInfo(self):
        return call_api(self.deviceAddress, DeviceInfo.ENDPOINTS['getDeviceInfo'])

    def getgetFeatures(self):
        return call_api(self.deviceAddress, DeviceInfo.ENDPOINTS['getFeatures'])
