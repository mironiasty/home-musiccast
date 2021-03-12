
from .callApi import callApi

class DeviceInfo:
    ENDPOINTS = {
        'getDeviceInfo': 'system/getDeviceInfo'
    }
    
    deviceAddress = ""
    
    def __init__(self, deviceAddress):
        self.deviceAddress = deviceAddress

    def getDeviceInfo(self):
        return callApi(self.deviceAddress, DeviceInfo.ENDPOINTS['getDeviceInfo'])