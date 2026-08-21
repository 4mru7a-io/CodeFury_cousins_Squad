from config import settings
from ingestion.load_data import load_model_data
from ingestion.build_documents import build_documents
from embeddings.embed import Embedder
from vectorstore.create_index import get_collection, upsert_documents
from vectorstore.retriever import Retriever
from generation.prompt import build_grounded_prompt
from generation.generate import generate_answer

def build_index():
    df = load_model_data(settings.data_path)
    documents = build_documents(df)
    embedder = Embedder(settings.embedding_model)
    embeddings = embedder.encode([d["text"] for d in documents])
    collection = get_collection(settings.vector_dir, settings.collection_name)
    count = upsert_documents(collection, documents, embeddings)
    print(f"Indexed documents: {count}")

def ask(query: str, top_k: int = 5):
    embedder = Embedder(settings.embedding_model)
    collection = get_collection(settings.vector_dir, settings.collection_name)
    retriever = Retriever(collection, embedder)
    retrieved = retriever.retrieve(query, top_k=top_k)
    prompt = build_grounded_prompt(query, retrieved)
    answer = generate_answer(
        settings.llm_base_url, settings.llm_api_key, settings.llm_model, prompt
    )
    return {"query": query, "retrieved_models": retrieved, "answer": answer}

if __name__ == "__main__":
    build_index()
    print("RAG index is ready.")
