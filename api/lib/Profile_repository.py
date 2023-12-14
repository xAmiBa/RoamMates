from lib.Profile import Profile

class ProfileRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from PROFILES')
        users = [Profile(row["id"], row["user_id"], row["picture"], row["name"], row["age"], row["gender"], row["bio"]) for row in rows]
        return users