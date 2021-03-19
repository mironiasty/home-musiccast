'''
Just API demo
'''

import pprint
from lib.devices_discovery import discover_music_cast_devices
from lib.device_info import DeviceInfo


for device in discover_music_cast_devices(4):
    device_info = DeviceInfo(device['base_url'], device['control_url'])
    pprint.pprint(device_info.get_device_info())
