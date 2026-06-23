from pipeline.compiler import compile_application
import json

prompt = """
Build a CRM with login,
dashboard,
contacts,
payments,
role-based access.
"""

result = compile_application(prompt)

# print(json.dumps(result, indent=4))