import requests
import json

musiccastIP = "192.168.7.x"
getDeviceInfoPath = "/YamahaExtendedControl/v1/system/getDeviceInfo"
response = requests.get("http://" + musiccastIP + getDeviceInfoPath)
print(response.json()['model_name'])

# x = json.load(response.json())
# print(x)