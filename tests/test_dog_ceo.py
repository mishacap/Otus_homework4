import pytest

from conftest import dog_api_client, get_all_breeds_list
from jsonschema import validate
from dogs_schemas import get_random_dog_schema, get_all_breeds_schema, get_dog_by_breed_schema, get_all_sub_breeds_schema, \
    get_random_dog_by_breed_schema


def test_get_random_dog(dog_api_client):
    response = dog_api_client.get_random_dog()
    json_response = response.json()
    assert response.status_code == 200
    assert json_response["status"] == "success"
    assert response.json()
    validate(instance=json_response, schema=get_random_dog_schema)


def test_get_all_breeds(dog_api_client):
    response = dog_api_client.get_all_breeds()
    json_response = response.json()
    assert response.status_code == 200
    assert json_response["status"] == "success"
    assert response.json()
    validate(instance=json_response, schema=get_all_breeds_schema)


@pytest.mark.parametrize("query", get_all_breeds_list())
def test_get_dog_by_breed(dog_api_client, query):
    response = dog_api_client.get_dog_by_breed(query)
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["status"] == "success"
    assert response.json()
    validate(instance=json_response, schema=get_dog_by_breed_schema)


@pytest.mark.parametrize("query", get_all_breeds_list())
def test_get_all_sub_breeds(dog_api_client, query):
    response = dog_api_client.get_all_sub_breeds(query)
    assert response.status_code == 200
    json_response = response.json()
    validate(instance=json_response, schema=get_all_sub_breeds_schema)

@pytest.mark.parametrize("query", get_all_breeds_list())
def test_get_random_dog_by_breed(dog_api_client, query):
    response = dog_api_client.get_random_dog_by_breed(query)
    assert response.status_code == 200
    json_response = response.json()
    validate(instance=json_response, schema=get_random_dog_by_breed_schema)




