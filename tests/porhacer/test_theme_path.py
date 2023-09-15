from utils import api_call
import models.theme_path as theme_path
import constants.endpoints as endpoints


endpoint = endpoints.qa_scenarios_url
# esteban nuevamente --> no se si es este TC https://gdmseeds.atlassian.net/browse/HW-4128 no tiene descripcion

def get(class_type, endpoint, status_code_expected):
    head = api_call.get_headers()
    return api_call.get(head, endpoint, status_code_expected)

# HW-xxxx
def test_incorrect_parameters(path):
    response = get(theme_path.ThemePath, endpoints.qa_theme_path_url + path, 200)
    x = 1

# HW-xxxx
def test_api_success(path):
    response = get(theme_path.ThemePath, endpoints.qa_theme_path_url + path, 200)
    y = 1

paths = [ 'planting-date']

for path in paths:
    test_api_success(path)
    x=8
    # TODO si aquino hay parametro, aplica el otro test??
    #test_incorrect_parameters(path)
