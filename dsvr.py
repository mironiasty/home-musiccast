import socket
import re

def getMSearchMessage():
    msg = \
        'M-SEARCH * HTTP/1.1\r\n' \
        'HOST:{host}:{port}\r\n' \
        'ST:{search_type}\r\n' \
        'MX:2\r\n' \
        'MAN:"ssdp:discover"\r\n' \
        '\r\n'.format(
            host="239.255.255.250",
            port="1900",
            search_type="urn:schemas-upnp-org:device:MediaRenderer:1"
        )
    return bytes(msg, "utf-8")

def getDescription(response):
    matchDescription = re.findall(r"Location: (\S+)", response, re.MULTILINE)
    matchModelName = re.findall(r"X-ModelName: (\S+)", response, re.MULTILINE)
    return (
        matchDescription[0] if matchDescription else None,
        matchModelName[0] if matchModelName else None
    )

def discoverDevices():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    s.settimeout(2)
    s.sendto(getMSearchMessage(), ('239.255.255.250', 1900))
    devices = []
    try:
        while True:
            data, (addr,port) = s.recvfrom(65507)
            description, modelName = getDescription(data.decode("utf-8"))
            devices.append((addr, description, modelName))
    except socket.timeout:
        pass

    return devices



print(discoverDevices())
