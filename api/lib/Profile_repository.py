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

# TODO: Finish query to add new profile with user object
    def add(self, user_object):
        query = f"""
        INSERT INTO profiles (
        u
        )"""