import json
from pipeline.gemini_client import generate


class BaseAgent:
    """
    Base class for every AI agent in the compiler pipeline.
    Handles:
    - LLM call
    - JSON parsing
    - Error handling
    """

    def __init__(self, stage_name):
        self.stage_name = stage_name

    def execute(self, prompt: str):

        response = generate(prompt)

        response = (
            response.replace("```json", "")
            .replace("```", "")
            .strip()
        )

        try:
            return json.loads(response)

        except json.JSONDecodeError:
            raise Exception(
                f"{self.stage_name} returned invalid JSON.\n\nResponse:\n{response}"
            )