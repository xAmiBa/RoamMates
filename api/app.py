from flask import Flask, request
import json
import psycopg
import os
import secrets
from lib.User import User
from lib.User_repository import UserRepository
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
def create_app(config = None):

    app = Flask(__name__)

    if config:
        app.config.from_object(config)

    app.secret_key = secrets.token_hex(32)
    return app

app = create_app()

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

    # Check if user email is unique
    if users.find_by_email(email) is None:
        users.add(User(None, username, password, email))
        response = app.response_class(response=json.dumps({"message": "OK!"}), status=200)
        print(response)
  
    else:
        response = app.response_class(response=json.dumps({"message": "Credentials error"}), status=401)
        

    return response
"""
Route: /users/authentication
Request: GET
[verifies that username matches password and creates a token]
"""
@app.route("/users/authentication")
def user_login():
    pass


"""
Route:
Request:
[]
"""



if __name__ == '__main__':
    config = os.environ.get('APP_CONFIG', 'config.DevelopmentConfig')
    app = create_app(config)
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

