import pytest
from jsonschema import validate

from tests.jsonplaceholder_schemas import get_all_posts_schema


def test_get_all_posts_ids(jsonplaceholder_api_client):
    response = jsonplaceholder_api_client.get_all_posts()
    json_response = response.json()
    assert response.status_code == 200
    assert response.json()
    validate(instance=json_response, schema=get_all_posts_schema)


