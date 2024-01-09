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
