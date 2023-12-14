from token_config import token_generator, token_checker
import jwt
import pytest

"""
Test if decoded token contains correct user id
"""

def test_generate_token():
    token = token_generator(1)

    assert jwt.decode(token, "secret", algorithms=["HS256"]) == {"user_id": 1}


"""
Test if token_checker confirms validity
"""
def test_token_checker_true():
    assert token_checker(token_generator(5), 5) == True

"""
Test if token_checker confirms invalidity
"""
def test_token_checker_false():
    assert token_checker(token_generator(1), 5) == False


"""
Test if token_checker rasises error
when token is empty
"""
def test_token_checker_exception():
    with pytest.raises(ValueError) as e:
        token_checker(" ", 5)
    assert str(e.value) == "Token not valid: Not enough segments"
    with pytest.raises(ValueError) as e:
        token_checker(None, 5)
    assert str(e.value) == "Token not valid: Invalid token type. Token must be a <class 'bytes'>"
