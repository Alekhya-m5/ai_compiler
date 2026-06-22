from pipeline.intent import extract_intent
from pipeline.architecture import generate_architecture

prompt = """
Build a CRM with login,
contacts,
dashboard,
role-based access,
premium plan with payments.
"""

intent = extract_intent(prompt)

architecture = generate_architecture(intent)

print(architecture)