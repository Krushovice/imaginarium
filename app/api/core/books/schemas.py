from typing import Annotated

from pydantic import BaseModel, ConfigDict

from annotated_types import MaxLen, MinLen


class BookBase(BaseModel):
    title: Annotated[str, MinLen(2), MaxLen(20)]
    autor: Annotated[str, MinLen(5), MaxLen(30)]
    genre: Annotated[str, MinLen(3), MaxLen(20)]


class BookCreate(BookBase):
    pass


class Book(BookBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
