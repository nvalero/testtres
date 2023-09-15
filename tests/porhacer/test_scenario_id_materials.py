from utils import api_call
import models.scenarios_id_materials as scenarios_id_materials
import constants.endpoints as endpoints
import models.error_ok_response_list as error_ok_response_list


endpoint = endpoints.qa_scenario_id_materials_url
#los 4225 y 4224 están bien, pero estos dos ,faltan, preguntarle a estebn porque no están claros
# https://gdmseeds.atlassian.net/browse/HW-4227
# https://gdmseeds.atlassian.net/browse/HW-4226
# https://gdmseeds.atlassian.net/browse/HW-5932 --> preguntar a esteban nuevamente, parecen repetidos, no están en el grupo de tests
# https://gdmseeds.atlassian.net/browse/HW-5933 --> preguntar a esteban nuevamente, parecen repetidos, no están en el grupo de tests

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


# HW-4225
def test_incorrect_parameters():
    endpoint_to_test = endpoint.format(idScenario='5061fe0b-97f1-4684-9aff-7bcdd1fb9a5aXXX')
    response = get(endpoint_to_test, 200)
    validate_response(response, error_ok_response_list.ResponseError, 'test_incorrect_parameters', endpoint_to_test, 'OK')


# HW-4224 --> preguntar a esteban un ID que devuelva datos --> id scenario
def test_api_success():
    endpoint_to_test = endpoint.format(idScenario='5061fe0b-97f1-4684-9aff-7bcdd1fb9a5a')
    response = get(endpoint, 200)
    validate_response(response, scenarios_id_materials.ResponseScenariosIdMaterials, 'test_api_success', endpoint_to_test, '')
    # try:
    #     response_set: scenarios_id_materials.ResponseScenariosIdMaterials = scenarios_id_materials.ResponseScenariosIdMaterials(**response)
    # except:
    #     assert 1 == 2, 'test_api_success: ' + endpoint + ', Service must return correct structure'
