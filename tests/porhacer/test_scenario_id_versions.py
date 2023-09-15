from utils import api_call
import models.scenario_id_versions as scenario_id_versions
import constants.endpoints as endpoints

# falta terminar este
endpoint = endpoints.qa_scenario_id_versions_url

def get(class_type, endpoint, status_code_expected):
    head = api_call.get_headers()
    response = api_call.get(head, endpoint, status_code_expected)

# HW-5635
# HW-5634
def test_incorrect_parameters():
    response = get(scenario_id_versions.ScenarioIdVersionsResult, endpoint.format(idScenario='5061fe0b-97f1-4684-9aff-7bcdd1fb9a5aXXX'), 200)

# HW-5633
def test_api_success():
    response = get(scenario_id_versions.ScenarioIdVersionsResult, endpoint.format(idScenario='5061fe0b-97f1-4684-9aff-7bcdd1fb9a5a'), 200)
