import jwt
from datetime import datetime, timedelta

# Function generating unique token containing user_id
def token_generator(user_id):

    token = jwt.encode(
        {"user_id": user_id},
        "secret",
        algorithm="HS256"
        )
    
    return token
