import json
from pipeline.gemini_client import generate


def extract_intent(user_prompt):
    prompt = f"""
You are the Intent Extraction stage of an AI Software Compiler.

Your ONLY job is to extract the user's intent.

Return ONLY valid JSON.

Output format:

{{
  "application_name": "",
  "application_type": "",
  "modules": [],
  "roles": [],
  "features": [],
  "assumptions": []
}}

User Request:
{user_prompt}
"""

    print("\n===== INTENT PROMPT =====")
    print(prompt)

    response = generate(prompt)

    print("\n===== INTENT RESPONSE =====")
    print(response)

    response = (
        response.replace("```json", "")
        .replace("```", "")
        .strip()
    )

    try:
        return json.loads(response)

    except json.JSONDecodeError:
        print("\n❌ Invalid JSON from Intent Agent:")
        print(response)
        raise