"""
high level support for doing this and that.
"""

import requests


def call_api(url_base, path, control_url='/YamahaExtendedControl/v1/'):
    base_uri = '{url_base}/{control_url}/{path}'
    uri = base_uri.format(url_base=url_base.strip('/'),
                          path=path.strip('/'),
                          control_url=control_url.strip('/'))
    response = requests.get(uri)
    return response.json()
