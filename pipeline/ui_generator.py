import json

from pipeline.base_agent import BaseAgent
from schemas.ui_schema import UISchema
from config import USE_MOCK_GENERATORS

agent = BaseAgent("UI Generator")


def generate_ui_schema(architecture):
    
    if USE_MOCK_GENERATORS:

        return {
            "pages": [
                {
                    "name": "Dashboard",
                    "route": "/dashboard",
                    "components": [
                        "Navbar",
                        "Table"
                    ]
                }
            ]
        }

    else:
        prompt = f"""
        You are the UI Generator.

        Generate ONLY the UI schema.

        Return JSON.

    Format:

    {{
        "pages":[
            {{
                "name":"",
                "route":"",
                "components":[]
            }}
        ]
    }}

Architecture:

{json.dumps(architecture, indent=2)}
"""
    data = agent.execute(prompt)
    validated = UISchema(**data)
    return validated.model_dump() 