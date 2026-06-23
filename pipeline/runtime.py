import json
import os


def generate_runtime(result):

    os.makedirs("generated", exist_ok=True)

    with open("generated/ui.json", "w") as f:
        json.dump(result["ui"], f, indent=4)

    with open("generated/api.json", "w") as f:
        json.dump(result["api"], f, indent=4)

    with open("generated/db.json", "w") as f:
        json.dump(result["database"], f, indent=4)

    with open("generated/auth.json", "w") as f:
        json.dump(result["auth"], f, indent=4)

    return {
        "generated_files": [
            "generated/ui.json",
            "generated/api.json",
            "generated/db.json",
            "generated/auth.json"
        ]
    }