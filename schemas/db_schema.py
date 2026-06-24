from typing import List, Any
from pydantic import BaseModel


class Table(BaseModel):
    name: str

    columns: List[Any]


class DBSchema(BaseModel):
    tables: List[Table]