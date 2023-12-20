from dataclasses import dataclass
from .User import User

"""
Model represents profiles table containing profiles assigned to each user
"""


@dataclass
class Profile:
    user_id: int  # foreign key referring to users table
    user: User
    picture: str
    name: str
    age: str
    gender: str
    bio: str
