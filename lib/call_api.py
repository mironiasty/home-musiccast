"""
high level support for doing this and that.
"""

import requests


def call_api(host, path):
    base_uri = 'http://{host}/YamahaExtendedControl/v1/{path}'
    uri = base_uri.format(host=host, path=path)
    print(uri)
    response = requests.get(uri)
    return response.json()
