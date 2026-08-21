from huggingface_hub import list_models
import requests
from bs4 import BeautifulSoup

from config import settings
from embeddings.embed import Embedder
from vectorstore.create_index import get_collection, upsert_documents
from rag.document_builder import build_document
from discovery.normalizer import normalize_model


def search_models(query, max_results=5):
    """
    Discover relevant model IDs from Hugging Face.
    """

    print(f"\n🔍 Searching Hugging Face for: {query}\n")

    models = list(
        list_models(
            search=query,
            limit=max_results,
            sort="downloads"
        )
    )

    results = []

    for model in models:

        model_url = f"https://huggingface.co/{model.id}"

        results.append({
            "id": model.id,
            "url": model_url
        })

    return results


def scrape_model_page(url):
    """
    Scrape an individual model page.
    """

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/131.0.0.0 Safari/537.36"
        )
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=15
    )

    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    title = (
        soup.title.get_text(strip=True)
        if soup.title
        else ""
    )

    text = soup.get_text(
        " ",
        strip=True
    )

    return {
        "url": url,
        "title": title,
        "text": text[:5000]
    }


if __name__ == "__main__":

    query = input(
        "What type of model do you need? "
    ).strip()

    if not query:

        print("❌ Please enter a requirement.")

    else:

        print("\n🔍 Discovering models...")

        # STEP 1: MODEL DISCOVERY
        results = search_models(query)

        if not results:

            print("\n❌ No models found.")

        else:

            print(
                f"\n✅ Found {len(results)} models.\n"
            )

            # Load RAG components only once
            print("🔄 Loading RAG components...")

            embedder = Embedder(
                settings.embedding_model
            )

            collection = get_collection(
                settings.vector_dir,
                settings.collection_name
            )

            print("✅ RAG ready.\n")

            # STEP 2 onwards
            for i, model in enumerate(
                results,
                start=1
            ):

                print("=" * 70)

                print(f"MODEL #{i}")
                print(f"ID: {model['id']}")
                print(f"URL: {model['url']}")

                try:

                    # STEP 2: SCRAPE MODEL PAGE
                    scraped_data = scrape_model_page(
                        model["url"]
                    )

                    # STEP 3: NORMALIZE
                    normalized_model = normalize_model(
                        model["id"],
                        model["url"],
                        scraped_data
                    )

                    # STEP 4: BUILD RAG DOCUMENT
                    rag_text = build_document(
                        normalized_model
                    )

                    # Chroma metadata cannot contain None values
                    clean_metadata = {
                        key: str(value)
                        for key, value in normalized_model.items()
                        if value is not None
                    }

                    document = {
                        "text": rag_text,
                        "metadata": clean_metadata
                    }

                    # STEP 5: CREATE EMBEDDING
                    embeddings = embedder.encode(
                        [rag_text]
                    )

                    # STEP 6: ADD TO CHROMA
                    upserted = upsert_documents(
                        collection,
                        [document],
                        embeddings
                    )

                    print("\nNORMALIZED MODEL DATA:\n")

                    for key, value in normalized_model.items():
                        print(f"{key}: {value}")

                    print(
                        f"\n✅ Added to RAG database: "
                        f"{upserted} model"
                    )

                except Exception as e:

                    print(
                        f"\n❌ Processing failed: {e}"
                    )