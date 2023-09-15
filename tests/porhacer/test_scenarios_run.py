from utils import api_call
import models.model_manager_scenarios_run as model_manager_scenarios_run
import models.errors_response_errors_list as errors_response_errors_list
import constants.endpoints as endpoints
import constants.headers as headers
import constants.general as constants

payload_path = constants.payload_path + 'test_scenarios_run\\'
endpoint = endpoints.qa_scenarios_run_url


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


# HW-5618
def test_not_using_parameters():
    response = post('data_not_using_parameters.json', 200)
    validate_response(response, errors_response_errors_list.ResponseError, 'test_not_using_parameters', endpoint, '')


# HW-5617
def test_incorrect_parameters():
    response = post('data_incorrect_parameters.json', 400)
    validate_response(response, errors_response_errors_list.ResponseError, 'test_incorrect_parameters', endpoint, 'BAD_REQUEST')


# HW-5616
def test_wrong_parameters():
    response = post('data_wrong_parameters.json', 400)
    validate_response(response, errors_response_errors_list.ResponseError, 'test_wrong_parameters', endpoint, 'BAD_REQUEST')

# HW-5615 --> preguntar a esteban, está fallando con este ID -- id de escenario
def test_api_success():
    response = post('data_correct_parameters.json', 200)
    validate_response(response, model_manager_scenarios_run.ResponseModelManagerScenariosRun, 'test_api_success', endpoint, '')

