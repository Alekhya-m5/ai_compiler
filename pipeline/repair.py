from pipeline.api_generator import generate_api_schema
from pipeline.db_generator import generate_db_schema
from pipeline.auth_generator import generate_auth_schema


def repair_output(errors, result):

    repaired = []

    for error in errors:

        if "database" in error.lower():

            result["database"] = generate_db_schema(
                result["architecture"]
            )

            repaired.append("database")

        elif "auth" in error.lower():

            result["auth"] = generate_auth_schema(
                result["architecture"]
            )

            repaired.append("auth")

        elif "api" in error.lower():

            result["api"] = generate_api_schema(
                result["architecture"]
            )

            repaired.append("api")

    return {
        "repaired": repaired,
        "count": len(repaired)
    }