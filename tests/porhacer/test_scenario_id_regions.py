import pytest
from utils import api_call
import models.scenario_id_regions as scenario_id_regions
import constants.endpoints as endpoints


endpoint = endpoints.qa_scenario_id_region_url


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


# HW-4544 --> no lo probé, debo colocar un ID correcto
def test_api_success():
    endpoint_to_test = endpoint.format(idScenario='5061fe0b-97f1-4684-9aff-7bcdd1fb9a5a')
    response = get(endpoint_to_test, 200)
    validate_response(response, scenario_id_regions.ScenarioIdRegionsResult, 'test_api_success', endpoint_to_test, '')
