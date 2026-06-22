import json

from pipeline.base_agent import BaseAgent
from schemas.app_schema import ArchitectureSchema

agent = BaseAgent("Architecture Generator")


def generate_architecture(intent):

    prompt = f"""
You are the Architecture Design stage of an AI Software Compiler.

Your ONLY responsibility is to design the software architecture.

Return ONLY valid JSON.

Rules:
- No markdown.
- No explanation.
- entities must be a list of strings.
- pages must be a list of strings.
- flows must be a list of strings.
- relationships must contain:
  - from_entity
  - to_entity
  - relation_type

Return exactly this format:

{{
    "entities": [],
    "pages": [],
    "flows": [],
    "relationships": [
        {{
            "from_entity": "",
            "to_entity": "",
            "relation_type": ""
        }}
    ]
}}

Intent:

{json.dumps(intent, indent=2)}
"""

    data = agent.execute(prompt)

    validated = ArchitectureSchema(**data)

    return validated.model_dump()