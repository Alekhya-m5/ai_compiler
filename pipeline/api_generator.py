import json

from pipeline.base_agent import BaseAgent

agent = BaseAgent("API Generator")


def generate_api_schema(architecture):

    prompt = f"""
You are the API Generator.

Generate REST API endpoints.

Return ONLY valid JSON.

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

    return agent.execute(prompt)