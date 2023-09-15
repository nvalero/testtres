import pytest

someobj = 1

@pytest.fixture(scope='session', autouse=True)
def prep_someobj(request):
    someobj = 3
    print('someobj' + str(someobj))