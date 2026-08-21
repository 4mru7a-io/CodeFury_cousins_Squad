import requests

def generate_answer(base_url: str, api_key: str, model: str, prompt: str) -> str:
    if not (base_url and api_key and model):
        raise RuntimeError(
            "LLM configuration missing. Set LLM_BASE_URL, LLM_API_KEY and LLM_MODEL."
        )
    url = base_url.rstrip("/") + "/chat/completions"
    response = requests.post(
        url,
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        json={
            "model": model,
            "messages": [
                {"role": "system", "content": "Answer using only the supplied evidence."},
                {"role": "user", "content": prompt},
            ],
            "temperature": 0.1,
        },
        timeout=90,
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
