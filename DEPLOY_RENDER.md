Render deployment notes
======================

1. Push this repository to GitHub.

2. Create a new Web Service on Render (private or public).

   - Environment: Python 3.x
   - Build command: `pip install -r requirements.txt`
   - Start command: `uvicorn api.app:app --host 0.0.0.0 --port $PORT`

3. Add environment variables in the Render dashboard: `LLM_BASE_URL`, `LLM_API_KEY`, `LLM_MODEL`, and any others from `.env.example`.

4. Ensure a persistent volume if you want to keep the local ChromaDB between deploys. Alternatively, use a managed vector DB.

5. To test locally before deploy:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn api.app:app --reload --port 8000
```

6. Frontend: host on Vercel or Netlify. Configure your frontend to call `https://<your-render-service>.onrender.com/api/search`.
7. Optional quick-start files added to the repo:

- `render.yaml` — manifest for Render with build/start commands and env var placeholders.
- `start.sh` — minimal start script used by Render or local testing.

When creating the Render service, you can select "Deploy from a Dockerfile or Render.yaml" and point it to `render.yaml` to pick up the settings automatically.
