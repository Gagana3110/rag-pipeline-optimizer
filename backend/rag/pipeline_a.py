import os

from dotenv import load_dotenv
from rag.evaluator import evaluate_pipeline
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

load_dotenv()

PERSIST_DIRECTORY = "./db/chroma_db"

def run_pipeline_a(query):

    # Load embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Load ChromaDB
    vectordb = Chroma(
        persist_directory=PERSIST_DIRECTORY,
        embedding_function=embeddings
    )

    # Retriever
    retriever = vectordb.as_retriever(
        search_kwargs={"k": 3}
    )

    # Retrieve relevant chunks
    docs = retriever.get_relevant_documents(query)

    context = "\n\n".join([doc.page_content for doc in docs])

    # LLM
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    # Prompt
    prompt = f"""
    Answer the question using ONLY the context below.

    Context:
    {context}

    Question:
    {query}
    """

    # Generate answer
    response = llm.invoke(prompt)
    evaluation = evaluate_pipeline(
    question=query,
    answer=response.content,
    context=context
)

    return {
    "pipeline": "Pipeline A",
    "question": query,
    "answer": response.content,
    "retrieved_chunks": len(docs),
    "evaluation": evaluation
}