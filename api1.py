import pytest
import requests

BASE_URL = "https://reqres.in/"


def test_get_users():
    # Make the API call
    response = requests.get(BASE_URL + "api/users?page=2")

    # Check if the response is successful (status code 200)
    assert response.status_code == 200

    # You can also check the response content to ensure it's in the expected format
    response_data = response.json()
    email_to_find = 'michael.lawson@reqres.in'
    assert any(entry['email'] == email_to_find for entry in response_data['data'])
    # assert "michael.lawson@reqres.in" in response_data
    # assert isinstance(response_data["michael.lawson@reqres.in"], list)
    print(response_data)
