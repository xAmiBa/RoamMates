from lib.Request_repository import RequestRepository
from lib.Request import Request

"""
Test if all requests retrieved
"""
def test_get_all_requests(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = RequestRepository(db_connection)
    assert repository.all() == [
        Request(1, None, 1, 2),
        Request(2, True, 2, 1)
    ]


"""
Test if all requests retrieved with status True
"""
def test_get_all_null_requests(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = RequestRepository(db_connection)
    assert repository.all_true() == [
        Request(2, True, 2, 1)
    ]

"""
Test if all requests retrieved with status null 
"""
def test_get_all_true_requests(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = RequestRepository(db_connection)
    assert repository.all_null() == [
        Request(1, None, 1, 2)
    ]

"""
Test if correct status returned
"""
def test_get_request_status(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = RequestRepository(db_connection)
    assert repository.get_request_status(1, 2) == None
    assert repository.get_request_status(2, 1) == True
    assert repository.get_request_status(4, 1) == ""
