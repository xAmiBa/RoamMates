from flask import Flask
import psycopg2
import os
import secrets

# Create a new Flask app
app = Flask(__name__)
app.secret_key = secrets.token_hex(32)




if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))