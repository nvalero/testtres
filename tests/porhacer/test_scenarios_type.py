from utils import api_call
import models.scenarios_type as scenarios_type
import models.errors_response_errors_list as errors_response_errors_list
import constants.endpoints as endpoints
import constants.headers as headers
import constants.general as constants


payload_path = constants.payload_path + 'test_scenarios_type\\'
endpoint = endpoints.qa_scenarios_type_url


def post(endpoint, payload_file, status_code_expected):
    head = api_call.get_headers()
    head['Content-Type'] = headers.ContentType
    replace_dictionary = {}
    return api_call.post(head, endpoint, payload_path + payload_file, status_code_expected,
                         replace_dictionary)


def validate_response(response, class_type,  test_name, endpoint, value_return):
    if value_return != '':
        try:
            response_set: class_type = class_type(**response)
        except:
            assert 1 == 2, test_name + ': ' + endpoint + ', Service must return correct structure'
        assert response.get('status') == value_return, test_name + ': ' + endpoint + ', Service must return ' + value_return


# HW-4269 --> preguntar a esteban , porque responde otra cosa alo que dice el test
def test_not_using_parameters():
    endpoint_to_test =  endpoint + ''
    response = post(endpoint_to_test, 'data_not_using_parameters.json', 400)
    validate_response(response, errors_response_errors_list.ResponseError, 'test_not_using_parameters', endpoint_to_test, 'BAD_REQUEST')


# HW-4268
def test_incorrect_parameters():
    endpoint_to_test = endpoint + 'type=new'
    response = post(endpoint_to_test, 'data_incorrect_parameters.json', 400)
    validate_response(response, errors_response_errors_list.ResponseError, 'test_incorrect_parameters', endpoint_to_test, 'BAD_REQUEST')


# HW-4270
def test_wrong_parameters():
    endpoint_to_test = endpoint + 'typexx=newxx'
    response = post(endpoint_to_test, 'data_wrong_parameters.json', 400)
    validate_response(response, errors_response_errors_list.ResponseError, 'test_wrong_parameters', endpoint_to_test, 'BAD_REQUEST')


# HW-4267 --> pendiente por probar
def test_api_success():
    endpoint_to_test = endpoint + 'type=new'
    response = post(endpoint_to_test, 'data_correct_parameters.json', 200)
    validate_response(response, scenarios_type.ResponseScenariosType, 'test_api_success', endpoint_to_test, '')
