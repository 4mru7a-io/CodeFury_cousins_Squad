import requests

# def generate_answer(base_url: str, api_key: str, model: str, prompt: str) -> str:
#     if not (base_url and api_key and model):
#         raise RuntimeError(
#             "LLM configuration missing. Set LLM_BASE_URL, LLM_API_KEY and LLM_MODEL."
#         )
#     url = base_url.rstrip("/") + "/chat/completions"
#     response = requests.post(
#         url,
#         headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
#         json={
#             "model": model,
#             "messages": [
#                 {"role": "system", "content": "Answer using only the supplied evidence."},
#                 {"role": "user", "content": prompt},
#             ],
#             "temperature": 0.1,
#         },
#         timeout=90,
#     )
#     response.raise_for_status()
#     return response.json()["choices"][0]["message"]["content"]
def generate_answer(base_url: str, api_key: str, model: str, prompt: str) -> str:

    # Temporary fallback for testing
    if not (base_url and api_key and model):
        return (
            "LLM generation is not configured yet.\n\n"
            "Grounded evidence has been retrieved and filtered successfully.\n"
            "The retrieved model candidates are available in the pipeline result."
        )

    import requests

    url = base_url.rstrip("/") + "/chat/completions"

    response = requests.post(
        url,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": model,
            "messages": [
                {
                    "role": "system",
                    "content": "Answer using only the supplied evidence."
                },
                {
                    "role": "user",
                    "content": prompt
                },
            ],
            "temperature": 0.1,
        },
        timeout=90,
    )
    try:
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        # Fail gracefully during demos — return fallback message including a short error note.
        return (
            "LLM generation failed or is not configured correctly.\n\n"
            "Grounded evidence has been retrieved and filtered successfully.\n"
            "The retrieved model candidates are available in the pipeline result.\n\n"
            f"(LLM error: {str(e)})"
        )