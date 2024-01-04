from flask import request, jsonify, session
from token_config import token_generator

from lib.database_connection import get_flask_database_connection
from lib.Profile_repository import ProfileRepository
from lib.User import User
from lib.User_repository import UserRepository


def apply_auth_routes(app):
    """Auth Router."""

    @app.route("/users/authentication", methods=["POST"])
    def user_login():
        """
        Route: /users/authentication
        Request: POST
        Verifies that username matches password and creates a token.
        """

        connection = get_flask_database_connection(app)
        users_repo = UserRepository(connection)

        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        if users_repo.check_login_details(email, password) is True:
            user = users_repo.find_by_email(email)
            # adds user_id to session to verify tokes later
            session["user_id"] = user.id
            token = token_generator(user.id)
            response = jsonify({"message": "OK!", "token": token})
            response.status_code = 200
        else:
            response = jsonify({"message": "Invalid credentials"})
            response.status_code = 401

        return response
