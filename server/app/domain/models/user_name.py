"""ユーザ名の値オブジェクトクラス.

ユーザ名は以下のルールに従う必要があります。

    * 3文字以上
    * 16文字以下

"""

import dataclasses


@dataclasses.dataclass(frozen=True)
class UserName:
    """UserNameクラス.

    ユーザ名の値オブジェクトです.

    Args:
        value (str): 値

    Attributes:
        value (str): 値
    """

    value: str

    def __post_init__(self):
        """PostInit処理.

        Raises:
            Exception: 入力値エラー
        """
        length = len(self.value)
        if length == 0:
            raise Exception("空文字です。")

        if length < 3:
            raise Exception("3文字以上にしてください。")

        if length > 16:
            raise Exception("16文字以下にしてください。")

    def __eq__(self, other: object) -> bool:
        """値が同じかどうか比較します.

        Args:
            other (object): 比較対象

        Returns:
            [bool]: 同じ値かどうか
        """
        return isinstance(other, UserName) and (self.value == other.value)
