import pytest

from conftest import dog_api_client

import requests

import json

from jsonschema import validate

from schemas import get_random_dog_schema, get_all_breeds_schema, get_dog_by_breed

from api_clients.dog_api_client import DogApiClient


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


@pytest.mark.parametrize("query",
                         dog_api_client.get_all_breeds_list())
def test_get_dog_by_breed(dog_api_client, query):
    # breeds_list = dog_api_client.get_all_breeds_list
    response = dog_api_client.get_dog_by_breed(query)
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["status"] == "success"
    assert response.json()
    validate(instance=json_response, schema=get_dog_by_breed)







