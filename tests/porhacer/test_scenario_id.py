from utils import api_call
import models.scenario_id as scenario_id
import models.error_response as error_response
import constants.endpoints as endpoints

# revisar, creo que lo debo eliminar porque lo sustotuye test_scenarios_by_id
endpoint = endpoints.qa_scenario_id_url

def get(class_type, endpoint, status_code_expected):
    head = api_call.get_headers()
    response = api_call.get(head, endpoint, status_code_expected)

# HW-xx
def test_incorrect_parameters():
    response = get(error_response.ResponseError, endpoint.format(idScenario='5061fe0b-97f1-4684-9aff-7bcdd1fb9a5aXXX'), 200)
    x = 1

# HW-xx
def test_api_success():
    response = get(scenario_id.ResponseScenario, endpoint.format(idScenario='5061fe0b-97f1-4684-9aff-7bcdd1fb9a5a'), 200)
    print(' xxxxxxxx --> ' + 'response')


#test_api_success()
# que codigo espera? está recibiendo un 200
