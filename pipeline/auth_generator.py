import json

from pipeline.base_agent import BaseAgent
from schemas.auth_schema import AuthSchema
from config import USE_MOCK_GENERATORS


agent = BaseAgent("Authentication Generator")


def generate_auth_schema(architecture):
    if USE_MOCK_GENERATORS:

        return {
            "roles": [
                {
                    "name": "Admin",
                    "permissions": [
                        "read",
                        "write"
                    ]
                }
            ]
        }

    else:
        prompt = f"""
    You are the Authentication Generator.

    Generate authentication and authorization rules.

    Return ONLY valid JSON.

    Rules:
    - No markdown
    - No explanation

    Format:

    {{
        "roles":[
            {{
                "name":"",
                "permissions":[]
            }}
        ]
    }}

Architecture:

{json.dumps(architecture, indent=2)}
"""

    data = agent.execute(prompt)

    validated = AuthSchema(**data)

    return validated.model_dump()