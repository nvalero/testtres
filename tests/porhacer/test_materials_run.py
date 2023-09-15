from utils import api_call
import models.model_manager_materials_run as model_manager_materials_run
import constants.endpoints as endpoints
import models.errors_response as errors_response
import models.errors_response_errors_list as errors_response_errors_list


endpoint = endpoints.qa_materials_run_url
#pendiente por probar,

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


# HW-3635
def test_blank_parameters():
    endpoint_to_test = endpoint.replace('run', '')
    response = get(endpoint_to_test, 400)
    validate_response(response, errors_response_errors_list.ResponseError, 'test_non_existent_parameters', endpoint_to_test, 'BAD_REQUEST')
    # try:
    #     response_set: errors_response_errors_list.ResponseError = errors_response_errors_list.ResponseError(**response)
    # except:
    #     assert 1 == 2, 'test_blank_parameters: ' + endpoint + ', Service must return correct structure'
    # assert response.get('status') == 'BAD_REQUEST', \
    #     'test_wrong_parameters: ' + endpoint + ', Service must return INTERNAL_SERVER_ERROR'

#preguntar a esteban, el parámetro a amandar, cual es? lo va a revisar
# HW-3636
def test_non_existent_parameters():
    endpoint_to_test = endpoint + '6726310'
    response = get(endpoint_to_test, 400)
    validate_response(response, errors_response.ResponseError, 'test_non_existent_parameters', endpoint_to_test, 'BAD_REQUEST')
    # try:
    #     response_set: errors_response.ResponseError = errors_response.ResponseError(**response)
    # except:
    #     assert 1 == 2, 'test_not_using_parameters: ' + endpoint + ', Service must return correct structure'
    # assert response.get('status') == 'BAD_REQUEST', \
    #     'test_wrong_parameters: ' + endpoint + ', Service must return INTERNAL_SERVER_ERROR'


# HW-3634
def test_incorrect_parameters():
    endpoint_to_test = endpoint + 'asdfasdfasdf'
    response = get(endpoint_to_test, 204)
    validate_response(response, model_manager_materials_run.ResponseModelManagerMaterialsRun, 'test_incorrect_parameters',
                      endpoint_to_test, '')


# HW-3633 --> preguntar a esteban de donde saco un ID para qeu me traiga datos - en paso 3 siguiente, llama a un proceso, y ahi le pasa un id, en save scenario, cuando llama run, run devuelve un id, es ese
def test_api_success():
    endpoint_to_test = endpoint + '6726310'
    response = get(endpoint_to_test, 200)
    validate_response(response, model_manager_materials_run.ResponseModelManagerMaterialsRun, 'test_api_success',
                      endpoint_to_test, '')
    #
    # try:
    #     response_set: model_manager_materials_run.ResponseModelManagerMaterialsRun = model_manager_materials_run.ResponseModelManagerMaterialsRun(**response)
    # except:
    #     assert 1 == 2, 'test_api_success: ' + endpoint + ', Service must return correct structure'
