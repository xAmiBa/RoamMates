from lib.Profile_repository import ProfileRepository
from lib.Profile import Profile

"""
Test if all profiles retrieved
"""


def test_get_all_users(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = ProfileRepository(db_connection)
    assert repository.all() == [
        Profile(
            1,
            1,
            "https://www.echoclinics.nhs.uk/wp-content/uploads/female-placeholder.jpg",
            "Amina",
            "28",
            "Female",
            "Test bio Amina",
        ),
        Profile(
            2,
            2,
            "https://www.treasury.gov.ph/wp-content/uploads/2022/01/male-placeholder-image.jpeg",
            "Daniel",
            "24",
            "Male",
            "Test bio Daniel",
        ),
    ]


def test_get_profile_by_user_id(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = ProfileRepository(db_connection)
    assert repository.find_by_user_id(2) == Profile(
        2,
        2,
        "https://www.treasury.gov.ph/wp-content/uploads/2022/01/male-placeholder-image.jpeg",
        "Daniel",
        "24",
        "Male",
        "Test bio Daniel",
    )
