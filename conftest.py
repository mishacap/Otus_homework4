import pytest

from api_clients.brewery_api_client import BreweryApiClient
from api_clients.dog_api_client import DogApiClient


@pytest.fixture(scope="function")
def dog_api_client():
    client = DogApiClient()
    return client

def get_all_breeds_list():
    client = DogApiClient()
    return client.get_all_breeds_list()

@pytest.fixture(scope="function")
def brewery_api_client():
    client = BreweryApiClient()
    return client

