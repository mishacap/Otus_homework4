import pytest
from jsonschema import validate

from conftest import get_all_posts_ids
from file_helpers.csv_helper import read_lines_from_csv
from tests.jsonplaceholder_schemas import get_all_posts_schema, get_post_by_id_schema, create_post_schema


def test_get_all_posts_ids(jsonplaceholder_api_client):
    response = jsonplaceholder_api_client.get_all_posts()
    json_response = response.json()
    assert response.status_code == 200
    assert response.json()
    validate(instance=json_response, schema=get_all_posts_schema)


@pytest.mark.parametrize("query", get_all_posts_ids())
def test_get_post_by_id(jsonplaceholder_api_client, query):
    response = jsonplaceholder_api_client.get_post_by_id(query)
    json_response = response.json()
    assert response.status_code == 200
    assert response.json()
    validate(instance=json_response, schema=get_post_by_id_schema)
    assert json_response["id"] == query


@pytest.mark.parametrize("data", read_lines_from_csv(), ids=["post 1",
                                                             "post 2",
                                                             "post 3",
                                                             "post 4",
                                                             "post 5",
                                                             "post 6",
                                                             "post 7",
                                                             "post 8",
                                                             "post 9",
                                                             "post 10"])
def test_create_post(jsonplaceholder_api_client, data):
    response = jsonplaceholder_api_client.create_post(data=data)
    json_response = response.json()
    assert response.status_code == 201
    assert response.json()
    validate(instance=json_response, schema=create_post_schema)






