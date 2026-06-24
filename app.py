
import streamlit as st
import json
from pipeline.compiler import compile_application
import graphviz

# from pipeline.compiler import compile_application

st.set_page_config(
    page_title="AI Software Compiler",
    page_icon="🤖",
    layout="wide"
)

# ======================================
# SIDEBAR
# ======================================

with st.sidebar:

    st.title("🤖 AI Compiler")

    st.markdown("### Pipeline Status")

    intent_status = st.empty()
    arch_status = st.empty()
    ui_status = st.empty()
    api_status = st.empty()
    db_status = st.empty()
    auth_status = st.empty()
    val_status = st.empty()
    runtime_status = st.empty()

    intent_status.info("⏳ Intent Agent")
    arch_status.info("⏳ Architecture Agent")
    ui_status.info("⏳ UI Generator")
    api_status.info("⏳ API Generator")
    db_status.info("⏳ DB Generator")
    auth_status.info("⏳ Auth Generator")
    val_status.info("⏳ Validator")
    runtime_status.info("⏳ Runtime")

    st.info(
        "Natural Language ➜ Structured Application"
    )

# ======================================
# HEADER
# ======================================

st.title("🤖 AI Software Compiler")

st.markdown("""
Convert natural language requirements into:

✅ UI Schema  
✅ API Schema  
✅ Database Schema  
✅ Authentication Rules  
✅ Runtime Configuration
""")

# ======================================
# TOP METRICS
# ======================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Stages", "6")

with col2:
    st.metric("Validation", "Enabled")

with col3:
    st.metric("Repair Engine", "Enabled")

with col4:
    st.metric("Runtime", "Enabled")

st.markdown("---")

# ======================================
# PIPELINE
# ======================================

st.subheader("⚙ Compiler Pipeline")

st.markdown("""
Prompt ➜ Intent ➜ Architecture ➜ UI ➜ API ➜ Database ➜ Auth ➜ Validation ➜ Runtime
""")

st.markdown("---")

# ======================================
# INPUT
# ======================================

prompt = st.text_area(
    "Describe your application",
    height=180,
    placeholder="""
Build a CRM with login,
dashboard,
contacts,
payments,
role-based access.
Admins can view analytics.
"""
)

# ======================================
# BUTTON
# ======================================

if st.button(
    "🚀 Compile Application",
    use_container_width=True
):

    progress = st.progress(0)

    try:

        # Stage 1
        intent_status.info("🔄 Running Intent Agent")
        progress.progress(10)

        status = st.empty()

        status.info("Running AI Compiler...")

        result = compile_application(prompt)
        
        status.success("Compilation Complete")

        # Mark all stages completed
        intent_status.success("✅ Intent Agent")
        progress.progress(20)

        arch_status.success("✅ Architecture Agent")
        progress.progress(35)

        ui_status.success("✅ UI Generator")
        progress.progress(50)

        api_status.success("✅ API Generator")
        progress.progress(65)

        db_status.success("✅ DB Generator")
        progress.progress(75)

        auth_status.success("✅ Auth Generator")
        progress.progress(85)

        val_status.success("✅ Validator")
        progress.progress(95)

        runtime_status.success("✅ Runtime")
        progress.progress(100)

        st.success("Compilation Complete")

    except Exception as e:

        st.error(f"Compilation Failed: {e}")
        st.stop()

    # ======================================
    # SUMMARY
    # ======================================

    st.subheader("📊 Compilation Summary")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Entities",
            len(result["architecture"]["entities"])
        )

    with c2:
        st.metric(
            "Pages",
            len(result["architecture"]["pages"])
        )

    with c3:
        st.metric(
            "Endpoints",
            len(result["api"]["endpoints"])
        )

    with c4:
        st.metric(
            "Tables",
            len(result["database"]["tables"])
        )

    st.markdown("---")

    # ======================================
    # TABS
    # ======================================

    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs(
        [
            "Intent",
            "Architecture",
            "UI",
            "API",
            "Database",
            "Auth",
            "Validation",
            "Runtime",
            "Repair"
        ]
    )

    with tab1:
        st.json(result["intent"])

    with tab2:

        st.subheader("Architecture JSON")
        st.json(result["architecture"])

        st.subheader("Architecture Diagram")

        graph = graphviz.Digraph()

        entities = result["architecture"]["entities"]

        for entity in entities:
            graph.node(entity)

        if len(entities) > 1:
            for i in range(len(entities) - 1):
                graph.edge(
                    entities[i],
                    entities[i + 1]
                )

        st.graphviz_chart(graph)

    with tab3:
        st.json(result["ui"])

    with tab4:
        st.json(result["api"])

    with tab5:
        st.json(result["database"])

    with tab6:
        st.json(result["auth"])

    with tab7:

        if len(result["validation_errors"]) == 0:
            st.success("Validation Passed")
        else:
            st.error(result["validation_errors"])

    with tab8:

        st.json(result["runtime"])

        st.download_button(
            "Download Runtime Config",
            json.dumps(
                result["runtime"],
                indent=4
            ),
            file_name="runtime.json",
            key="runtime_download"
        )


    with tab9:

        repair = result["repair"]

        if repair["repaired"]:
            st.warning("System performed repairs")
        else:
            st.success("No repairs required")

        st.json(repair)

   
# ======================================
# FOOTER
# ======================================

st.markdown("---")

st.caption(
    "AI Software Compiler • Multi-Stage Generation • Validation • Repair • Runtime"
)

