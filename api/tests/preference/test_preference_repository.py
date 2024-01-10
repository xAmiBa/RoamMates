from lib.Preference import Preference
from lib.Preference_repository import PreferenceRepository


def test_get_all_preferences(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = PreferenceRepository(db_connection)
    assert repository.all()[0] == Preference(id=1, user_id=1, age_slot='[18, 24]', gender='other', continent='North America', season='winter', category='resort')

def test_get_preferences_by_user_id(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = PreferenceRepository(db_connection)
    assert repository.find_by_user_id(1) == Preference(
        1, 1, "[18, 24]", "other", "North America", "winter", "resort"
    )


def test_setup_preferences_for_new_user(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = PreferenceRepository(db_connection)
    new_preferences = Preference(
        None, 50, "[25, 30]", "female", "Africa", "winter", "beach"
    )
    repository.insert_preferences(new_preferences)
    assert repository.find_by_user_id(50) == Preference(
        50, 50, "[25, 30]", "female", "Africa", "winter", "beach"
    )


def test_setup_preferences_for_existing_user(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = PreferenceRepository(db_connection)
    new_preferences = Preference(
        1, 1, "[25, 30]", "female", "Africa", "winter", "beach"
    )
    repository.update_preferences(new_preferences)
    assert repository.find_by_user_id(1) == new_preferences
