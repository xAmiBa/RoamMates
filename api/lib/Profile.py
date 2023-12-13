

class Profile():

    def __init__(self, id, user_id, picture, name, age, gender, bio):
        self.id = id
        self.user_id = user_id
        self.picture = picture
        self.name = name
        self.age = age
        self.gender = gender
        self.bio = bio 


    def __eq__(self, other):
        return self.__dict__ == other.__dict__
