import pytest
from api_clients.dog_api_client import DogApiClient


@pytest.fixture(scope="function")
def dog_api_client():
    client = DogApiClient()
    return client
