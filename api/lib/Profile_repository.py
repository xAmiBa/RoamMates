from lib.Profile import Profile
from lib.User import User


class ProfileRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        query = """SELECT
          users.id, users.username, users.email, profiles.* 
          from PROFILES JOIN users ON user_id = users.id"""
        rows = self._connection.execute(query)
        users = [
            Profile(
                row["user_id"],
                User(row["id"], row["username"], None, row["email"]),
                row["picture"],
                row["name"],
                row["age"],
                row["gender"],
                row["bio"],
            )
            for row in rows
        ]
        return users

    def find_by_user_id(self, user_id):
        query = """SELECT
          users.id, users.username, users.email, profiles.* 
          from PROFILES JOIN users ON user_id = users.id WHERE user_id = %s"""
        rows = self._connection.execute(query, [user_id])
        row = rows[0]
        return Profile(
            row["user_id"],
            User(row["id"], row["username"], None, row["email"]),
            row["picture"],
            row["name"],
            row["age"],
            row["gender"],
            row["bio"],
        )

    def update_profile(self, profile_object):
        query = """
        UPDATE profiles
        SET picture = %s, name = %s, age = %s, gender = %s, bio = %s
        WHERE user_id = %s;
        """
        self._connection.execute(query, [
            profile_object.picture,
            profile_object.name,
            profile_object.age,
            profile_object.gender,
            profile_object.bio,
            profile_object.user_id
            ])