
'''
Discovery related methods
'''
import socket
import re
from xml.dom import minidom, DOMException
import requests


def __get_xml(uri):
    response = requests.get(uri)
    return minidom.parseString(response.text)


def __check_correct_manufacturer(xml):
    yamaha = "Yamaha Corporation"
    items = xml.getElementsByTagName('manufacturer')
    try:
        items = xml.getElementsByTagName('manufacturer')
        manufacturer = items[0].firstChild.data
        if manufacturer == yamaha:
            return True
        return False
    except DOMException:
        return False


def __get_address_and_control_path(xml):
    try:
        x_url_base = xml.getElementsByTagName('yamaha:X_URLBase')
        url_base = x_url_base[0].firstChild.data
        x_control_url = xml.getElementsByTagName('yamaha:X_yxcControlURL')
        cotrol_url = x_control_url[0].firstChild.data
        x_name = xml.getElementsByTagName('friendlyName')
        name = x_name[0].firstChild.data
        return {
            'name': name,
            'urlBase': url_base,
            'controlUrl': cotrol_url
        }
    except DOMException:
        return None


def __get_msearch_message():
    message = \
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
    return bytes(message, "utf-8")


def __get_description(response):
    match_description = re.findall(r"Location: (\S+)", response, re.MULTILINE)
    match_model_name = re.findall(
        r"X-ModelName: (\S+)", response, re.MULTILINE)
    return (
        match_description[0] if match_description else None,
        match_model_name[0] if match_model_name else None
    )


def __discover_devices(timeout):
    sendto_socket = socket.socket(
        socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sendto_socket.settimeout(timeout)
    sendto_socket.sendto(__get_msearch_message(), ('239.255.255.250', 1900))
    devices = []
    try:
        while True:
            data, (addr) = sendto_socket.recvfrom(65507)
            description, model_name = __get_description(data.decode("utf-8"))
            if(description is not None and model_name is not None):
                devices.append((addr, description, model_name))
    except socket.timeout:
        pass

    return devices


def discover_music_cast_devices(timeout=2):
    devices = __discover_devices(timeout)
    descriptions = map(lambda device: device[1], devices)
    xmls = map(__get_xml, descriptions)
    correct = filter(__check_correct_manufacturer, xmls)
    data = map(__get_address_and_control_path, correct)
    return data
