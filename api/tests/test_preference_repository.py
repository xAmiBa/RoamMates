from lib.Preference import Preference
from lib.Preference_repository import PreferenceRepository

def test_get_all_preferences(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = PreferenceRepository(db_connection)
    assert repository.all() == [
        Preference(1, 1, '[18, 24]', 'Other', 'North America', 'Winter', 'Resort'),
        Preference(2, 2, '[25, 30]', 'Female', 'Europe', 'Spring', 'Beach')
    ]