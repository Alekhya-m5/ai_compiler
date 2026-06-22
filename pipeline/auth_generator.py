import json

from pipeline.base_agent import BaseAgent

agent = BaseAgent("Auth Generator")


def generate_auth_schema(architecture):

    prompt = f"""
You are the Authentication Generator.

Generate ONLY authentication rules.

Return JSON.

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