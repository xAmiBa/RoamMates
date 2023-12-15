from flask import Flask, request
import json
import psycopg
import os
import secrets
from lib.User import User
from lib.User_repository import UserRepository
from lib.database_connection import get_flask_database_connection
from token_config import token_checker, token_generator

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
        response = app.response_class(response=json.dumps({"message": "OK!"}), status=200)
  
    else:
        print("User already exists:")
        response = app.response_class(response=json.dumps({"message": "Credentials error"}), status=401)

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
        response = app.response_class(response=json.dumps({
            "message": "OK!",
            "token": token
            }),status=200)
        return response
    return app.response_class(response=json.dumps({"message": "Invalid credentials"}), status=401)


"""
Route:
Request:
[]
"""



if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

