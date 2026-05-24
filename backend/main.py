from fastapi import FastAPI, UploadFile, File
import shutil
import os
import asyncio

from rag.ingest import ingest_document
from rag.pipeline_a import run_pipeline_a
from rag.pipeline_b import run_pipeline_b

app = FastAPI()

UPLOAD_DIRECTORY = "./uploaded_docs"

os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

@app.get("/")
def home():
    return {"message": "RAG Optimizer Backend Running"}

# PDF Upload Endpoint
@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    file_path = os.path.join(
        UPLOAD_DIRECTORY,
        file.filename
    )

    # Save uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Process PDF
    chunks_created = ingest_document(file_path)

    return {
        "filename": file.filename,
        "chunks_created": chunks_created,
        "status": "Document processed successfully"
    }

# Question Answering Endpoint
@app.post("/ask")
async def ask_question(query: str):

    results = await asyncio.gather(
        asyncio.to_thread(run_pipeline_a, query),
        asyncio.to_thread(run_pipeline_b, query)
    )

    return {
        "pipeline_a": results[0],
        "pipeline_b": results[1]
    }