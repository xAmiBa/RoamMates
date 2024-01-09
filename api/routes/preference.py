from flask import request, jsonify, session
from token_config import token_checker, token_generator

from lib.database_connection import get_flask_database_connection
from lib.Preference_repository import PreferenceRepository
from lib.Preference import Preference


def apply_preference_routes(app):
    """Profile Router."""

    @app.route("/preferences/data", methods=["PUT"])
    def setup_preferences_data():
        """
        Posts preferences data
        Route: /preferences/data
        Request: PUT
        """

        connection = get_flask_database_connection(app)
        # get data
        data = request.get_json()

        token = request.headers["Authorization"][7:]
        user_id = session.get("user_id")

        if not token_checker(token, user_id):
            response = jsonify({"message": "Invalid credentials"})
            response.status_code = 401
            return response

        # get old preferences by user_id
        preferences_repo = PreferenceRepository(connection)
        preferences = preferences_repo.find_by_user_id(user_id)
        # compare both data and skip None values
        if preferences:
            for key in ["age_slot", "gender", "continent", "season", "category"]:
                setattr(preferences, key, data[key])

            preferences_repo.update_preferences(preferences)

        else:
            # create new preferences object
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
        response = jsonify({"message": "OK!", "token": token})
        response.status_code = 200

        return response
