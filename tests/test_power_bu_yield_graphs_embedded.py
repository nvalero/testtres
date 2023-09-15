from utils import api_call
import models.power_bu_yield_graphs_embedded as power_bu_yield_graphs_embedded
import models.errors_response_errors_list as errors_response_errors_list
import constants.endpoints as endpoints
import constants.general as constants

#este ya está listo
payload_path = constants.payload_path + 'test_power_bu_yield_graphs_embedded\\'
endpoint = endpoints.qa_graphics_report_url


def get(endpoint, status_code_expected):
    head = api_call.get_headers()
    return api_call.get(head, endpoint, status_code_expected)


def validate_response(response, class_type,  test_name, endpoint, value_return):
    if value_return != '':
        try:
            response_set: class_type = class_type(**response)
        except:
            assert 1 == 2, test_name + ': ' + endpoint + ', Service must return correct structure'
        assert response.get('status') == value_return, test_name + ': ' + endpoint + ', Service must return ' + value_return


# HW-5251 - Automated
def test_not_using_parameters():
    endpoint_to_test = endpoint
    response = get(endpoint_to_test, 400)
    validate_response(response, errors_response_errors_list.ResponseError, 'test_not_using_parameters', endpoint_to_test, '')


# HW-5253 - Automated
def test_incorrect_parameters():
    endpoint_to_test = endpoint + 'scenariossss'
    response = get(endpoint_to_test, 400)
    validate_response(response, errors_response_errors_list.ResponseError, 'test_incorrect_parameters',
                      endpoint_to_test, 'BAD_REQUEST')


# HW-5254 - Automated
def test_wrong_parameters():
    endpoint_to_test = endpoint.replace('report', 'asdf') + 'ssssss'
    response = get(endpoint_to_test, 400)
    validate_response(response, errors_response_errors_list.ResponseError, 'test_wrong_parameters', endpoint_to_test, 'BAD_REQUEST')


# HW-5252 - Automated
def test_api_success():
    endpoint_to_test = endpoint + 'scenario'
    response = get(endpoint_to_test, 200)
    validate_response(response, power_bu_yield_graphs_embedded.ResultGraphsEmbedded, 'test_api_success', endpoint_to_test, '')
