from flask import Flask, request, jsonify
import json
import psycopg
import os
import secrets
from lib.User import User
from lib.User_repository import UserRepository
from lib.database_connection import get_flask_database_connection
from token_config import token_checker, token_generator
from lib.User_repository import UserRepository
from lib.User import User
from lib.Profile_repository import ProfileRepository
from lib.Profile import Profile

# Create a new Flask app
app = Flask(__name__)
app.secret_key = secrets.token_hex(32)


"""
Route: /users/add
Request: POST
[Signup, adds user to Users table]
"""
@app.route("/users/add", methods=["POST"])
def user_signup():
    connection = get_flask_database_connection(app)
    users = UserRepository(connection)

    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')
    print("EMAIL PASSED:", email)

    # Check if user email is unique
    if users.find_by_email(email) == []:
        users.add(User(None, username, password, email))
        response = jsonify({"message": "OK!"})
        response.status_code = 200

    else:
        print("User already exists:")
        response = jsonify({"message": "Credentials error"})
        response.status_code = 401

    return response
"""
Route: /users/authentication
Request: POST
[verifies that username matches password and creates a token]
"""
@app.route("/users/authentication", methods=["POST"])
def user_login():
    connection = get_flask_database_connection(app)
    users = UserRepository(connection)

    email = request.form.get('email')
    password = request.form.get('password')

    if users.check_login_details(email, password) is True:
        user = users.find_by_email(email)
        token = token_generator(user.id)
        response = jsonify({
            "message": "OK!",
            "token": token
            })
        response.status_code = 200
    else:
        response = jsonify({"message": "Invalid credentials"})
        response.status_code = 401
    
    return response


"""
Route: /profiles/data
Request:  GET
[gets all users profiles data]
"""
def users_profiles_data():
    connection = get_flask_database_connection(app)
    users = UserRepository(connection)
    profiles = ProfileRepository(connection)
    email = request.form.get('token')


"""
Route: /requests/null
Request: GET
[gets users profiles data - only profiles who sent request to user]
"""
"""
Route: /requests/true
Request: GET
[gets users profiles data - only matched users]
"""



if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

