def build_document(model):

    fields = [
        "model_name",
        "provider",
        "model_family",
        "model_version",
        "task",
        "description",
        "parameters",
        "context_window",
        "supported_languages",
        "hardware_requirements",
        "quantization",
        "license",
        "open_source",
        "limitations",
        "strengths",
        "use_cases",
        "source"
    ]

    lines = []

    for field in fields:

        value = model.get(field)

        if value is not None:
            lines.append(
                f"{field.replace('_', ' ').title()}: {value}"
            )

    return "\n".join(lines)