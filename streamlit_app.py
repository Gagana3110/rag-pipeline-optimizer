import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="RAG Pipeline Optimizer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

/* ---------------------------------------------------
MAIN APP
--------------------------------------------------- */

.stApp {
    background: linear-gradient(
        135deg,
        #020617 0%,
        #050B1E 40%,
        #08112E 100%
    );
    color: white;
}

/* Remove Streamlit Branding */

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* ---------------------------------------------------
GLOBAL TEXT
--------------------------------------------------- */

html, body, [class*="css"] {
    color: white;
    font-family: 'Inter', sans-serif;
}

/* ---------------------------------------------------
MAIN TITLE
--------------------------------------------------- */

.main-title {

    font-size: 62px;
    font-weight: 800;
    line-height: 1.1;

    background: linear-gradient(
        90deg,
        #38BDF8,
        #818CF8,
        #EC4899
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    margin-bottom: 10px;

    text-shadow:
        0 0 30px rgba(168,85,247,0.35);
}

/* ---------------------------------------------------
SUBTITLE
--------------------------------------------------- */

.subtitle {

    color: #E2E8F0;
    font-size: 22px;
    margin-bottom: 32px;
}

/* ---------------------------------------------------
SECTION TITLES
--------------------------------------------------- */

.section-title-pink {

    color: #FF4DDE;

    font-size: 42px;

    font-weight: 800;

    margin-top: 10px;
    margin-bottom: 8px;

    text-shadow:
        0 0 18px rgba(255,77,222,0.7);
}

.section-title-blue {

    color: #00E5FF;

    font-size: 42px;

    font-weight: 800;

    margin-top: 10px;
    margin-bottom: 8px;

    text-shadow:
        0 0 18px rgba(0,229,255,0.7);
}

/* ---------------------------------------------------
DESCRIPTION TEXT
--------------------------------------------------- */

.desc-text {

    color: #E2E8F0;

    font-size: 18px;

    margin-bottom: 12px;
}

/* ---------------------------------------------------
PIPELINE CARDS
--------------------------------------------------- */

.pipeline-card-blue {

    background: rgba(15, 23, 42, 0.95);

    border: 1px solid rgba(0,229,255,0.4);

    border-radius: 22px;

    padding: 24px;

    box-shadow:
        0 0 20px rgba(0,229,255,0.12);
}

.pipeline-card-pink {

    background: rgba(15, 23, 42, 0.95);

    border: 1px solid rgba(255,77,222,0.4);

    border-radius: 22px;

    padding: 24px;

    box-shadow:
        0 0 20px rgba(255,77,222,0.12);
}

/* ---------------------------------------------------
PIPELINE TITLES
--------------------------------------------------- */

.pipeline-title-blue {

    font-size: 30px;

    font-weight: 700;

    color: #38BDF8;

    margin-bottom: 18px;
}

.pipeline-title-pink {

    font-size: 30px;

    font-weight: 700;

    color: #FF4DDE;

    margin-bottom: 18px;
}

/* ---------------------------------------------------
ANSWER BOX
--------------------------------------------------- */

.answer-box {

    background: #0F172A;

    border-radius: 16px;

    padding: 18px;

    color: #E2E8F0;

    line-height: 1.7;

    margin-top: 12px;

    margin-bottom: 18px;

    border: 1px solid rgba(255,255,255,0.06);
}

/* ---------------------------------------------------
SIDEBAR
--------------------------------------------------- */

[data-testid="stSidebar"] {

    background:
        rgba(2, 6, 23, 0.96);

    border-right:
        1px solid rgba(255,255,255,0.08);
}

/* ---------------------------------------------------
SIDEBAR TITLE
--------------------------------------------------- */

.sidebar-title {

    font-size: 34px;

    font-weight: 800;

    color: white;
}

/* ---------------------------------------------------
SIDEBAR BOX
--------------------------------------------------- */

.sidebar-box {

    background:
        rgba(15,23,42,0.85);

    border-radius: 18px;

    padding: 16px;

    margin-bottom: 12px;

    color: #22C55E;

    font-size: 17px;

    border:
        1px solid rgba(255,255,255,0.06);
}

/* ---------------------------------------------------
BUTTONS
--------------------------------------------------- */

.stButton > button {

    background: linear-gradient(
        90deg,
        #2563EB,
        #9333EA,
        #EC4899
    );

    color: white;

    border: none;

    border-radius: 14px;

    padding: 14px 26px;

    font-size: 18px;

    font-weight: 700;

    transition: 0.3s;

    width: 100%;
}

.stButton > button:hover {

    transform: scale(1.02);

    box-shadow:
        0 0 20px rgba(236,72,153,0.4);
}

/* ---------------------------------------------------
TEXT INPUT
--------------------------------------------------- */

.stTextInput input {

    background-color:
        #0F172A !important;

    color: white !important;

    border-radius: 16px;

    border:
        2px solid #00E5FF;

    padding: 16px;

    box-shadow:
        0 0 18px rgba(0,229,255,0.18);
}

/* Placeholder */

input::placeholder {

    color: #94A3B8 !important;
}

/* ---------------------------------------------------
FILE UPLOADER
--------------------------------------------------- */

[data-testid="stFileUploader"] {

    background:
        rgba(15,23,42,0.75);

    border:
        2px solid #FF4DDE;

    border-radius: 18px;

    padding: 12px;

    box-shadow:
        0 0 18px rgba(255,77,222,0.15);
}

/* File uploader text */

[data-testid="stFileUploader"] small {

    color: #E2E8F0 !important;
}

/* ---------------------------------------------------
METRICS
--------------------------------------------------- */

[data-testid="metric-container"] {

    background: #111827;

    border-radius: 16px;

    padding: 12px;

    border:
        1px solid rgba(255,255,255,0.06);
}

/* ---------------------------------------------------
SCROLLBAR
--------------------------------------------------- */

::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-thumb {

    background: #9333EA;

    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">⚙️ System Overview</div>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown(
        '<div class="sidebar-box">✅ Uploads PDFs</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-box">✅ Creates embeddings</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-box">✅ Runs multiple RAG pipelines</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-box">✅ Evaluates responses</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-box">✅ Compares retrieval quality</div>',
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
        <div style="
            border-top: 1px solid rgba(255,255,255,0.08);
            margin-top: 10px;
            margin-bottom: 25px;
        "></div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="
            color: white;
            font-size: 38px;
            font-weight: 800;
            margin-bottom: 28px;
        ">
            📊 Pipelines
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="
            color: white;
            font-size: 26px;
            font-weight: 500;
            margin-bottom: 30px;
        ">
            🔷 Pipeline A → Top 3 Retrieval
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="
            color: white;
            font-size: 26px;
            font-weight: 500;
        ">
            🟣 Pipeline B → Top 5 Retrieval
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.markdown(
    '<div class="main-title">🤖 RAG Pipeline Optimizer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Compare Multiple RAG Pipelines with AI Evaluation Metrics</div>',
    unsafe_allow_html=True
)

# ---------------------------------------------------
# UPLOAD SECTION
# ---------------------------------------------------

st.markdown(
    '<div class="section-title-pink">📄 Upload Documents</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="desc-text">Upload your PDF document</div>',
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader(
    "",
    type=["pdf"],
    label_visibility="collapsed"
)

if uploaded_file is not None:

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file.getvalue(),
            "application/pdf"
        )
    }

    if st.button("🚀 Upload & Process"):

        with st.spinner("Processing document..."):

            response = requests.post(
                f"{BACKEND_URL}/upload",
                files=files
            )

            if response.status_code == 200:

                result = response.json()

                st.success(
                    "✅ Document uploaded successfully!"
                )

                col1, col2 = st.columns(2)

                with col1:

                    st.metric(
                        "Chunks Created",
                        result["chunks_created"]
                    )

                with col2:

                    st.metric(
                        "Status",
                        "Processed"
                    )

            else:

                st.error("❌ Upload failed")

# ---------------------------------------------------
# ASK QUESTION SECTION
# ---------------------------------------------------

st.markdown(
    '<div class="section-title-blue">❓ Ask Questions</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="desc-text">Ask something about the uploaded document</div>',
    unsafe_allow_html=True
)

query = st.text_input(
    "",
    placeholder="🔍 Ask something about the uploaded document...",
    label_visibility="collapsed"
)

if st.button("🧠 Run RAG Pipelines"):

    with st.spinner("Running pipelines..."):

        response = requests.post(
            f"{BACKEND_URL}/ask",
            params={"query": query}
        )

        if response.status_code == 200:

            result = response.json()

            pipeline_a = result["pipeline_a"]
            pipeline_b = result["pipeline_b"]

            st.markdown("---")

            st.markdown("# 📊 Pipeline Comparison")

            col1, col2 = st.columns(2)

            with col1:

                st.markdown(
                    '<div class="pipeline-card-blue">',
                    unsafe_allow_html=True
                )

                st.markdown(
                    '<div class="pipeline-title-blue">🔷 Pipeline A</div>',
                    unsafe_allow_html=True
                )

                st.markdown("### 💬 Answer")

                st.markdown(
                    f'<div class="answer-box">{pipeline_a["answer"]}</div>',
                    unsafe_allow_html=True
                )

                st.markdown("### 📈 Metrics")

                m1, m2 = st.columns(2)

                with m1:

                    st.metric(
                        "Faithfulness",
                        pipeline_a["evaluation"]["faithfulness"]
                    )

                with m2:

                    st.metric(
                        "Relevancy",
                        pipeline_a["evaluation"]["answer_relevancy"]
                    )

                st.metric(
                    "Retrieved Chunks",
                    pipeline_a["retrieved_chunks"]
                )

                st.markdown(
                    "</div>",
                    unsafe_allow_html=True
                )

            with col2:

                st.markdown(
                    '<div class="pipeline-card-pink">',
                    unsafe_allow_html=True
                )

                st.markdown(
                    '<div class="pipeline-title-pink">🟣 Pipeline B</div>',
                    unsafe_allow_html=True
                )

                st.markdown("### 💬 Answer")

                st.markdown(
                    f'<div class="answer-box">{pipeline_b["answer"]}</div>',
                    unsafe_allow_html=True
                )

                st.markdown("### 📈 Metrics")

                m1, m2 = st.columns(2)

                with m1:

                    st.metric(
                        "Faithfulness",
                        pipeline_b["evaluation"]["faithfulness"]
                    )

                with m2:

                    st.metric(
                        "Relevancy",
                        pipeline_b["evaluation"]["answer_relevancy"]
                    )

                st.metric(
                    "Retrieved Chunks",
                    pipeline_b["retrieved_chunks"]
                )

                st.markdown(
                    "</div>",
                    unsafe_allow_html=True
                )

        else:

            st.error("❌ Failed to run pipelines")