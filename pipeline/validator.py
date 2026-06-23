def validate_compilation(result):

    errors = []

    # ==========================
    # Check Required Sections
    # ==========================

    required_sections = [
        "intent",
        "architecture",
        "ui",
        "api",
        "database",
        "auth"
    ]

    for section in required_sections:

        if section not in result:

            errors.append(
                f"Missing section: {section}"
            )

    if errors:
        return errors

    # ==========================
    # Architecture ↔ Database
    # ==========================

    db_tables = [
        table["name"]
        for table in result["database"]["tables"]
    ]

    for entity in result["architecture"]["entities"]:

        if entity not in db_tables:

            errors.append(
                f"Missing database table for entity: {entity}"
            )

    # ==========================
    # Intent Roles ↔ Auth Roles
    # ==========================

    auth_roles = [
        role["name"]
        for role in result["auth"]["roles"]
    ]

    for role in result["intent"]["roles"]:

        if role not in auth_roles:

            errors.append(
                f"Missing auth role: {role}"
            )

    # ==========================
    # UI Routes ↔ API Endpoints
    # ==========================

    api_paths = [
        endpoint["path"]
        for endpoint in result["api"]["endpoints"]
    ]

    for page in result["ui"]["pages"]:

        route = page["route"]

        if route not in api_paths:

            errors.append(
                f"No API endpoint found for route: {route}"
            )

    # ==========================
    # API Exists
    # ==========================

    if len(result["api"]["endpoints"]) == 0:

        errors.append(
            "No API endpoints generated"
        )

    # ==========================
    # DB Exists
    # ==========================

    if len(result["database"]["tables"]) == 0:

        errors.append(
            "No database tables generated"
        )

    # ==========================
    # Auth Exists
    # ==========================

    if len(result["auth"]["roles"]) == 0:

        errors.append(
            "No authentication roles generated"
        )

    return errors