import json
from lib.User_repository import UserRepository
from lib.User import User
import os
import pytest

# Set the APP_CONFIG environment variable to use the testing configuration
os.environ['APP_CONFIG'] = 'config.TestingConfig'
from app import app

@pytest.fixture
def client():
    # Create a test client using the application with the testing configuration
    with app.test_client() as client:
        yield client

def test_user_signup_success(client, db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    users = UserRepository(db_connection)

    print("Existing Users:", users.all())

    # Make a POST request with valid credentials
    response = client.post('/users/add', data=dict(
        username='test_user',
        password='test_password',
        email='test@example.com'
    ))
    print(response.get_data(as_text=True))
    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # # Check if the response message is as expected
    # expected_message = {"message": "OK!"}
    # assert response.json == expected_message

#     # Check if the user was added to the database
#     user = users.find_by_email('test@example.com')
#     assert user is not None
#     assert user.username == 'test_user'

# def test_user_signup_credentials_error():
#     client = app.test_client()
#     connection = get_flask_database_connection(app)
#     users = UserRepository(connection)

#     # Make a POST request with existing email (should return 401)
#     response = client.post('/users/add', data=dict(
#         username='existing_user',
#         password='existing_password',
#         email='test@example.com'
#     ))

#     # Check if the response status code is 401 (Unauthorized)
#     assert response.status_code == 401

#     # Check if the response message is as expected
#     expected_message = {"message": "Credentials error"}
#     assert response.json == expected_message
