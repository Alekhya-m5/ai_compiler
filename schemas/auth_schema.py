from typing import List, Any
from pydantic import BaseModel


class Role(BaseModel):
    name: str

    permissions: List[Any]


class AuthSchema(BaseModel):
    roles: List[Role]