from lib.Profile import Profile


def test_profile_initiation():
    profile = Profile(1, 1, None, "Amina", "25", "Female", "Test bio 1")
    assert profile.id == 1
    assert profile.user_id == 1
    assert profile.name == "Amina"
    assert profile.age == "25"
    assert profile.gender == "Female"
    assert profile.bio == "Test bio 1"


def test_eql():
    profile1 = Profile(1, 1, None, "Amina", "25", "Female", "Test bio 1")
    profile2 = Profile(1, 1, None, "Amina", "25", "Female", "Test bio 1")
    assert profile1 == profile2
