from huggingface_hub import list_models
import requests
from bs4 import BeautifulSoup

from normalizer import normalize_model

def search_models(query, max_results=5):
    """
    STEP 1: Discover relevant model IDs from Hugging Face.
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
    STEP 2: Scrape an individual model page.
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

        results = search_models(query)

        if not results:

            print("\n❌ No models found.")

        else:

            print(
                f"\n✅ Found {len(results)} models.\n"
            )

            for i, model in enumerate(
                results,
                start=1
            ):

                print("=" * 70)

                print(f"MODEL #{i}")
                print(f"ID: {model['id']}")
                print(f"URL: {model['url']}")

                try:

                    # STEP 2: SCRAPE
                    scraped_data = scrape_model_page(
                        model["url"]
                    )

                    # STEP 3: NORMALIZE
                    normalized_model = normalize_model(
                        model["id"],
                        model["url"],
                        scraped_data
                    )

                    # DISPLAY RESULT
                    print("\nNORMALIZED MODEL DATA:\n")

                    for key, value in normalized_model.items():
                        print(f"{key}: {value}")

                except Exception as e:

                    print(
                        f"\n❌ Processing failed: {e}"
                    )