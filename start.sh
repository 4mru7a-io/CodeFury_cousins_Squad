#!/usr/bin/env bash
# Minimal start script used by Render or local testing
exec uvicorn api.app:app --host 0.0.0.0 --port ${PORT:-8000}
