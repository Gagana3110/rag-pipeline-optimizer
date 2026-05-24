from dotenv import load_dotenv
from rag.evaluator import evaluate_pipeline
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

load_dotenv()

PERSIST_DIRECTORY = "./db/chroma_db"

def run_pipeline_b(query):

    # Different embedding model
    embeddings = HuggingFaceEmbeddings(
       model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Load ChromaDB
    vectordb = Chroma(
        persist_directory=PERSIST_DIRECTORY,
        embedding_function=embeddings
    )

    # Different retrieval strategy
    retriever = vectordb.as_retriever(
        search_kwargs={"k": 5}
    )

    docs = retriever.get_relevant_documents(query)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    prompt = f"""
    You are an accurate AI assistant.

    Use ONLY the provided context.

    Context:
    {context}

    Question:
    {query}
    """

    response = llm.invoke(prompt)
    evaluation = evaluate_pipeline(
    question=query,
    answer=response.content,
    context=context
)

    return {
    "pipeline": "Pipeline B",
    "answer": response.content,
    "retrieved_chunks": len(docs),
    "evaluation": evaluation
}