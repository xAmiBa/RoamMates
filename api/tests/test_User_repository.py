from lib.User_repository import UserRepository
from lib.User import User

"""
Test if all users retrieved
"""
def test_get_all_users(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = UserRepository(db_connection)
    assert repository.all() == [
        User(1, "amina", "amina1", "amina@gmail.com"),
        User(2, "daniel", "daniel1", "daniel@gmail.com")
    ]