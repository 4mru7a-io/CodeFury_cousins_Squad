# ModelProof — Phase 1 RAG Foundation

## Goal

Build the evidence-grounding layer for an AI Model Marketplace.

Phase 1:
Excel/CSV → cleaning → model documents → embeddings → ChromaDB → retrieval → grounded LLM response.

## Architecture

```text
Excel model dataset
       ↓
Data validation / cleaning
       ↓
Model documents + metadata
       ↓
Embedding model
       ↓
Persistent ChromaDB
       ↓
Semantic retrieval
       ↓
Grounded prompt
       ↓
OpenAI-compatible LLM endpoint
       ↓
Answer + evidence + source URLs
```

## Setup

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate
pip install -r requirements.txt
copy .env.example .env
```

Set the LLM endpoint variables in `.env`.

## Build the index

```bash
python pipeline.py
```

## Run evaluation queries

```bash
python evaluation/test_queries.py
```

## Important design separation

RAG retrieves evidence.
Recommendation Engine (Phase 2) calculates scores and ranks models.
Live Model Arena (later) measures actual outputs and latency.
Scraper pipeline (later) refreshes the model dataset.

## Next phases

1. Natural-language requirement extraction
2. Transparent weighted recommendation engine
3. Automated model-data refresh / scraper pipeline
4. Live Model Arena
5. Frontend dashboard
6. Deployment assistant
