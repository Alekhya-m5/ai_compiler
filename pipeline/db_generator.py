import json

from pipeline.base_agent import BaseAgent
from schemas.db_schema import DBSchema
from config import USE_MOCK_GENERATORS

agent = BaseAgent("Database Generator")


def generate_db_schema(architecture):
    if USE_MOCK_GENERATORS:

        return {
            "tables": [
                {
                    "name": "User",
                    "columns": [
                        "id",
                        "email",
                        "password"
                    ]
                }
            ]
        }
    
    else:
        prompt = f"""
    are the Database Schema Generator.

    rate ONLY the database schema.

    rn ONLY valid JSON.

    Rules:
    - No markdown
    - No explanation

    Format:

    {{
        "tables":[
            {{
                "name":"",
                "columns":[]
            }}
        ]
    }}

Architecture:

{json.dumps(architecture, indent=2)}
"""

    
    data = agent.execute(prompt)

    validated = DBSchema(**data)

    return validated.model_dump()