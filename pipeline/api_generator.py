import json

from pipeline.base_agent import BaseAgent
from schemas.api_schema import APISchema
from config import USE_MOCK_GENERATORS

agent = BaseAgent("API Generator")


def generate_api_schema(architecture):
    if USE_MOCK_GENERATORS:

        return {
            "endpoints": [
                {
                    "path": "/dashboard",
                    "method": "GET"
                }
            ]
        }
    else:

            prompt = f"""
            You are the API Generator of an AI Software Compiler.

            Generate REST API endpoints.

            Return ONLY valid JSON.

            Rules:
            - No markdown
            - No explanation

        Format:

        {{
        "endpoints":[
            {{
                "path":"",
                "method":"",
                "request":[],
                "response":[]
            }}
        ]
        }}

Architecture:

{json.dumps(architecture, indent=2)}
"""

    data = agent.execute(prompt)

    validated = APISchema(**data)

    return validated.model_dump()