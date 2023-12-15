from dataclasses import dataclass

"""
Model represents requests table containing match requests from users
"""


@dataclass
class Request:
    id: int
    status: bool
    request_from: int  # user id of user who sent request
    request_to: int  # user id of user who recieved request
