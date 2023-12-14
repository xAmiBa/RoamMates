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