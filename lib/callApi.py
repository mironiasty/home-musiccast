import requests


def callApi(host, path):
    BASE_URI = 'http://{host}/YamahaExtendedControl/v1/{path}'
    uri = BASE_URI.format(host=host, path=path)
    print(uri)
    response = requests.get(uri)
    return response.json()
