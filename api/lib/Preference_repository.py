from lib.Preference import Preference
class PreferenceRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM preferences')
        preferences = [Preference(row["id"], row["user_id"], row["age_slot"], row["gender"], row["continent"], row["season"], row["category"]) for row in rows]
        return preferences
    
    def find_by_user_id(self, user_id):
        rows = self._connection.execute('SELECT * from PREFERENCES WHERE user_id = %s',
                                        [user_id])
        row = rows[0]
        return Preference(row["id"], row["user_id"], row["age_slot"], row["gender"], row["continent"], row["season"], row["category"])