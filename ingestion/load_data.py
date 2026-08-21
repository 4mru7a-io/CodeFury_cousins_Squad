from pathlib import Path
import pandas as pd

REQUIRED_COLUMNS = {
    "model_name", "provider", "task", "description", "parameters",
    "context_window", "input_price", "output_price", "currency", "latency"
}

def normalize_columns(df):
    df = df.copy()
    df.columns = [str(c).strip().lower().replace(" ", "_").replace("-", "_") for c in df.columns]
    return df

def load_model_data(path: str):
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Dataset not found: {p}")
    if p.suffix.lower() in {".xlsx", ".xls"}:
        df = pd.read_excel(p)
    elif p.suffix.lower() == ".csv":
        df = pd.read_csv(p)
    else:
        raise ValueError("Supported dataset formats: .xlsx, .xls, .csv")

    df = normalize_columns(df)
    missing = sorted(REQUIRED_COLUMNS - set(df.columns))
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    df = df.dropna(subset=["model_name", "provider"]).copy()
    df["model_name"] = df["model_name"].astype(str).str.strip()
    df["provider"] = df["provider"].astype(str).str.strip()

    before = len(df)
    version_col = "model_version" if "model_version" in df.columns else None
    subset = ["model_name"] + ([version_col] if version_col else [])
    df = df.drop_duplicates(subset=subset, keep="last")

    for col in ["input_price", "output_price", "benchmark_score", "context_window"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    print(f"Loaded rows: {before}")
    print(f"Valid rows: {len(df)}")
    print(f"Duplicates removed: {before - len(df)}")
    return df
