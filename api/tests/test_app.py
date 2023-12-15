import json
from playwright.sync_api import Page, expect


"""
Check if server returns "OK" response 
when request to /users/add correct
""" 
def test_user_signup_success(web_client, test_web_address):
    response = web_client.post(f"http://{test_web_address}/users/add", data={
        "email": "test@example.com",
        "password": "test_password",
        "username": "test_username",
    })

    assert response.status_code == 200
    assert response.get_json().get('message') == "OK!"

"""
Check if server returns 401 response 
when request to /users/add incorrect - duplicate email
""" 
def test_user_signup_fail(web_client, test_web_address):
    response = web_client.post(f"http://{test_web_address}/users/add", data={
        "email": "amina@gmail.com",
        "password": "test_password",
        "username": "test_username",
    })

    assert response.status_code == 401
    assert response.get_json().get('message') == "Credentials error"

"""
Check if server returns "OK" response 
when request to /users/authentication correct
""" 
def test_user_signup_fail(web_client, test_web_address):
    response = web_client.post(f"http://{test_web_address}/users/authentication", data={
        "email": "amina@gmail.com",
        "password": "amina1"
    })

    assert response.status_code == 200
    assert response.get_json().get('message') == "OK!"


"""
Check if server returns "Invalid credentials" response 
when request to /users/authentication incorrect
""" 
def test_user_signup_fail(web_client, test_web_address):
    response = web_client.post(f"http://{test_web_address}/users/authentication", data={
        "email": "amina@gmail.com",
        "password": "wrong_password"
    })

    assert response.status_code == 401
    assert response.get_json().get('message') == "Invalid credentials"






