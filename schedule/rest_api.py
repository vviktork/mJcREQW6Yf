import requests
import json


def rest_api(api, data):
    HEADERS = {}
    URL = 'http://127.0.0.1:8000/api/v1/' + api
    try:
        if api == 'servis2':
            DATA = json.dumps({'formula': data[0],
                               'interval': data[1],
                               'dt': data[2]
                               })
        elif api == 'servis3':
            DATA = json.dumps(data)

        response = requests.post(URL, data=DATA, headers=HEADERS).json()
    except Exception as e:
        response = 'Request: ' + str(e)

    return response



