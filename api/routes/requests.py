from flask import request, jsonify, session
from token_config import token_checker, token_generator

from lib.database_connection import get_flask_database_connection
from lib.Request_repository import RequestRepository


def apply_request_routes(app):
    """Requests Router."""

    @app.route("/requests/null", methods=["GET"])
    def requests_pending_user_list():
        """Gets list of users that sent request
            to currently logged user.

        Returns:
            _type_: Json (message and list of users.)
        """
        connection = get_flask_database_connection(app)
        token = request.form.get("token")
        user_id = session.get("user_id")

        if token_checker(token, user_id):
            request_repo = RequestRepository(connection)
            users = request_repo.get_requesting_users_for_user(user_id)
            token = token_generator(user_id)
            response = jsonify({"message": "OK!", "token": token, "users": users})
            response.status_code = 200

        else:
            response = jsonify({"message": "Invalid credentials"})
            response.status_code = 401

        return response
