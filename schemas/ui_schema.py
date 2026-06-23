from typing import List
from pydantic import BaseModel


class Page(BaseModel):
    name: str

    route: str

    components: List[str]


class UISchema(BaseModel):
    pages: List[Page]