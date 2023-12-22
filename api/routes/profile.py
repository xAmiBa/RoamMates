from flask import request, jsonify, session
from token_config import token_checker, token_generator

from lib.database_connection import get_flask_database_connection
from lib.Profile_repository import ProfileRepository
from lib.User_repository import UserRepository
from lib.Preference_repository import PreferenceRepository
from lib.Request_repository import RequestRepository


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

        token = request.headers["Authorization"][7:]
        user_id = session.get("user_id")

        if token_checker(token, user_id):
            token = token_generator(user_id)
            response = jsonify({"message": "OK!", "token": token, "users": users_list})
            response.status_code = 200

        else:
            response = jsonify({"message": "Invalid credentials"})
            response.status_code = 401

        return response

    @app.route("/profiles/<user_id>", methods=["GET"])
    def user_profile(user_id):
        """
        Route: /profiles/user_id
        Request: GET
        Gets User details togheter with preferences and request.
        """

        connection = get_flask_database_connection(app)
        profiles_repo = UserRepository(connection)
        preferences_repo = PreferenceRepository(connection)
        requests_repo = RequestRepository(connection)

        token = request.headers["Authorization"][7:]
        session_user_id = session.get("user_id")

        profile_data = profiles_repo.find_by_id(user_id)
        preferences_data = preferences_repo.find_by_user_id(user_id)

        # request status between for session user and accessed profile
        request_data = requests_repo.get_request_status(session_user_id, user_id)

        if token_checker(token, session_user_id):
            token = token_generator(session_user_id)
            response = jsonify(
                {
                    "message": "OK!",
                    "token": token,
                    "profile": profile_data,
                    "preferences": preferences_data,
                    "user_request_status": request_data,
                }
            )
            response.status_code = 200

        else:
            response = jsonify({"message": "Invalid credentials"})
            response.status_code = 401

        return response
