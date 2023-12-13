from lib.Preference import Preference

def test_request_initiation():
    preference = Preference(1, 1, "[18,24]", "Male", "Europe", "Summer", "Beach")
    assert preference.id == 1
    assert preference.user_id == 1
    assert preference.age_slot == "[18,24]"
    assert preference.gender == "Male"
    assert preference.continent == "Europe"
    assert preference.season == "Summer"
    assert preference.category == "Beach"

def test_eql():
    preference1 = Preference(1, 1, "[18,24]", "Male", "Europe", "Summer", "Beach")
    preference2 = Preference(1, 1, "[18,24]", "Male", "Europe", "Summer", "Beach")
    assert preference1 == preference2