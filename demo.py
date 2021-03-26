'''
Just API demo
'''

import pprint
from lib.devices_discovery import get_device_by_name
from lib.device_info import DeviceInfoNetusb


# for device in discover_music_cast_devices(4):
#     device_info = (device['base_url'], device['control_url'])
#     pprint.pprint(device_info.get_device_info())
dev = get_device_by_name("Sypialnia")
info = DeviceInfoNetusb(dev)
pprint.pprint(info.get_preset_info())
