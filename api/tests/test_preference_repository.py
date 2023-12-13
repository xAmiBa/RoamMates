from lib.Preference import Preference
from lib.Preference_repository import PreferenceRepository

def test_get_all_requests(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = PreferenceRepository(db_connection)
    assert repository.all() == [
        Preference(1, 1, "[18,24]", "Male", "Europe", "Summer", "Beach"),
        Preference(2, 2, "[18,24]", "Female", "Asia", "Winter", "Sport/fitness")
    ]