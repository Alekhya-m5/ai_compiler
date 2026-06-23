from pipeline.intent import extract_intent
from pipeline.architecture import generate_architecture
from pipeline.ui_generator import generate_ui_schema
from pipeline.api_generator import generate_api_schema
from pipeline.db_generator import generate_db_schema
from pipeline.auth_generator import generate_auth_schema
from pipeline.validator import validate_compilation
from pipeline.repair import repair_output
from pipeline.runtime import generate_runtime


def compile_application(user_prompt):

    result = {}

    print("Stage 1 : Intent Extraction")
    intent = extract_intent(user_prompt)
    result["intent"] = intent

    print("Stage 2 : Architecture")
    architecture = generate_architecture(intent)
    result["architecture"] = architecture

    print("Stage 3 : UI")
    result["ui"] = generate_ui_schema(architecture)

    print("Stage 4 : API")
    result["api"] = generate_api_schema(architecture)

    print("Stage 5 : Database")
    result["database"] = generate_db_schema(architecture)

    print("Stage 6 : Authentication")
    result["auth"] = generate_auth_schema(architecture)

    print("Stage 7 : Validation")
    errors = validate_compilation(result)

    result["validation_errors"] = errors

    repair_result = repair_output(
    errors,
    result
    )

    result["repair"] = repair_result

    runtime_result = generate_runtime(result)

    result["runtime"] = runtime_result

    return result