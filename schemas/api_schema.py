from typing import List
from pydantic import BaseModel


class Endpoint(BaseModel):
    path: str

    method: str

    request: List[str]

    response: List[str]


class APISchema(BaseModel):
    endpoints: List[Endpoint]