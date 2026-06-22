from typing import List
from pydantic import BaseModel


class IntentSchema(BaseModel):
    application_name: str
    application_type: str
    modules: List[str]
    roles: List[str]
    features: List[str]
    assumptions: List[str]


class Relationship(BaseModel):
    from_entity: str
    to_entity: str
    relation_type: str


class ArchitectureSchema(BaseModel):
    entities: List[str]
    pages: List[str]
    flows: List[str]
    relationships: List[Relationship]