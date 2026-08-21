from config import settings
from embeddings.embed import Embedder
from vectorstore.create_index import get_collection
from vectorstore.retriever import Retriever


def main():

    query = input("\nEnter your requirement: ").strip()

    if not query:
        print("Please enter a requirement.")
        return

    print("\nLoading RAG...")

    embedder = Embedder(settings.embedding_model)

    collection = get_collection(
        settings.vector_dir,
        settings.collection_name
    )

    retriever = Retriever(
        collection,
        embedder
    )

    results = retriever.retrieve(
        query,
        top_k=5
    )

    print("\n" + "=" * 70)
    print("USER REQUIREMENT")
    print(query)

    print("\n" + "=" * 70)
    print("RETRIEVED MODELS")

    for i, item in enumerate(results, start=1):

        print("\n" + "-" * 60)
        print(f"MODEL #{i}")
        print(f"Relevance: {item['relevance_score']}")

        print("\nModel Name:")
        print(
            item["metadata"].get(
                "model_name",
                "Unknown"
            )
        )

        print("\nTask:")
        print(
            item["metadata"].get(
                "task",
                "Unknown"
            )
        )

        print("\nProvider:")
        print(
            item["metadata"].get(
                "provider",
                "Unknown"
            )
        )

        print("\nEvidence:")
        print(
            item["document"][:500]
        )


if __name__ == "__main__":
    main()