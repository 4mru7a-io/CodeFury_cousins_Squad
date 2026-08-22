import re


class RequirementParser:

    def parse(self, query: str):

        query_lower = query.lower()

        requirement = {
            "raw_query": query,
            "task": None,
            "languages": [],
            "max_input_price": None,
            "max_output_price": None,
            "max_vram_gb": None,
            "open_source_required": False,
            "quantization_required": False,
            "keywords": []
        }

        # -------------------------
        # TASK DETECTION
        # -------------------------

        if any(word in query_lower for word in [
            "speech recognition",
            "speech-to-text",
            "speech to text",
            "asr",
            "transcription"
        ]):
            requirement["task"] = "automatic-speech-recognition"

        elif any(word in query_lower for word in [
            "chatbot",
            "chat model",
            "conversational",
            "conversation"
        ]):
            requirement["task"] = "text-generation"

        elif any(word in query_lower for word in [
            "text generation",
            "language model",
            "llm"
        ]):
            requirement["task"] = "text-generation"

        elif any(word in query_lower for word in [
            "embedding",
            "semantic search",
            "sentence similarity"
        ]):
            requirement["task"] = "sentence-similarity"

        elif "image classification" in query_lower:
            requirement["task"] = "image-classification"

        # -------------------------
        # LANGUAGE DETECTION
        # -------------------------

        languages = [
            "hindi",
            "english",
            "marathi",
            "tamil",
            "telugu",
            "kannada",
            "bengali",
            "gujarati",
            "punjabi"
        ]

        for language in languages:
            if language in query_lower:
                requirement["languages"].append(
                    language.capitalize()
                )

        # -------------------------
        # VRAM DETECTION
        # -------------------------

        vram_match = re.search(
            r"(\d+(?:\.\d+)?)\s*(gb)?\s*(?:vram|gpu|memory)",
            query_lower
        )

        if vram_match:
            requirement["max_vram_gb"] = float(
                vram_match.group(1)
            )

        # -------------------------
        # PRICE DETECTION
        # -------------------------

        price_match = re.search(
            r"(?:under|below|less than|max(?:imum)?)[\s$]*(\d+(?:\.\d+)?)",
            query_lower
        )

        if price_match:
            requirement["max_input_price"] = float(
                price_match.group(1)
            )

        # -------------------------
        # OPEN SOURCE
        # -------------------------

        if any(word in query_lower for word in [
            "open source",
            "open-source",
            "opensource"
        ]):
            requirement["open_source_required"] = True

        # -------------------------
        # QUANTIZATION
        # -------------------------

        if any(word in query_lower for word in [
            "quantized",
            "quantization",
            "4-bit",
            "4 bit",
            "8-bit",
            "8 bit"
        ]):
            requirement["quantization_required"] = True

        # -------------------------
        # KEYWORDS
        # -------------------------

        requirement["keywords"] = [
            word
            for word in [
                "low cost",
                "low latency",
                "fast",
                "small",
                "lightweight",
                "multilingual",
                "efficient",
                "production",
                "commercial"
            ]
            if word in query_lower
        ]

        return requirement