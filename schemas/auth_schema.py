from typing import List
from pydantic import BaseModel


class Role(BaseModel):
    name: str

    permissions: List[str]


class AuthSchema(BaseModel):
    roles: List[Role]