from lib.Preference import Preference
class PreferenceRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM preferences')
        preferences = [Preference(row["id"], row["user_id"], row["age_slot"], row["gender"], row["continent"], row["season"], row["category"]) for row in rows]
        return preferences