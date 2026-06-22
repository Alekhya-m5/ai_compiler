from pipeline.intent import extract_intent

prompt = """
Build a CRM with login,
contacts,
dashboard,
role-based access,
premium plan with payments.
"""

intent = extract_intent(prompt)

print(intent)