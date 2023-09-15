from utils import api_call
import models.errors_response_errors_list as errors_response_errors_list
import constants.endpoints as endpoints
import constants.headers as headers
import constants.general as constants
from models import agronomics_sets


payload_path = constants.payload_path + 'test_agronomics_sets\\'
endpoint = endpoints.qa_agronomics_sets_url


def post(payload_file, status_code_expected):
    head = api_call.get_headers()
    head['Content-Type'] = headers.ContentType
    return api_call.post(head, endpoint, payload_path + payload_file,
                             status_code_expected, {})


def validate_response(response, class_type,  test_name, endpoint, value_return):
    if value_return != '':
        try:
            response_set: class_type = class_type(**response)
        except:
            assert 1 == 2, test_name + ': ' + endpoint + ', Service must return correct structure'
        assert response.get('status') == value_return, test_name + ': ' + endpoint + ', Service must return ' + value_return

#
# # HW-xxxx
# def test_forbidden():
#     head = api_call.get_headers()
#     head['Authorization'] = 'Bearer xxxx'
#     return api_call.post(head, agronomics_sets.ResponseAgronomicSet, endpoint, payload_path + 'data_correct_parameters.json',
#                              403, {})


# HW-5938
def test_blank_parameters():
    response = post('data_not_using_parameters.json', 200)
    validate_response(response, None, 'test_blank_parameters', endpoint, '')


# HW-5939
def test_incorrect_parameters():
    response = post('data_incorrect_parameters.json', 400)
    validate_response(response, errors_response_errors_list.ResponseError, 'test_incorrect_parameters',
                      endpoint, 'BAD_REQUEST')


# HW-5937 --> falta por probar
def test_api_success():
    response = post('data_correct_parameters.json', 200)
    validate_response(response, agronomics_sets.ResponseAgronomicSet, 'test_api_success', endpoint, '')
