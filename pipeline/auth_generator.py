import json

from pipeline.base_agent import BaseAgent

agent = BaseAgent("Authentication Generator")


def generate_auth_schema(architecture):

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

    return agent.execute(prompt)