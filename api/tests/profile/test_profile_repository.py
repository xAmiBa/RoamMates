from lib.Profile_repository import ProfileRepository
from lib.Profile import Profile
from lib.User import User

"""
Test if all profiles retrieved
only first and last dues to size of db
"""


def test_get_all_users(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = ProfileRepository(db_connection)
    assert repository.all()[0] == Profile(user_id=1, user=User(id=1, username='amina', password=None, email='amina@gmail.com'), picture='https://www.echoclinics.nhs.uk/wp-content/uploads/female-placeholder.jpg', name='Amina', age='25', gender='female', bio='Passionate about exploring new cultures and trying local cuisines. Always seeking the next adventure to add to my travel diary. On a mission to visit every continent and experience the diversity our world has to offer.')
    assert repository.all()[-1] == Profile(user_id=50, user=User(id=50, username='wanderlust_dreaming', password=None, email='wanderlust_dreaming@example.com'), picture='https://www.treasury.gov.ph/wp-content/uploads/2022/01/male-placeholder-image.jpeg', name='Henry', age='33', gender='other', bio='A global nomad with a heart full of wanderlust. Join me in navigating through diverse cultures, embracing the beauty of our planet, and creating a legacy of global adventures.')


def test_get_profile_by_user_id(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = ProfileRepository(db_connection)
    assert repository.find_by_user_id(2) == Profile(
        2,
        User(2, "daniel", None, "daniel@gmail.com"),
        "https://www.treasury.gov.ph/wp-content/uploads/2022/01/male-placeholder-image.jpeg",
        "Daniel",
        "30",
        "male",
        "Adventure enthusiast with a love for nature and outdoor activities. Constantly looking for hidden gems off the beaten path. I believe that every journey is an opportunity to learn and grow.",
    )

def test_profile_updated_with_new_values(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = ProfileRepository(db_connection)
    new_profile = Profile(
        2,
        User(2, "daniel", None, "daniel@gmail.com"),
        "https://www.treasury.gov.ph/wp-content/uploads/2022/01/male-placeholder-image.jpeg",
        "Daniel",
        "24",
        "Female",
        "Test bio Daniel",
    )
    repository.update_profile(new_profile)
    assert repository.find_by_user_id(2) == Profile(
        2,
        User(2, "daniel", None, "daniel@gmail.com"),
        "https://www.treasury.gov.ph/wp-content/uploads/2022/01/male-placeholder-image.jpeg",
        "Daniel",
        "24",
        "Female",
        "Test bio Daniel",
    )

def test_profile_updated_with_new_values(db_connection):
    db_connection.seed("seeds/roammates_seed.sql")
    repository = ProfileRepository(db_connection)
    new_profile = Profile(
        2,
        User(2, "daniel", None, "daniel@gmail.com"),
        "https://www.treasury.gov.ph/wp-content/uploads/2022/01/male-placeholder-image.jpeg",
        "Daniel",
        "24",
        "Female",
        "Test bio Daniel",
    )

    repository.update_profile(new_profile)
    assert repository.find_by_user_id(2) == Profile(
        2,
        User(2, "daniel", None, "daniel@gmail.com"),
        "https://www.treasury.gov.ph/wp-content/uploads/2022/01/male-placeholder-image.jpeg",
        "Daniel",
        "24",
        "Female",
        "Test bio Daniel",
    )