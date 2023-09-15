from utils import api_call
import models.theme_values as theme_values
import models.theme_values_incorrect as theme_values_incorrect
import models.error_ok_response as error_ok_response
import models.error_response as error_response
import constants.endpoints as endpoints
import constants.headers as headers
import constants.general as constants

# estos tests están listos
payload_path = constants.payload_path + 'test_global_themes_values\\'
endpoint = endpoints.qa_global_url


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


# HW-3374 - Automated
def test_not_using_parameters():
    response = post('data_not_using_parameters.json', 200)
    validate_response(response, error_ok_response.ResponseError, 'test_not_using_parameters', endpoint, '')


# HW-3373 - Automated
def test_incorrect_parameters():
    response = post('data_incorrect_parameters.json', 200)
    validate_response(response, theme_values_incorrect.ThemeValuesIncorrect, 'test_incorrect_parameters', endpoint, 'OK')


# HW-3372 - Automated
def test_wrong_parameters():
    response = post('data_wrong_parameters.json', 500)
    validate_response(response, error_response.ResponseError, 'test_wrong_parameters', endpoint, 'INTERNAL_SERVER_ERROR')


# HW-3371
def test_api_success():
    response = post('data_correct_parameters.json', 200)
    validate_response(response, theme_values.ThemeValues, 'test_api_success', endpoint, '')
