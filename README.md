# 🤖 RAG Pipeline Optimizer

An AI-powered platform to compare and evaluate multiple Retrieval-Augmented Generation (RAG) pipelines using FastAPI, ChromaDB, OpenAI, and Streamlit.

---

# 🚀 Features

✅ Upload PDF documents  
✅ Generate vector embeddings using HuggingFace  
✅ Store embeddings in ChromaDB  
✅ Run multiple RAG pipelines  
✅ Compare retrieval strategies  
✅ Evaluate responses using AI metrics  
✅ Interactive Streamlit dashboard  
✅ FastAPI backend APIs  
✅ Modern cyberpunk UI  

---

# 🧠 What is RAG?

RAG (Retrieval-Augmented Generation) combines:

- Vector search / retrieval
- Large Language Models (LLMs)

The system:
1. Retrieves relevant chunks from documents
2. Sends retrieved context to the LLM
3. Generates accurate contextual answers

---

# 🏗️ Architecture

```text
                ┌─────────────────┐
                │   Streamlit UI  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │   FastAPI API   │
                └────────┬────────┘
                         │
         ┌───────────────┼────────────────┐
         ▼                                ▼
┌──────────────────┐          ┌──────────────────┐
│ Pipeline A       │          │ Pipeline B       │
│ Top-3 Retrieval  │          │ Top-5 Retrieval  │
└────────┬─────────┘          └────────┬─────────┘
         ▼                                ▼
              ┌──────────────────┐
              │    ChromaDB      │
              │ Vector Database  │
              └──────────────────┘
                         │
                         ▼
              ┌──────────────────┐
              │  OpenAI GPT-4o   │
              └──────────────────┘
```

---

# 🛠️ Tech Stack

## Frontend
- Streamlit

## Backend
- FastAPI
- Python

## AI / ML
- LangChain
- OpenAI
- HuggingFace Embeddings
- ChromaDB

## Evaluation
- RAGAS

---

# 📂 Project Structure

```text
rag-pipeline-optimizer/
│
├── backend/
│   ├── rag/
│   │   ├── ingest.py
│   │   ├── pipeline_a.py
│   │   ├── pipeline_b.py
│   │   ├── evaluator.py
│   │   └── retrieval.py
│   │
│   ├── main.py
│   └── requirements.txt
│
├── streamlit_app.py
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/rag-pipeline-optimizer.git
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

---

## 3. Activate Environment

### Mac/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## 4. Install Dependencies

```bash
pip install -r backend/requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file inside `backend/`

```env
OPENAI_API_KEY=your_openai_api_key
```

---

# ▶️ Run Backend

```bash
cd backend
uvicorn main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

# ▶️ Run Frontend

From root directory:

```bash
streamlit run streamlit_app.py
```

Frontend runs on:

```text
http://localhost:8501
```

---

# 📊 RAG Pipelines

## 🔷 Pipeline A
- Top-3 retrieval
- Faster response
- Lower retrieval depth

## 🟣 Pipeline B
- Top-5 retrieval
- Higher contextual coverage
- Better retrieval diversity

---

# 📈 Evaluation Metrics

The platform compares pipelines using:

- Faithfulness
- Answer Relevancy
- Retrieval Quality
- Context Precision

---

# 🖼️ Dashboard

The dashboard provides:

- PDF Upload
- Query Input
- Pipeline Comparison
- Metrics Visualization
- Best Pipeline Selection

---

# 🔮 Future Improvements

- Hybrid Search (BM25 + Vector Search)
- Reranking Models
- Multi-document ingestion
- Docker deployment
- Kubernetes scaling
- Authentication system
- Real-time monitoring
- LangSmith tracing
