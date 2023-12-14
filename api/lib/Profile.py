from dataclasses import dataclass

"""
Model represents profiles table containing profiles assigned to each user
"""

@dataclass
class Profile:
    id: int
    user_id: int   #foreign key referring to users table
    picture: str
    name: str
    age: str
    gender: str
    bio: str 
