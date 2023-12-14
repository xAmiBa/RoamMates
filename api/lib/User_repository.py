from lib.User import User

class UserRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from USERS')
        users = [User(row["id"], row["username"], row["password"], row["email"]) for row in rows]
        return users
    
    def add(self, user_object):
        self._connection.execute('INSERT INTO users (username, password, email) VALUES (%s, %s, %s);',
                                 [user_object.username, user_object.password, user_object.email])
        
    def find_by_id(self, user_id):
        rows = self._connection.execute('SELECT * from USERS WHERE id = %s',
                                        [user_id])
        row = rows[0]
        return User(row["id"], row["username"], row["password"], row["email"])
    
    def find_by_email(self, user_id):
        rows = self._connection.execute('SELECT * from USERS WHERE email = %s',
                                        [user_id])

        if rows == []:
            return []
        else: 
            row = rows[0]
            return User(row["id"], row["username"], row["password"], row["email"])
    