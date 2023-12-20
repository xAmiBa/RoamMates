from flask import Flask, request, jsonify, session
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
from lib.Request_repository import RequestRepository
from lib.Preference_repository import PreferenceRepository
from routes.profile import apply_profile_routes
from routes.auth import apply_auth_routes
# Create a new Flask app
app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

apply_profile_routes(app)
apply_auth_routes(app)





"""
Route: /requests/null
Request: GET
[gets users profiles data - only profiles who sent request to user]
"""
@app.route("/requests/null", methods=["GET"])
def requests_null():
    connection = get_flask_database_connection(app)
    requests_repo = RequestRepository(connection)
    requests_list = requests_repo.all_null()

    token = request.form.get('token')
    user_id = session.get('user_id')
    
    if token_checker(token, user_id):
        token = token_generator(user_id)
        response = jsonify({
            "message": "OK!",
            "token": token,
            "requests": requests_list
            })
        response.status_code = 200

    else:
        response = jsonify({"message": "Invalid credentials"})
        response.status_code = 401

    return response

"""
Route: /requests/true
Request: GET
[gets users profiles data - only matched users]
"""
@app.route("/requests/true", methods=["GET"])
def requests_true():
    connection = get_flask_database_connection(app)
    requests_repo = RequestRepository(connection)
    requests_list = requests_repo.all_true()

    token = request.form.get('token')
    user_id = session.get('user_id')
    
    if token_checker(token, user_id):
        token = token_generator(user_id)
        response = jsonify({
            "message": "OK!",
            "token": token,
            "requests": requests_list,
            })
        response.status_code = 200

    else:
        response = jsonify({"message": "Invalid credentials"})
        response.status_code = 401

    return response


"""
Route: /profiles/user_id
Request: GET
[gets profile data by user id]
"""
@app.route("/profiles/user_id", methods=["GET"])
def user_profile():
    connection = get_flask_database_connection(app)
    profiles_repo = UserRepository(connection)
    preferences_repo = PreferenceRepository(connection)
    requests_repo = RequestRepository(connection)

    token = request.form.get('token')
    user_id_from_req = request.form.get('id')
    session_user_id = session.get('user_id')

    profile_data = profiles_repo.find_by_id(user_id_from_req)
    preferences_data = preferences_repo.find_by_user_id(user_id_from_req)

     # request status between for session user and accessed profile
    request_data = requests_repo.get_request_status(session_user_id, user_id_from_req)
    
    if token_checker(token, session_user_id):
        token = token_generator(session_user_id)
        response = jsonify({
            "message": "OK!",
            "token": token,
            "profile": profile_data,
            "preferences": preferences_data,
            "user_request_status": request_data
            })
        response.status_code = 200

    else:
        response = jsonify({"message": "Invalid credentials"})
        response.status_code = 401

    return response

if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))
