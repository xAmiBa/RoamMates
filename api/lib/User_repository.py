from lib.User import User

class UserRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from USERS')
        users = [User(row["id"], row["username"], row["password"], row["email"]) for row in rows]
        return users