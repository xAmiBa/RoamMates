from lib.Request_repository import RequestRepository
from lib.Request import Request
from lib.Profile import Profile
from lib.User import User

"""
Test if all requests retrieved
"""


def test_get_all_requests(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = RequestRepository(db_connection)
    assert repository.all() == [Request(1, None, 1, 2), Request(2, True, 2, 1)]


"""
Test if all requests retrieved with status True
"""


def test_get_all_null_requests(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = RequestRepository(db_connection)
    assert repository.all_true() == [Request(2, True, 2, 1)]


"""
Test if all requests retrieved with status null 
"""


def test_get_all_true_requests(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = RequestRepository(db_connection)
    assert repository.all_null() == [Request(1, None, 1, 2)]


def test_get_requesting_users_for_user_with_one_pending_request(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = RequestRepository(db_connection)
    result = repository.get_requesting_users_for_user(2)
    assert result == [
        Profile(
            1,
            User(1, "amina", None, "amina@gmail.com"),
            "https://www.echoclinics.nhs.uk/wp-content/uploads/female-placeholder.jpg",
            "Amina",
            "28",
            "Female",
            "Test bio Amina",
        )
    ]


def test_get_requesting_users_for_user_with_zero_pending_request(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = RequestRepository(db_connection)
    result = repository.get_requesting_users_for_user(1)
    assert result == []


"""
Test if correct status returned
"""


def test_get_request_status(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = RequestRepository(db_connection)
    assert repository.get_request_status(1, 2) == None
    assert repository.get_request_status(2, 1) == True
    assert repository.get_request_status(4, 1) == ""
