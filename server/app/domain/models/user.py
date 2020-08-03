from .user_id import UserId
from .user_name import UserName


class User:
    def __init__(self, user_id: UserId, user_name: UserName):
        self.user_id = user_id
        self.user_name = user_name
