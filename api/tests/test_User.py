from lib.User import User


"""
Testing if User class is initailised with all variables
"""
def test_initialisation():
    test_user = User(1, "username", "password", "email")
    assert test_user.id == 1
    assert test_user.username == "username"
    assert test_user.password == "password"
    assert test_user.email == "email"


"""
Testing if two identical objects are equal
"""
def test_equality():
    test_user1 = User(1, "username", "password", "email")
    test_user2 = User(1, "username", "password", "email")
    assert test_user1 == test_user2

