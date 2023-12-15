import json
from playwright.sync_api import Page


"""
Check if server returns "OK" response 
when request to /users/add correct
""" 
def test_user_signup_success(page: Page, test_web_address):
    page.goto(f'http://{test_web_address}/users/add')

    # Define the JavaScript code with placeholders for dynamic values
    js_code = """
        async ({ url, data }) => {
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            });
            return await response.json();
        }
    """

    # Define the data to be sent in the request
    request_data = {
        "url": f'http://{test_web_address}/users/add',
        "data": {
            "username": "test_user",
            "password": "test_password",
            "email": "test@example.com",
        }
    }

    # Perform actions on the page, such as making a POST request
    response = page.evaluate(js_code, request_data)
    print("Response from server:", response)
    
    # Check for the expected response
    assert response.get('message') in ["OK!"]



"""
Check if server returns "OK" response 
when request to /users/authentication correct
""" 
def test_user_login_success(page: Page, test_web_address):
    page.goto(f'http://{test_web_address}/users/add')

    # Define the JavaScript code with placeholders for dynamic values
    js_code = """
        async ({ url, data }) => {
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            });
            return await response.json();
        }
    """

    # Define the data to be sent in the request
    request_data = {
        "url": f'http://{test_web_address}/users/add',
        "data": {
            "email": "amina@gmail.com",
            "password": "amina1",
        }
    }

    # Perform actions on the page, such as making a POST request
    response = page.evaluate(js_code, request_data)
    print("Response from server:", response)
    
    # Check for the expected response
    assert response.get('message') in ["OK!"]
