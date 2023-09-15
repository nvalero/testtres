from utils import api_call
import models.theme_values_macroregion as theme_values_macroregion
import constants.endpoints as endpoints
import constants.headers as headers
import constants.general as constants
import models.error_response as error_response
import models.error_ok_response as error_ok_response

#PENDIENTE ESTE TEST, 3382 se parece a 3381 --> esteban
payload_path = constants.payload_path + 'test_global_themes_values_macroregion\\'
endpoint = endpoints.qa_global_url

def post(payload_file, status_code_expected):
    head = api_call.get_headers()
    head['Content-Type'] = headers.ContentType
    replace_dictionary = {"sub-region": "sub_region", "macro-region": "macro_region"}
    return api_call.post(head, endpoint, payload_path + payload_file, status_code_expected, replace_dictionary)


def validate_response(response, class_type,  test_name, endpoint, value_return):
    try:
        response_set: class_type = class_type(**response)
    except:
        assert 1 == 2, test_name + ': ' + endpoint + ', Service must return correct structure'
    if value_return != '':
        assert response.get('status') == value_return, test_name + ': ' + endpoint + ', Service must return ' + value_return


# HW-3381
def test_blank_parameters():
    response = post('data_not_using_parameters.json', 200)
    validate_response(response, error_ok_response.ResponseError, 'test_blank_parameters', endpoint, '')
    # try:
    #     response_set: error_ok_response.ResponseError = error_ok_response.ResponseError(**response)
    # except:
    #     assert 1 == 2, 'test_blank_parameters: ' + endpoint + ', Service must return correct structure'

#
# # HW-3382
# def test_incorrect_parameters():
#     response = post(theme_values_macroregion.ThemeValuesMacroRegion, 'data_incorrect_parameters.json', 500)
#     assert response.get('status') == 'INTERNAL_SERVER_ERROR', \
#         'test_incorrect_parameters: ' + endpoint + ', Service must return INTERNAL_SERVER_ERROR'
#

# HW-3380
def test_wrong_parameters():
    response = post('data_wrong_parameters.json', 500)
    validate_response(response, error_response.ResponseError, 'test_wrong_parameters', endpoint, 'INTERNAL_SERVER_ERROR')
    # try:
    #     response_set: error_response.ResponseError = error_response.ResponseError(**response)
    # except:
    #     assert 1 == 2, 'test_wrong_parameters: ' + endpoint + ', Service must return correct structure'
    # assert response.get('status') == 'INTERNAL_SERVER_ERROR', \
    #     'test_wrong_parameters: ' + endpoint + ', Service must return INTERNAL_SERVER_ERROR'


# HW-3379
def test_api_success():
    response = post('data_correct_parameters.json', 200)
    validate_response(response, theme_values_macroregion.ThemeValuesMacroRegion, 'test_api_success', endpoint, '')
    # try:
    #     response_set: theme_values_macroregion.ThemeValuesMacroRegion = theme_values_macroregion.ThemeValuesMacroRegion(**response)
    # except:
    #     assert 1 == 2, 'test_api_success: ' + endpoint + ', Service must return correct structure'


# test_api_success()
# test_not_using_parameters()
# test_wrong_parameters()
# test_incorrect_parameters()
