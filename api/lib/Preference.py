from dataclasses import dataclass

"""
Model represents preferences table containing preferences set for each user
"""

@dataclass
class Preference:
   id: int
   user_id: int   #foreign key referring to users table
   age_slot: str
   gender: str
   continent: str 
   season: str
   category: str