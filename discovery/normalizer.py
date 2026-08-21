from datetime import date


def normalize_model(model_id, model_url, scraped_data):

    raw_text = scraped_data["text"].lower()

    model_name = model_id.split("/")[-1]
    provider = model_id.split("/")[0]

    # Task detection
    task = "unknown"

    if "automatic speech recognition" in raw_text:
        task = "automatic-speech-recognition"

    elif "text generation" in raw_text:
        task = "text-generation"

    elif "sentence similarity" in raw_text:
        task = "sentence-similarity"

    elif "image classification" in raw_text:
        task = "image-classification"

    # Language detection
    languages = []

    if "hindi" in raw_text:
        languages.append("Hindi")

    if "english" in raw_text:
        languages.append("English")

    if "chinese" in raw_text:
        languages.append("Chinese")

    # License detection
    license_name = None

    if "apache-2.0" in raw_text:
        license_name = "Apache-2.0"

    elif "mit" in raw_text:
        license_name = "MIT"

    elif "cc-by-4.0" in raw_text:
        license_name = "CC-BY-4.0"

    # Open-source detection
    open_source = None

    if license_name in [
        "Apache-2.0",
        "MIT",
        "CC-BY-4.0"
    ]:
        open_source = True

    # Description
    description = scraped_data["text"][:500]

    record = {
        "model_name": model_name,
        "provider": provider,
        "model_family": None,
        "model_version": None,
        "task": task,
        "description": description,
        "parameters": None,
        "context_window": None,
        "input_price": None,
        "output_price": None,
        "currency": None,
        "latency": None,
        "benchmark_score": None,
        "benchmark_name": None,
        "supported_languages": ", ".join(languages) if languages else None,
        "hardware_requirements": None,
        "quantization": None,
        "license": license_name,
        "open_source": open_source,
        "model_card_url": model_url,
        "documentation_url": model_url,
        "limitations": None,
        "strengths": None,
        "use_cases": None,
        "release_date": None,
        "source": "web_scraper",
        "last_updated": str(date.today())
    }

    return record