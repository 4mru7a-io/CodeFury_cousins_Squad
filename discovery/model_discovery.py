import requests
from bs4 import BeautifulSoup
from urllib.parse import quote


def search_models(query, max_results=5):
    """
    Discover model pages from Hugging Face's public model search page.
    """

    encoded_query = quote(query)

    url = f"https://huggingface.co/models?search={encoded_query}"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/131.0.0.0 Safari/537.36"
        )
    }

    print(f"\n🌐 Searching: {url}")

    response = requests.get(
        url,
        headers=headers,
        timeout=15
    )

    print(f"HTTP Status: {response.status_code}")

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    results = []

    for link in soup.find_all("a", href=True):

        href = link["href"]

        # Hugging Face model pages
        if href.startswith("/"):
            parts = href.strip("/").split("/")

            if len(parts) == 2 and parts[0] not in [
                "datasets",
                "spaces",
                "docs"
            ]:
                model_url = "https://huggingface.co" + href

                if model_url not in results:
                    results.append(model_url)

        if len(results) >= max_results:
            break

    return results


def scrape_model_page(url):

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

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.get_text(strip=True) if soup.title else ""

    text = soup.get_text(" ", strip=True)

    return {
        "url": url,
        "title": title,
        "text": text[:10000]
    }


if __name__ == "__main__":

    query = input(
        "What type of model do you need? "
    ).strip()

    print("\n🔍 Discovering models...\n")

    results = search_models(query)

    if not results:
        print("❌ No models discovered.")
        print("Try another query.")
    else:

        print(f"✅ Found {len(results)} model pages.\n")

        for i, url in enumerate(results, 1):

            print("=" * 70)
            print(f"MODEL #{i}")
            print(url)

            try:
                data = scrape_model_page(url)

                print(f"Title: {data['title']}")
                print("\nExtracted text:")
                print(data["text"][:500])

            except Exception as e:
                print(f"⚠️ Could not scrape page: {e}")