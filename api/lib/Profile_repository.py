from lib.Profile import Profile


class ProfileRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * from PROFILES")
        users = [
            Profile(
                row["id"],
                row["user_id"],
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
        rows = self._connection.execute(
            "SELECT * from PROFILES WHERE user_id = %s", [user_id]
        )
        row = rows[0]
        return Profile(
            row["id"],
            row["user_id"],
            row["picture"],
            row["name"],
            row["age"],
            row["gender"],
            row["bio"],
        )
