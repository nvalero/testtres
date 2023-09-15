import requests
import constants.headers as headers
import curlify
import json

def get_headers():
    return {
        'Authorization': headers.Authorization,
        'Cookie': headers.Cookie
    }

def replace_data(cadena, replace_dictionary):
    for i in replace_dictionary:
        #print(i, mydict[i])
        cadena = cadena.replace(i, replace_dictionary[i])
    return cadena

def get(headers, url, status_code_expected):
    response = requests.get(url, headers=headers)
    print(curlify.to_curl(response.request))
    print('Response -->' + response.text)
    if (response.text != ''):
        data = response.json()
    else:
        data = ''
    assert response.status_code == status_code_expected, 'status code must be ' + str(status_code_expected)  + ' but received ' + str(response.status_code)
    return data


def post(headers, url, payload_file, status_code_expected, replace_dictionary):
    contents = open(payload_file).read()
    response = requests.post(url, headers=headers, data=contents)
    print(curlify.to_curl(response.request))
    print('Response -->' + response.text)
    cadena = replace_data(response.text, replace_dictionary)
    if (cadena != ''):
        data = json.loads(cadena)
    else:
        data = ''
    assert response.status_code == status_code_expected, 'status code must be ' + str(status_code_expected) + ' but received ' + str(response.status_code)
    return data


def post_with_file(headers, class_type, url, payload_file, body_file, status_code_expected, replace_dictionary):
    response = requests.post(url, headers=headers, files={'file': ('materials.csv', open(payload_file, 'rb'), 'text/csv')})
    print(curlify.to_curl(response.request))
    print('Response -->' + response.text)
    cadena = replace_data(response.text, replace_dictionary)
    # cadena = response.text.replace("scenario.status", "scenario_status").replace("sub-region", "sub_region").replace("macro-region", "macro_region")
    data = json.loads(cadena)
    print(response_set)
    assert response.status_code == status_code_expected, 'status code must be ' + str(status_code_expected) + ' but received ' + str(response.status_code)
    return data
