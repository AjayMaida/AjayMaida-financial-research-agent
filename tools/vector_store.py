import chromadb
from chromadb.utils import embedding_functions

client = chromadb.PersistentClient(path="./data/chroma_db")

embedding_fn = embedding_functions.DefaultEmbeddingFunction()

collection = client.get_or_create_collection(
    name="financial_docs",
    embedding_function=embedding_fn
)

def add_documents(docs: list[dict]):
    """docs = [{"id": "...", "text": "...", "metadata": {...}}]"""
    collection.add(
        ids=[d["id"] for d in docs],
        documents=[d["text"] for d in docs],
        metadatas=[d.get("metadata", {}) for d in docs]
    )

def query_documents(query: str, n_results: int = 3) -> list[str]:
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )
    return results["documents"][0] if results["documents"] else []