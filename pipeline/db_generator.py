import json

from pipeline.base_agent import BaseAgent
from schemas.db_schema import DBSchema

agent = BaseAgent("Database Generator")


def generate_db_schema(architecture):

    prompt = f"""
You are the Database Schema Generator.

Generate ONLY the database schema.

Return ONLY valid JSON.

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