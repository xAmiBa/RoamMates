from flask import request, jsonify, session
from token_config import token_generator

from lib.database_connection import get_flask_database_connection
from lib.Profile_repository import ProfileRepository
from lib.User import User
from lib.User_repository import UserRepository


def apply_auth_routes(app):
    """Auth Router."""

    @app.route("/users/add", methods=["POST"])
    def user_signup():
        """
        Route: /users/add
        Request: POST
        [Signup, adds user to Users table]
        """
        connection = get_flask_database_connection(app)
        user_repo = UserRepository(connection)

        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')

        # Check if user email is unique
        if user_repo.find_by_email(email):
            print("User already exists:")
            response = jsonify({"message": "Credentials error"})
            response.status_code = 401

        else:
            user_repo.add(User(None, username, password, email))
            response = jsonify({"message": "OK!"})
            response.status_code = 200        

        return response


    """
    Route: /users/authentication
    Request: POST
    [verifies that username matches password and creates a token]
    """


    @app.route("/users/authentication", methods=["POST"])
    def user_login():
        connection = get_flask_database_connection(app)
        users_repo = UserRepository(connection)

        email = request.form.get("email")
        password = request.form.get("password")

        if users_repo.check_login_details(email, password) is True:
            user = users_repo.find_by_email(email)
            # adds user_id to session to verify tokes later
            session['user_id'] = user.id
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

