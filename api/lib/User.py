class User:

    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    def __eq__(self, other):
        return self.__dict__ == other.__dict__