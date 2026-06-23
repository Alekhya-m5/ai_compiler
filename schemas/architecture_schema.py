from typing import List
from pydantic import BaseModel


class Relationship(BaseModel):
    from_entity: str
    to_entity: str
    relation_type: str


class ArchitectureSchema(BaseModel):
    entities: List[str]

    pages: List[str]

    flows: List[str]

    relationships: List[Relationship]