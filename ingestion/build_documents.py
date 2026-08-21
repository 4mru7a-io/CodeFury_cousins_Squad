from typing import Any, Dict, List
import pandas as pd

def _clean(value: Any) -> str:
    if pd.isna(value):
        return "Not available"
    return str(value).strip()

def row_to_document(row: pd.Series) -> Dict[str, Any]:
    fields = [
        ("Model", "model_name"), ("Provider", "provider"),
        ("Model family", "model_family"), ("Version", "model_version"),
        ("Task", "task"), ("Description", "description"),
        ("Parameters", "parameters"), ("Context window", "context_window"),
        ("Input price", "input_price"), ("Output price", "output_price"),
        ("Currency", "currency"), ("Latency", "latency"),
        ("Benchmark score", "benchmark_score"), ("Benchmark name", "benchmark_name"),
        ("Supported languages", "supported_languages"),
        ("Hardware requirements", "hardware_requirements"),
        ("Quantization", "quantization"), ("License", "license"),
        ("Open source", "open_source"), ("Limitations", "limitations"),
        ("Strengths", "strengths"), ("Use cases", "use_cases"),
        ("Release date", "release_date"),
    ]
    text = "\n".join(f"{label}: {_clean(row.get(col, None))}" for label, col in fields)
    metadata = {
        "model_name": _clean(row.get("model_name")),
        "provider": _clean(row.get("provider")),
        "model_version": _clean(row.get("model_version")),
        "task": _clean(row.get("task")),
        "license": _clean(row.get("license")),
        "source": _clean(row.get("source")),
        "model_card_url": _clean(row.get("model_card_url")),
        "documentation_url": _clean(row.get("documentation_url")),
        "last_updated": _clean(row.get("last_updated")),
    }
    return {"text": text, "metadata": metadata}

def build_documents(df: pd.DataFrame) -> List[Dict[str, Any]]:
    return [row_to_document(row) for _, row in df.iterrows()]
