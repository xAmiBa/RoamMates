from lib.Request import Request

"""
Testing if Request class is initailised with all variables
"""


def test_initialisation():
    test_request = Request(1, None, 1, 2)
    assert test_request.id == 1
    assert test_request.status == None
    assert test_request.request_from == 1
    assert test_request.request_to == 2


"""
Testing if two identical objects are equal
"""


def test_equality():
    test_request1 = Request(1, None, 1, 2)
    test_request2 = Request(1, None, 1, 2)
    assert test_request1 == test_request2
