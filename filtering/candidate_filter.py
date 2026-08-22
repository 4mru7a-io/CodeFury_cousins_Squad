# def filter_candidates(candidates, requirement):
#     filtered = []

#     for item in candidates:

#         metadata = item.get("metadata", {})

#         # 1. Task filter
#         required_task = requirement.get("task")

#         if required_task:
#             model_task = metadata.get("task", "").lower()

#             if model_task != required_task.lower():
#                 continue

#         # 2. Language filter
#         required_languages = requirement.get(
#             "languages",
#             []
#         )

#         if required_languages:
#             model_languages = (
#                 metadata.get(
#                     "supported_languages",
#                     ""
#                 )
#                 .lower()
#             )

#             language_match = all(
#                 language.lower() in model_languages
#                 for language in required_languages
#             )

#             if not language_match:
#                 continue

#         # 3. Open-source filter
#         if requirement.get(
#             "open_source_required",
#             False
#         ):

#             license_info = metadata.get(
#                 "license",
#                 ""
#             ).lower()

#             if not license_info:
#                 continue

#         # 4. Quantization filter
#         if requirement.get(
#             "quantization_required",
#             False
#         ):

#             quantization = metadata.get(
#                 "quantization",
#                 ""
#             ).lower()

#             if not quantization:
#                 continue

#         filtered.append(item)

#     return filtered
import re


def filter_candidates(candidates, requirement):
    filtered = []

    for item in candidates:
        metadata = item.get("metadata", {})

        # Task filter
        required_task = requirement.get("task")

        if required_task:
            model_task = metadata.get("task", "").lower()

            if model_task != required_task.lower():
                continue

        # Language filter
        required_languages = requirement.get("languages", [])

        if required_languages:
            model_languages = metadata.get(
                "supported_languages", ""
            ).lower()

            language_match = all(
                language.lower() in model_languages
                for language in required_languages
            )

            if not language_match:
                continue

        # VRAM filter
        max_vram = requirement.get("max_vram_gb")

        if max_vram is not None:
            hardware = metadata.get(
                "hardware_requirements", ""
            ).lower()

            vram_values = re.findall(
                r"(\d+(?:\.\d+)?)\s*gb",
                hardware
            )

            if vram_values:
                required_vram = min(
                    float(value)
                    for value in vram_values
                )

                if required_vram > max_vram:
                    continue

        # Open-source filter
                # Open-source filter
        if requirement.get("open_source_required", False):

            license_info = metadata.get(
                "license",
                ""
            ).lower()

            open_source_licenses = [
                "apache",
                "mit",
                "bsd",
                "gpl",
                "lgpl",
                "agpl",
                "mpl",
            ]

            is_open_source = any(
                license_name in license_info
                for license_name in open_source_licenses
            )

            if not is_open_source:
                continue
        # Quantization filter
        if requirement.get("quantization_required", False):
            quantization = metadata.get(
                "quantization", ""
            ).lower()

            if not quantization:
                continue

        filtered.append(item)

    return filtered