from pipeline.intent import extract_intent
from pipeline.architecture import generate_architecture
from pipeline.ui_generator import generate_ui_schema
from pipeline.api_generator import generate_api_schema
from pipeline.db_generator import generate_db_schema
from pipeline.auth_generator import generate_auth_schema


def compile_application(user_prompt):

    result = {}

    print("\n==============================")
    print("Stage 1 : Intent Extraction")
    print("==============================")

    intent = extract_intent(user_prompt)
    result["intent"] = intent

    print("\n==============================")
    print("Stage 2 : Architecture")
    print("==============================")

    architecture = generate_architecture(intent)
    result["architecture"] = architecture

    print("\n==============================")
    print("Stage 3 : UI Schema")
    print("==============================")

    ui = generate_ui_schema(architecture)
    result["ui"] = ui

    print("\n==============================")
    print("Stage 4 : API Schema")
    print("==============================")

    api = generate_api_schema(architecture)
    result["api"] = api

    print("\n==============================")
    print("Stage 5 : Database Schema")
    print("==============================")

    database = generate_db_schema(architecture)
    result["database"] = database

    print("\n==============================")
    print("Stage 6 : Authentication Schema")
    print("==============================")

    auth = generate_auth_schema(architecture)
    result["auth"] = auth

    return result