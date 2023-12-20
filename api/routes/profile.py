from flask import request, jsonify, session
from token_config import token_checker, token_generator

from lib.database_connection import get_flask_database_connection
from lib.Profile_repository import ProfileRepository


def apply_profile_routes(app):
    """Profile Router."""

    @app.route("/profiles/data", methods=["GET"])
    def users_profiles_data():
        """
        Gets all users profiles data.
        Route: /profiles/data
        Request:  GET
        """

        connection = get_flask_database_connection(app)
        profile_repo = ProfileRepository(connection)
        users_list = profile_repo.all()

        token = request.form.get("token")
        user_id = session.get("user_id")

        if token_checker(token, user_id):
            token = token_generator(user_id)
            response = jsonify({"message": "OK!", "token": token, "users": users_list})
            response.status_code = 200

        else:
            response = jsonify({"message": "Invalid credentials"})
            response.status_code = 401

        return response
