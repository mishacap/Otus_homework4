import requests
import pytest

def test_check_status(base_url, status_code):
    url = f"{base_url}/"
    response = requests.get(url)
    assert response.status_code == int(status_code)

