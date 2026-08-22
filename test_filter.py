# from filtering.candidate_filter import filter_candidates


# def main():
#     candidates = [
#         {
#             "metadata": {
#                 "model_name": "Qwen2.5-7B-Instruct",
#                 "task": "text-generation",
#                 "supported_languages": "English, Hindi, multilingual",
#                 "hardware_requirements": "8GB+ VRAM",
#                 "license": "Apache 2.0",
#                 "quantization": "4-bit supported",
#             }
#         },
#         {
#             "metadata": {
#                 "model_name": "Whisper-Test",
#                 "task": "automatic-speech-recognition",
#                 "supported_languages": "Hindi",
#                 "hardware_requirements": "4GB VRAM",
#                 "license": "MIT",
#                 "quantization": "supported",
#             }
#         },
#         {
#             "metadata": {
#                 "model_name": "Hindi-Test-Model-10GB",
#                 "task": "text-generation",
#                 "supported_languages": "Hindi, English",
#                 "hardware_requirements": "10GB VRAM",
#                 "license": "Apache 2.0",
#                 "quantization": "4-bit supported",
#             }
#         },
#                 {
#             "metadata": {
#                 "model_name": "Proprietary-Hindi-Model",
#                 "task": "text-generation",
#                 "supported_languages": "Hindi, English",
#                 "hardware_requirements": "6GB VRAM",
#                 "license": "Proprietary Commercial License",
#                 "quantization": "4-bit supported",
#             }
#         }
#     ]

#     requirement = {
#         "task": "text-generation",
#         "languages": ["Hindi"],
#         "max_vram_gb": 8.0,
#         "open_source_required": True,
#         "quantization_required": False,
#     }

#     filtered = filter_candidates(
#         candidates,
#         requirement
#     )

#     print("\nFILTERED CANDIDATES")
#     print("=" * 60)

#     for item in filtered:
#         print(item["metadata"]["model_name"])


# if __name__ == "__main__":
#     main()
from filtering.candidate_filter import filter_candidates


def print_results(title, results):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)

    if not results:
        print("No candidates matched.")

    for item in results:
        metadata = item["metadata"]

        print(
            f"Model: {metadata.get('model_name')}"
        )

        print(
            f"Task: {metadata.get('task')}"
        )

        print(
            f"Languages: "
            f"{metadata.get('supported_languages')}"
        )

        print(
            f"Hardware: "
            f"{metadata.get('hardware_requirements')}"
        )

        print(
            f"License: "
            f"{metadata.get('license')}"
        )

        print("-" * 70)


candidates = [

    {
        "metadata": {
            "model_name": "Hindi-ASR-Model",
            "task": "automatic-speech-recognition",
            "supported_languages": "Hindi, English",
            "hardware_requirements": "4 GB VRAM",
            "license": "Apache 2.0",
            "quantization": "4-bit"
        }
    },

    {
        "metadata": {
            "model_name": "English-Chat-Model",
            "task": "text-generation",
            "supported_languages": "English",
            "hardware_requirements": "12 GB VRAM",
            "license": "MIT",
            "quantization": ""
        }
    },

    {
        "metadata": {
            "model_name": "Multilingual-Embedding-Model",
            "task": "sentence-similarity",
            "supported_languages": "English, Hindi, Marathi",
            "hardware_requirements": "2 GB VRAM",
            "license": "Apache 2.0",
            "quantization": "8-bit"
        }
    }
]


# -------------------------------------------------
# TEST 1: Hindi ASR
# -------------------------------------------------

requirement = {
    "task": "automatic-speech-recognition",
    "languages": ["Hindi"],
    "max_vram_gb": None,
    "open_source_required": False,
    "quantization_required": False
}

results = filter_candidates(
    candidates,
    requirement
)

print_results(
    "TEST 1: Hindi ASR",
    results
)


# -------------------------------------------------
# TEST 2: English chatbot under 8GB VRAM
# -------------------------------------------------

requirement = {
    "task": "text-generation",
    "languages": ["English"],
    "max_vram_gb": 8,
    "open_source_required": False,
    "quantization_required": False
}

results = filter_candidates(
    candidates,
    requirement
)

print_results(
    "TEST 2: English chatbot under 8GB VRAM",
    results
)


# -------------------------------------------------
# TEST 3: Open-source multilingual embedding model
# -------------------------------------------------

requirement = {
    "task": "sentence-similarity",
    "languages": [],
    "max_vram_gb": None,
    "open_source_required": True,
    "quantization_required": False
}

results = filter_candidates(
    candidates,
    requirement
)

print_results(
    "TEST 3: Open-source embedding model",
    results
)


# -------------------------------------------------
# TEST 4: Quantized language model
# -------------------------------------------------

requirement = {
    "task": "text-generation",
    "languages": [],
    "max_vram_gb": None,
    "open_source_required": False,
    "quantization_required": True
}

results = filter_candidates(
    candidates,
    requirement
)

print_results(
    "TEST 4: Quantized language model",
    results
)