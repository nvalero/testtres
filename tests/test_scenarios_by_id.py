from utils import api_call
import models.scenario_id as scenario
import constants.endpoints as endpoints
import models.error_ok_response_list as error_ok_response_list

# estos tests están listos
endpoint = endpoints.qa_scenario_id_url

# https://gdmseeds.atlassian.net/browse/HW-5931 --> revisar esteban nuevamente, se perece  a los que estan aqui
# https://gdmseeds.atlassian.net/browse/HW-5930

def get(endpoint, status_code_expected):
    head = api_call.get_headers()
    return api_call.get(head, endpoint, status_code_expected)


def validate_response(response, class_type,  test_name, endpoint, value_return):
    try:
        response_set: class_type = class_type(**response)
    except:
        assert 1 == 2, test_name + ': ' + endpoint + ', Service must return correct structure'
    if value_return != '':
        assert response.get('status') == value_return, test_name + ': ' + endpoint + ', Service must return ' + value_return


# HW-4201
def test_incorrect_parameters():
    endpoint_to_test = endpoint.format(idScenario='5061fe0b-97f1-4684-9aff-7bcdd1fb9a5aXXX')
    response = get(endpoint_to_test, 200)
    validate_response(response, error_ok_response_list.ResponseError, 'test_incorrect_parameters', endpoint, '')


# HW-4200
def test_api_success():
    endpoint_to_test = endpoint.format(idScenario='5061fe0b-97f1-4684-9aff-7bcdd1fb9a5a')
    response = get(endpoint_to_test, 200)
    validate_response(response, scenario.ResponseScenario, 'test_api_success', endpoint_to_test, '')
