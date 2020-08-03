import dataclasses
import uuid


@dataclasses.dataclass(frozen=True)
class UserId:
    value: uuid.UUID
