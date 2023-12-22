from flask import Flask
import os
import secrets

from routes.profile import apply_profile_routes
from routes.auth import apply_auth_routes
from routes.requests import apply_request_routes


# Create a new Flask app
app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

apply_profile_routes(app)
apply_auth_routes(app)
apply_request_routes(app)


if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))
