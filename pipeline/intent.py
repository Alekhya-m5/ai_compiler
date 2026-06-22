import json

from pipeline.base_agent import BaseAgent

agent = BaseAgent("Intent Extraction")


def extract_intent(user_prompt):

    prompt = f"""
You are the Intent Extraction stage of an AI Software Compiler.

Your ONLY responsibility is to understand the user's requirements.

Return ONLY valid JSON.

Output format:

{{
    "application_name":"",
    "application_type":"",
    "modules":[],
    "roles":[],
    "features":[],
    "assumptions":[]
}}

User Request:

{user_prompt}
"""

    return agent.execute(prompt)