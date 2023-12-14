from token_generator import token_generator
import jwt

"""
Test if decoded token contains correct user id
"""

def test_generate_token():
    token = token_generator(1)

    assert jwt.decode(token, "secret", algorithms=["HS256"]) == {"user_id": 1}