from pipeline.intent import extract_intent
from pipeline.architecture import generate_architecture
from pipeline.ui_generator import generate_ui_schema

prompt = """
Build a CRM with login,
contacts,
dashboard,
role-based access,
premium plan with payments.
"""

intent = extract_intent(prompt)

architecture = generate_architecture(intent)

ui = generate_ui_schema(architecture)

print(ui)