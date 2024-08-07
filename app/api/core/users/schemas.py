from typing import Annotated

from pydantic import BaseModel, ConfigDict

from annotated_types import MaxLen, MinLen


class UserBase(BaseModel):
    username: Annotated[str, MinLen(3), MaxLen(15)]
    email: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class UserUpdate(UserCreate):
    pass


class UserUpdatePartial(UserCreate):
    username: Annotated[str, MinLen(3), MaxLen(15)] | None = None
    email: str | None = None
