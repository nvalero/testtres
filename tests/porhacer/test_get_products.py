from utils import api_call
import constants.endpoints as endpoints
import constants.general as constants
import models.theme_values_incorrect as theme_values_incorrect
import models.theme_values as theme_values
import constants.headers as headers


# FALTAAAAAAAAAAAAAAAAAAAAA
endpoint = endpoints.qa_scenario_id_url
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
    try:
        response_set: class_type = class_type(**response)
    except:
        assert 1 == 2, test_name + ': ' + endpoint + ', Service must return correct structure'
    if value_return != '':
        assert response.get('status') == value_return, test_name + ': ' + endpoint + ', Service must return ' + value_return
# HW-4307



# HW-4306
def test_incorrect_parameters():
    response = post('data_incorrect_parameters.json', 200)
    validate_response(response, theme_values_incorrect.ThemeValuesIncorrect, 'test_incorrect_parameters', endpoint, 'OK')


# HW-4305
def test_api_success():
    response = post('data_correct_parameters.json', 200)
    validate_response(response, theme_values.ThemeValues, 'test_api_success', endpoint, '')

