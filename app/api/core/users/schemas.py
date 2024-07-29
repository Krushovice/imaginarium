from typing import Annotated

from pydantic import EmailStr, BaseModel

from annotated_types import MaxLen, MinLen


class UserCreate(BaseModel):
    email: EmailStr
    username: Annotated[str, MinLen(5), MaxLen(20)]
