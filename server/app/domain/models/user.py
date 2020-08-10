"""ユーザクラス.

ユーザは以下の情報を持ちます。

* ユーザID
* ユーザ名

"""

from .user_id import UserId
from .user_name import UserName


class User:
    """ユーザクラス.

    Args:
        user_id (UserId): ユーザID
        user_name (UserName): ユーザ名

    Attributes:
        user_id (UserId): ユーザID
        user_name (UserName): ユーザ名
    """

    def __init__(self, user_id: UserId, user_name: UserName):
        """初期化処理.

        Args:
            user_id (UserId): ユーザID
            user_name (UserName): ユーザ名
        """
        self.user_id = user_id
        self.user_name = user_name
