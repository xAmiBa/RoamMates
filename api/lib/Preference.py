

class Preference():

    def __init__(self,id, user_id, age_slot, gender, continent, season, category):
        self.id = id
        self.user_id = user_id
        self.age_slot = age_slot
        self.gender = gender
        self.continent = continent 
        self.season = season
        self.category = category

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    