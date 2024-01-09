from lib.Request_repository import RequestRepository
from lib.Request import Request
from lib.Profile import Profile
from lib.User import User

"""
Test if all requests retrieved
Only first and last due to size of database
"""


def test_get_all_requests(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = RequestRepository(db_connection)
    assert repository.all()[0] == Request(id=1, status=None, request_from=1, request_to=2)
    assert repository.all()[-1] == Request(id=53, status=True, request_from=9, request_to=6)


"""
Test if all requests retrieved with status True
"""


def test_get_all_null_requests(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = RequestRepository(db_connection)
    assert repository.all_true() == [
        Request(id=2, status=True, request_from=2, request_to=1), 
        Request(id=5, status=True, request_from=2, request_to=4), 
        Request(id=7, status=True, request_from=16, request_to=1), 
        Request(id=10, status=True, request_from=9, request_to=5), 
        Request(id=12, status=True, request_from=14, request_to=17), 
        Request(id=15, status=True, request_from=20, request_to=2), 
        Request(id=18, status=True, request_from=4, request_to=6), 
        Request(id=21, status=True, request_from=8, request_to=19), 
        Request(id=23, status=True, request_from=17, request_to=20), 
        Request(id=27, status=True, request_from=1, request_to=4), 
        Request(id=29, status=True, request_from=8, request_to=19), 
        Request(id=33, status=True, request_from=5, request_to=2), 
        Request(id=36, status=True, request_from=3, request_to=7), 
        Request(id=38, status=True, request_from=12, request_to=8), 
        Request(id=42, status=True, request_from=1, request_to=18), 
        Request(id=45, status=True, request_from=8, request_to=3), 
        Request(id=47, status=True, request_from=13, request_to=4), 
        Request(id=51, status=True, request_from=11, request_to=5), 
        Request(id=53, status=True, request_from=9, request_to=6)
        ] 


"""
Test if all requests retrieved with status null 
"""


def test_get_all_true_requests(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = RequestRepository(db_connection)
    assert repository.all_null() == [
        Request(id=1, status=None, request_from=1, request_to=2), 
        Request(id=3, status=None, request_from=7, request_to=18), 
        Request(id=6, status=None, request_from=10, request_to=3), 
        Request(id=9, status=None, request_from=20, request_to=12), 
        Request(id=13, status=None, request_from=3, request_to=7), 
        Request(id=16, status=None, request_from=12, request_to=10), 
        Request(id=19, status=None, request_from=18, request_to=11), 
        Request(id=22, status=None, request_from=1, request_to=16), 
        Request(id=25, status=None, request_from=2, request_to=14), 
        Request(id=28, status=None, request_from=10, request_to=6), 
        Request(id=31, status=None, request_from=17, request_to=9), 
        Request(id=34, status=None, request_from=20, request_to=1), 
        Request(id=37, status=None, request_from=14, request_to=10), 
        Request(id=40, status=None, request_from=9, request_to=11), 
        Request(id=43, status=None, request_from=6, request_to=14), 
        Request(id=46, status=None, request_from=17, request_to=9), 
        Request(id=49, status=None, request_from=7, request_to=19), 
        Request(id=52, status=None, request_from=18, request_to=1)
        ]


def test_get_requesting_users_for_user_with_one_pending_request(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = RequestRepository(db_connection)
    result = repository.get_requesting_users_for_user(2, "IS NULL")
    assert result == [
        Profile(user_id=1, user=User(id=1, username='amina', password=None, email='amina@gmail.com'), picture='https://www.echoclinics.nhs.uk/wp-content/uploads/female-placeholder.jpg', name='Amina', age='25', gender='female', bio='Passionate about exploring new cultures and trying local cuisines. Always seeking the next adventure to add to my travel diary. On a mission to visit every continent and experience the diversity our world has to offer.')
        ]


def test_get_requesting_users_for_user_with_zero_pending_request(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = RequestRepository(db_connection)
    result = repository.get_requesting_users_for_user(1, "IS NULL")
    assert result == [
        Profile(user_id=20, user=User(id=20, username='nomad_life', password=None, email='nomad_life@example.com'), picture='https://www.treasury.gov.ph/wp-content/uploads/2022/01/male-placeholder-image.jpeg', name='Andrew', age='25', gender='male', bio='Wanderer at heart, always seeking the next destination to fuel my curiosity. From city lights to natural wonders, Im on a perpetual quest for exploration and discovery.'),
        Profile(user_id=18, user=User(id=18, username='jetsetter22', password=None, email='jetsetter22@example.com'), picture='https://www.treasury.gov.ph/wp-content/uploads/2022/01/male-placeholder-image.jpeg', name='Dave', age='29', gender='male', bio='Enthusiastic traveler seeking the thrill of new adventures. From mountains to beaches, Im ready to explore it all. Lets create unforgettable memories together!')
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
