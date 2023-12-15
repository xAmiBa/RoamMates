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
        User(2, "daniel", "daniel1", "daniel@gmail.com"),
    ]


"""
Test add new user
"""


def test_post_new_user(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = UserRepository(db_connection)
    repository.add(User(None, "testname", "testpassword", "testemail"))
    assert repository.all() == [
        User(1, "amina", "amina1", "amina@gmail.com"),
        User(2, "daniel", "daniel1", "daniel@gmail.com"),
        User(3, "testname", "testpassword", "testemail"),
    ]


"""
Test if user by id found
"""


def test_find_user_by_id(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = UserRepository(db_connection)
    assert repository.find_by_id(1) == User(1, "amina", "amina1", "amina@gmail.com")


"""
Test if user by email found
"""


def test_find_user_by_email_none(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = UserRepository(db_connection)
    assert repository.find_by_email("amina@gmail.com") == User(
        1, "amina", "amina1", "amina@gmail.com"
    )


"""
Test if user by email not found
"""


def test_find_user_by_email_none(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = UserRepository(db_connection)
    assert repository.find_by_email("nonexistingemail@gmail.com") == []


"""
Test if user email and password is in database for login attempt
"""


def test_check_login_details(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = UserRepository(db_connection)
    assert repository.check_login_details("amina@gmail.com", "amina1") == True


def test_check_login_details_password_incorrect(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = UserRepository(db_connection)
    assert repository.check_login_details("amina@gmail.com", "amina5") == False


def test_check_login_details_email_incorrect(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = UserRepository(db_connection)
    assert repository.check_login_details("amina@gmail.co.uk", "amina1") == False


def test_check_login_details_password(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = UserRepository(db_connection)
    assert repository.check_login_details("amina@gmail.co.uk", "daniel1") == False
