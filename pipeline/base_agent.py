import json

from pipeline.gemini_client import generate


class BaseAgent:

    def __init__(self, stage_name):

        self.stage_name = stage_name

    def execute(self, prompt):

        print(f"\n========== {self.stage_name} ==========\n")

        response = generate(prompt)

        response = (
            response.replace("```json", "")
            .replace("```", "")
            .strip()
        )

        try:

            return json.loads(response)

        except json.JSONDecodeError:

            print(response)

            raise Exception(
                f"{self.stage_name} produced invalid JSON."
            )