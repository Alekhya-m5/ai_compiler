from typing import List, Any
from pydantic import BaseModel


class Endpoint(BaseModel):
    path: str

    method: str

    request: List[Any]

    response: List[Any]


class APISchema(BaseModel):
    endpoints: List[Endpoint]