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


@pytest.fixture(scope='session')
def get_empty_cart_message():
    return test_data()['empty_cart_message']


@pytest.fixture(scope='session')
def get_home_title():
    return test_data()['home_page_title']


@pytest.fixture(scope='session')
def get_add_new_product_headline():
    return test_data()['add_new_product_headline']
