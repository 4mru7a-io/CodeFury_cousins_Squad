from pathlib import Path
import chromadb

def get_collection(vector_dir: str, collection_name: str):
    Path(vector_dir).mkdir(parents=True, exist_ok=True)
    client = chromadb.PersistentClient(path=vector_dir)
    return client.get_or_create_collection(
        name=collection_name, metadata={"hnsw:space": "cosine"}
    )

def upsert_documents(collection, documents, embeddings):
    ids = [d["id"] for d in documents]

    collection.upsert(
        ids=ids,
        documents=[d["text"] for d in documents],
        metadatas=[d["metadata"] for d in documents],
        embeddings=embeddings,
    )

    return len(ids)
