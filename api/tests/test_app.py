import json
from playwright.sync_api import Page
from lib.User_repository import UserRepository

"""
Route: /users/add
Request: POST
Check if server returns "OK" response 
when request correct
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


# """
# Waiting for a coach to help me with different type of test later
# """
# def test_user_signup(web_client, db_connection, test_web_address):
#     # Assuming your route is /users/add
#     response = web_client.post(f"http://{test_web_address}/users/add", data={
#         "username": "test_user",
#         "password": "test_password",
#         "email": "test@example.com",
#     })
    
#     assert response.status_codewq == 200  # Assuming successful registration
#     print("RESPONSE:", response)
#     assert response.json["message"] == "OK!"

#     # Now you can check if the user was added to the database
#     connection = db_connection  # You might need to adjust this
#     users = UserRepository(db_connection)
#     user = users.find_by_email('test@example.com')
    

"""
Route: /users/add
Request: POST
Check if server returns "OK" response 
when request correct
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