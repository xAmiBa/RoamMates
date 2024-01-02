from lib.Profile import Profile
from lib.User import User


def test_profile_initiation():
    test_user = User(1, "username", "password", "email")
    profile = Profile(1, test_user, None, "Amina", "25", "Female", "Test bio 1")
    assert profile.user_id == 1
    assert profile.name == "Amina"
    assert profile.age == "25"
    assert profile.gender == "Female"
    assert profile.bio == "Test bio 1"


def test_eql():
    test_user = User(1, "username", "password", "email")
    profile1 = Profile(1, test_user, "Amina", None, "25", "Female", "Test bio 1")
    profile2 = Profile(1, test_user, "Amina", None, "25", "Female", "Test bio 1")
    assert profile1 == profile2
