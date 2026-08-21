from config import settings
from embeddings.embed import Embedder
from vectorstore.create_index import get_collection
from vectorstore.retriever import Retriever


def main():
    query = input("\nEnter your requirement: ").strip()

    if not query:
        print("Please enter a requirement.")
        return

    print("\nLoading embedding model...")
    embedder = Embedder(settings.embedding_model)

    collection = get_collection(
        settings.vector_dir,
        settings.collection_name
    )

    retriever = Retriever(collection, embedder)

    results = retriever.retrieve(query, top_k=3)

    print("\n" + "=" * 80)
    print("USER REQUIREMENT")
    print(query)

    print("\n" + "=" * 80)
    print("RETRIEVED EVIDENCE")

    for i, item in enumerate(results, start=1):
        print(f"\n{'-' * 60}")
        print(f"MODEL #{i}")
        print(f"Relevance: {item['relevance_score']}")

        print("\nMetadata:")
        for key, value in item["metadata"].items():
            print(f"{key}: {value}")

        print("\nModel Evidence:")
        print(item["document"])


if __name__ == "__main__":
    main()