from typing import List
from pydantic import BaseModel


class IntentSchema(BaseModel):
    application_name: str
    application_type: str

    modules: List[str]

    roles: List[str]

    features: List[str]

    assumptions: List[str]