from utils import api_call
import constants.endpoints as endpoints
import models.errors_response_errors_list as errors_response_errors_list
from models import scenario_id_agronomics_sets


endpoint = endpoints.qa_scenario_id_agronomics_sets_url


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


# HW-4154 --> es el mismo que HW-4152--> falta, revisar con esteban
def test_non_existent_parameters():
    endpoint_to_test = endpoint.format(idScenario='5061fe0b-97f1-4684-9aff-7bcdd1fb9a5a', name='test_02')\
        .replace('name', 'namexx')
    response = get(endpoint_to_test, 400)
    validate_response(response, errors_response_errors_list.ResponseError, 'test_non_existent_parameters', endpoint_to_test, 'BAD_REQUEST')


# HW-4153
def test_blank_parameters():
    endpoint_to_test = endpoint.format(idScenario='5061fe0b-97f1-4684-9aff-7bcdd1fb9a5a', name='').replace('name', '')
    response = get(endpoint_to_test, 400)
    validate_response(response, errors_response_errors_list.ResponseError, 'test_blank_parameters', endpoint_to_test, 'BAD_REQUEST')


# HW-4152--> falta, revisar con esteban
def test_incorrect_parameters():
    endpoint_to_test = endpoint.replace('name', 'namex').format(idScenario='5061fe0b-97f1-4684-9aff-7bcdd1fb9a5a', namex='test_02')
    response = get(endpoint_to_test, 400)
    validate_response(response, errors_response_errors_list.ResponseError, 'test_incorrect_parameters', endpoint_to_test, 'BAD_REQUEST')


# HW-4151
def test_api_success():
    endpoint_to_test = endpoint.format(idScenario='5061fe0b-97f1-4684-9aff-7bcdd1fb9a5a', name='name')
    response = get(endpoint_to_test, 200)
    validate_response(response, scenario_id_agronomics_sets.ScenarioIdAgronomicsSetsResult, 'test_api_success', endpoint_to_test, '')
