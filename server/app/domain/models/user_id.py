"""ユーザIDの値オブジェクトクラス.

ユーザIDは以下の形式です.

    * 形式: UUID
    * フォーマット: 不明

"""

import dataclasses
import uuid


@dataclasses.dataclass(frozen=True)
class UserId:
    """ユーザIDクラス.

    Args:
        value (UUID): 値

    Attributes:
        value (UUID): 値
    """

    value: uuid.UUID

    def __eq__(self, other: object) -> bool:
        """値が同じかどうか比較します.

        Args:
            other (object): 比較対象

        Returns:
            [bool]: 同じ値かどうか
        """
        return isinstance(other, UserId) and self.value == other.value
