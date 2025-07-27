import requests

def test_api_status():
    headers = {
        "x-api-key": "reqres-free-v1"  # Add your API key here
    }
    response = requests.get("https://reqres.in/api/users/2", headers=headers)
    assert response.status_code == 200
