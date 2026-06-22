import json

from pipeline.base_agent import BaseAgent

agent = BaseAgent("UI Generator")


def generate_ui_schema(architecture):

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

    return agent.execute(prompt)