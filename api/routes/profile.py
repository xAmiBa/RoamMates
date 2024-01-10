from flask import request, jsonify, session
from token_config import token_checker, token_generator
import os
from datetime import datetime
from werkzeug.utils import secure_filename

from lib.database_connection import get_flask_database_connection
from lib.Profile_repository import ProfileRepository
from lib.User_repository import UserRepository
from lib.Preference_repository import PreferenceRepository
from lib.Request_repository import RequestRepository


def apply_profile_routes(app):
    """Profile Router."""

    @app.route("/profiles/data", methods=["GET", "PUT"])
    def users_profiles_data():
        if request.method == "GET":
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

        elif request.method == "PUT":
            """
            Updated profile data.
            Route: /profiles/data
            Request:  PUT

            This method updates user profile in database. When Image is present,
            the unique name is created (date, time and filename) and added to database.
            Image is stored locally in api/static/UPLOADS directory
            """
            connection = get_flask_database_connection(app)
            profile_repo = ProfileRepository(connection)

            user_id = session.get("user_id")
            token = request.headers["Authorization"][7:]
            picture = request.files["picture"]
   
            if not token_checker(token, user_id):
                response = jsonify({"message": "Invalid credentials"})
                response.status_code = 401
                return response

            user_profile = profile_repo.find_by_user_id(user_id)

            if picture:
                filename = secure_filename(str(datetime.now()) + picture.filename )
                picture.save(os.path.join(app.config["UPLOADS"], filename))
                user_profile.picture = "/static/UPLOADS/" + filename

            for key in ["name", "age", "gender", "bio"]:
                    new_value = request.form.get(key)
                    setattr(user_profile, key, new_value)
            
            profile_repo.update_profile(user_profile)
            token = token_generator(user_id)
            response = jsonify(
                {
                    "message": "OK!",
                    "token": token,
                    "id": user_id,
                }
            )
            response.status_code = 200
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



        """
        Draft code with cofiguration of amazon bucket for image storage.        
        Upload image to bucket.
        """
        # import boto3
        # from dotenv import load_dotenv
        # load_dotenv()
        # s3 = boto3.client(
        #     "s3",
        #     aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
        #     aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
        # )

        # # get image access URL from bucket
        # if picture:
        #     # Specify the bucket name and object name
        #     bucket_name = os.environ.get("BUCKET_NAME")
        #     object_name = picture.filename + str(datetime.now()) + ".png"

        #     # Upload the file to S3
        #     s3.upload_fileobj(picture, bucket_name, object_name)

        #     # Get the S3 URL of the uploaded file
        #     photo_url = f"https://{bucket_name}.s3.amazonaws.com/{object_name}"
        #     print(photo_url)

        #     # Process the received data as needed
        #     result = {
        #         "photo_url": photo_url,
        #     }

        #       # Return a Flask Response object
        #     response = jsonify(
        #         {
        #             "message": "OK!",
        #             }
        #     )
        #     response.status_code = 200
        #     return response

    # Handle the case when there is no picture

