import pytest
from jsonschema import validate

from conftest import get_all_posts_ids, get_all_users_ids
from file_helpers.csv_helper import read_lines_from_csv_create, read_lines_from_csv_update, read_ids_from_csv_update
from tests.jsonplaceholder_schemas import get_all_posts_schema, get_post_by_id_schema, create_and_update_post_schema, \
    get_all_post_by_user_shema


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


@pytest.mark.parametrize("data", read_lines_from_csv_create(), ids=["post 1",
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
    validate(instance=json_response, schema=create_and_update_post_schema)
    assert json_response["userId"] == data["userId"]
    assert json_response["title"] == data["title"]
    assert json_response["body"] == data["body"]


@pytest.mark.parametrize(
    ["data", "query"],
    [(data, query) for data, query in zip(read_lines_from_csv_update(), read_ids_from_csv_update())],
    ids=["update post 1", "update post 2", "update post 3", "update post 4", "update post 5",
         "update post 6", "update post 7", "update post 8", "update post 9", "update post 10"])
def test_update_post(jsonplaceholder_api_client, data, query):
    response = jsonplaceholder_api_client.update_post(data=data, query=query)
    json_response = response.json()
    assert response.status_code == 200
    assert json_response
    validate(instance=json_response, schema=create_and_update_post_schema)
    assert json_response["userId"] == data["userId"]
    assert json_response["title"] == data["title"]
    assert json_response["body"] == data["body"]


@pytest.mark.parametrize("query", get_all_users_ids())
def test_get_all_posts_by_user(jsonplaceholder_api_client, query):
    response = jsonplaceholder_api_client.get_all_post_by_user(query)
    json_response = response.json()
    assert response.status_code == 200
    assert response.json()
    validate(instance=json_response, schema=get_all_post_by_user_shema)
    for post in json_response:
        assert post["userId"] == query
