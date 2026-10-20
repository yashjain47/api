import pytest
from utils.api_client import APIClient

@pytest.fixture(scope="module")
def api_client():
    return APIClient()


def test_get_users(api_client):

    'Getting All Users Data'
    response = api_client.get_request("users")
    print(response.json())
    assert response.status_code == 200                                                                                                          
    assert len(response.json()) != 0



def test_create_users(api_client,load_user_data):

    'Getting Data from Json File'
    user_data = load_user_data
    
    'Creating the Entry in the Database'
    response = api_client.post_request("users",user_data)
    assert response.status_code == 201
    print("\nResponse Data : ",response.json())
    assert response.json()['name'] == user_data['name']

    'Verifying the Posted Data'
    id = response.json()['id']
    print(f"ID: {id}")
    response = api_client.get_request(f"users/{1}")
    print(response.json())
    assert response.status_code == 200



def test_update_users(api_client,load_user_data):

    'Getting Data from Json File'
    user_data = load_user_data

    'Updating the data into the database'
    response = api_client.put_request(f"users/{1}",user_data)
    print(response.json())
    assert response.status_code == 200
    assert len(response.json()) != 0



def test_delete_users(api_client):

    'Deleting Users Data'
    response = api_client.delete_request("users/1")
    assert response.status_code == 200