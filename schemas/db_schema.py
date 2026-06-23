from typing import List
from pydantic import BaseModel


class Table(BaseModel):
    name: str

    columns: List[str]


class DBSchema(BaseModel):
    tables: List[Table]