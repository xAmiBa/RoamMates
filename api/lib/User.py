from dataclasses import dataclass

"""
Model represents users table containing user informations
"""
@dataclass
class User:
    id: int
    username: str
    password: str
    email: str
        
