import pytest
from utils import api_call
import models.model_manager_agronomics_run as model_manager_agronomics_run
import models.agronomics_run as agronomics_run
import models.errors_response_errors_list as errors_response_errors_list
import constants.endpoints as endpoints
import constants.general as constants
import constants.headers as headers


payload_path = constants.payload_path + 'test_agronomics_run\\'
endpoint = endpoints.qa_agronomics_url
endpoint_id = endpoints.qa_agronomics_run_id_url

#FALTAAAAAAAAAAAAAAAAAAAAAAAAAAA


def get(endpoint, status_code_expected):
    head = api_call.get_headers()
    return api_call.get(head, endpoint, status_code_expected)

def post(payload_file, status_code_expected):
    head = api_call.get_headers()
    head['Content-Type'] = headers.ContentType
    replace_dictionary = {"scenario.status": "scenario_status", "sub-region": "sub_region", "macro-region": "macro_region",
                          "scenario.environment": "scenario_environment", "scenario.planting-date": "scenario_planting_date",
                          "scenario.year": "scenario_year"}
    return api_call.post(head, endpoint, payload_path + payload_file, status_code_expected,
                         replace_dictionary)


def validate_response(response, class_type,  test_name, endpoint, value_return):
    if value_return != '':
        try:
            response_set: class_type = class_type(**response)
        except:
            assert 1 == 2, test_name + ': ' + endpoint + ', Service must return correct structure'
        assert response.get('status') == value_return, test_name + ': ' + endpoint + ', Service must return ' + value_return
        return response_set


# HW-4557
def test_not_using_parameters():
    response = post('data_not_using_parameters.json', 200)
    validate_response(response, errors_response_errors_list.ResponseError, 'test_not_using_parameters', endpoint, '')


# HW-4556
def test_incorrect_parameters():
    response = post('data_incorrect_parameters.json', 204)
    validate_response(response, None, 'test_incorrect_parameters', endpoint, '')


# HW-4558
def test_wrong_parameters():
    response = post('data_wrong_parameters.json', 400)
    validate_response(response, errors_response_errors_list.ResponseError, 'test_wrong_parameters', endpoint, 'BAD_REQUEST')


# HW-4555  --> falta probar
def test_api_success():
    response = post('data_correct_parameters.json', 200)
    response_set = validate_response(response, model_manager_agronomics_run.ResponseModelManagerAgronomicsRun, 'test_api_success', endpoint, '')
    endpoint_to_test = endpoint_id.format('runId', response_set.data.runId)
    response = get(endpoint_to_test, 200)
    validate_response(response, agronomics_run.ResponseAgronomicsRun, 'test_api_success', endpoint_to_test, '')

