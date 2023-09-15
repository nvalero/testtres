from utils import api_call
import models.scenario_query_regions as scenario_query_regions
import models.errors_response_errors_list as errors_response_errors_list
import models.error_response as error_response
import constants.endpoints as endpoints
import constants.headers as headers
import constants.general as constants

#este ya está listo
payload_path = constants.payload_path + 'test_display_filter_results\\'
endpoint = endpoints.qa_regions_url

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


# HW-3628 - Automated
def test_not_using_parameters():
    response = post('data_not_using_parameters.json', 200)
    validate_response(response, scenario_query_regions.ScenarioQueryRegionsResult, 'test_not_using_parameters', endpoint, '')


# HW-3627 - Automated
def test_incorrect_parameters():
    response = post('data_incorrect_parameters.json', 400)
    validate_response(response, errors_response_errors_list.ResponseError, 'test_incorrect_parameters',
                      endpoint, 'BAD_REQUEST')
    # assert response.get('status') == 'INTERNAL_SERVER_ERROR', \
    #     'test_incorrect_parameters: ' + endpoint + ', Service must return INTERNAL_SERVER_ERROR'


# HW-3629 - Automated
def test_wrong_parameters():
    response = post('data_wrong_parameters.json', 500)
    validate_response(response, error_response.ResponseError, 'test_wrong_parameters', endpoint, 'INTERNAL_SERVER_ERROR')


# HW-3626 - Automated
def test_api_success():
    response = post('data_correct_parameters.json', 200)
    validate_response(response, scenario_query_regions.ScenarioQueryRegionsResult, 'test_api_success',
                      endpoint, '')
