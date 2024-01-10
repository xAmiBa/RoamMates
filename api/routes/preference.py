from flask import request, jsonify, session
from token_config import token_checker, token_generator

from lib.database_connection import get_flask_database_connection
from lib.Preference_repository import PreferenceRepository
from lib.Preference import Preference


def apply_preference_routes(app):
    """
    Profile Router.
    Method finds preferences by user id.
    If preferences exist: the update_preferences method is executed
    If preferences does not exist: the insert_preferences method is executed
    """

    @app.route("/preferences/data", methods=["PUT"])
    def setup_preferences_data():
        """
        Posts preferences data
        Route: /preferences/data
        Request: PUT
        """
        
        connection = get_flask_database_connection(app)
        data = request.get_json()
        token = request.headers["Authorization"][7:]
        user_id = session.get("user_id")

        print("TOKEN BE:", token)
        print("user_id BE:", user_id)
        print("TOKEN CHECKER STATUS:", token_checker(token, user_id))

        if not token_checker(token, user_id):
            response = jsonify({"message": "Invalid credentials"})
            response.status_code = 401
            return response

        preferences_repo = PreferenceRepository(connection)
        preferences = preferences_repo.find_by_user_id(user_id)

        if preferences:
            for key in ["age_slot", "gender", "continent", "season", "category"]:
                setattr(preferences, key, data[key])
            preferences_repo.update_preferences(preferences)

        else:
            new_preferences = Preference(
                None,
                user_id,
                data.get("age_slot"),
                data.get("gender"),
                data.get("continent"),
                data.get("season"),
                data.get("category"),
            )
            preferences_repo.insert_preferences(new_preferences)

        token = token_generator(user_id)
        response = jsonify({"message": "OK!", "token": token, "user_id": user_id})
        response.status_code = 200
        return response