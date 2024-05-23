import pytest
import requests
import json
from conftest import brewery_api_client, get_all_breweries, get_all_cities
from jsonschema import validate
from tests.breweries_schemas import get_list_of_breweries_schema, get_single_brewery_by_id_schema, \
    get_get_breweries_by_city_schema


def test_get_list_of_breweries(brewery_api_client):
    response = brewery_api_client.get_list_of_breweries()
    json_response = response.json()
    assert response.status_code == 200
    assert response.json()
    validate(instance=json_response, schema=get_list_of_breweries_schema)


@pytest.mark.parametrize("query", get_all_breweries())
def test_get_single_brewery_by_id(brewery_api_client, query):
    response = brewery_api_client.get_single_brewery_by_id(query)
    assert response is not None, "No response received from the API"
    assert response.status_code == 200
    json_response = response.json()
    assert response.json()
    validate(instance=json_response, schema=get_single_brewery_by_id_schema)


@pytest.mark.parametrize("query", get_all_cities())
def test_get_breweries_by_city(brewery_api_client, query):
    response = brewery_api_client.get_breweries_by_city(query)
    assert response is not None, "No response received from the API"
    assert response.status_code == 200
    json_response = response.json()
    assert response.json()
    validate(instance=json_response, schema=get_get_breweries_by_city_schema)










