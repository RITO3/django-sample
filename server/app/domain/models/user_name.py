import dataclasses


@dataclasses.dataclass(frozen=True)
class UserName:
    value: str

    """This is post init function.
    """

    def __post_init__(self):
        length = len(self.value)
        if length == 0:
            raise Exception("空文字です。")

        if length < 3:
            raise Exception("3文字以上にしてください。")

        if length > 16:
            raise Exception("16文字以下にしてください。")

    def __eq__(self, other):
        return isinstance(other, UserName) and (self.value == other.value)
