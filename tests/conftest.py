import pytest
import json
import os

print(os.getcwd() + "/tests/test_data.json")
path_to_json_data = os.getcwd() + "/tests/test_data.json"


@pytest.fixture(scope='session')
def test_data():
    with open(path_to_json_data) as data:
        return json.load(data)


@pytest.fixture(scope='session')
def admin_data():
    return test_data()['admin_credentials']['name'], test_data()['admin_credentials']['password']
