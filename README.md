# ModelProof

### AI Model Discovery, Comparison & Evaluation Platform

ModelProof is an AI model marketplace designed to help developers, startups, and businesses discover the right AI model for their specific requirements.

Instead of manually searching through hundreds of models, ModelProof allows users to describe their requirements and discover relevant models using semantic retrieval, structured metadata, performance information, pricing, and evaluation signals.

---

## 🚀 Problem

Choosing the right AI model is often difficult.

Developers need to compare:

- Model capabilities
- Supported tasks
- Performance
- Latency
- Pricing
- Context window
- Deployment requirements
- Open-source availability
- Model reliability

Information is usually scattered across different model repositories and documentation.

**ModelProof brings this information together into one platform.**

---

## 💡 Solution

ModelProof provides a centralized AI model discovery and evaluation system.

Users can:

1. Describe what they need.
2. Search for relevant AI models.
3. Retrieve semantically matching models.
4. Compare multiple models.
5. Evaluate models using structured signals.
6. Make an informed model-selection decision.

---

## ✨ Key Features

### 🔍 Semantic Model Discovery

Users can enter natural-language requirements such as:

> "I need a Hindi model for automatic speech recognition."

The system converts the requirement into an embedding and retrieves semantically relevant models.

---

### 🧠 RAG-Based Retrieval

ModelProof uses a Retrieval-Augmented Generation architecture.

The retrieval pipeline combines:

- Requirement parsing
- Candidate filtering
- Document construction
- Sentence embeddings
- Vector similarity search
- Grounded response generation

This allows the system to work with structured model information rather than relying only on an LLM's internal knowledge.

---

### 📊 Model Comparison

Users can compare models across important dimensions such as:

- Overall performance
- Reasoning
- Coding
- Vision
- Latency
- Rating
- Cost
- Intended use case

---

### 💰 Cost Awareness

Model information includes pricing fields such as:

- Input price
- Output price
- Currency

This helps users consider both capability and cost when selecting a model.

---

### ⚡ Performance Evaluation

ModelProof presents evaluation signals including:

- Performance
- Evidence
- Value
- Trust
- Task compatibility

The goal is to make model recommendations more transparent and understandable.

---

### 🎨 Interactive Web Interface

The frontend provides:

- Model marketplace
- Search
- Category filters
- Model cards
- Comparison interface
- Evaluation section
- Interactive animations
- Responsive design
- Model detail modals

---

## 🏗️ Architecture

```text
                         ┌──────────────────────┐
                         │       User           │
                         │ Natural Language Req │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   Requirement Parser │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Candidate Filtering  │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Document Builder     │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Sentence Transformer│
                         │  MiniLM Embeddings   │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   Chroma Vector DB   │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │      Retriever       │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Grounded Prompt      │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │      LLM / Gemini    │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │      FastAPI API     │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   ModelProof UI      │
                         └──────────────────────┘
🛠️ Tech Stack
Backend
Python
FastAPI
Uvicorn
Pandas
AI / ML
Sentence Transformers
all-MiniLM-L6-v2
Retrieval-Augmented Generation (RAG)
LLM-based grounded generation
Vector Database
ChromaDB
Frontend
HTML5
CSS3
JavaScript
Font Awesome
Google Fonts
Data
CSV / Excel model metadata
Development
Git
GitHub
VS Code
📁 Project Structure
modelproof_rag_phase1/
│
├── api/
│   └── app.py
│
├── config.py
│
├── data/
│   └── models.xlsx
│
├── embeddings/
│   └── embed.py
│
├── filtering/
│   └── candidate_filter.py
│
├── generation/
│   ├── generate.py
│   └── prompt.py
│
├── ingestion/
│   ├── load_data.py
│   └── build_documents.py
│
├── requirement/
│   └── parser.py
│
├── vectorstore/
│   ├── create_index.py
│   └── retriever.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── pipeline.py
├── test_pipeline.py
├── test_retrieval.py
├── requirements.txt
└── README.md
📋 Model Data Schema

The model dataset contains structured information such as:

Field	Description
model_name	Name of the AI model
provider	Model provider
task	Supported AI task
description	Model description
parameters	Model parameter information
context_window	Supported context length
input_price	Input cost
output_price	Output cost
currency	Pricing currency
latency	Expected latency

Additional benchmark and model metadata can also be included.

⚙️ Installation

Clone the repository:

git clone https://github.com/4mru7a-io/CodeFury_cousins_Squad.git

Move into the project:

cd modelproof_rag_phase1

Create a virtual environment:

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt
🔐 Environment Variables

API keys and other secrets should never be committed to GitHub.

Create a .env file or configure environment variables locally.

Example:

MODEL_DATA_PATH=data/models.xlsx
VECTOR_COLLECTION=modelproof_models
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2

LLM_BASE_URL=https://generativelanguage.googleapis.com/v1beta
LLM_API_KEY=YOUR_API_KEY_HERE
LLM_MODEL=gemini-2.5-flash

Important: Replace YOUR_API_KEY_HERE with your own API key locally. Never upload the actual key to GitHub.

▶️ Running the Application

Start the FastAPI server:

uvicorn api.app:app --reload

The application will be available at:

http://127.0.0.1:8000

Open the URL in your browser to access ModelProof.

🔎 Example Query

Example user requirement:

I need a Hindi model for automatic speech recognition.

The system processes the requirement through:

User Requirement
       ↓
Requirement Parsing
       ↓
Candidate Filtering
       ↓
Semantic Embedding
       ↓
Vector Retrieval
       ↓
Relevant Models
       ↓
Grounded Generation
       ↓
Recommendation
🎯 Use Cases

ModelProof can be useful for:

Developers selecting AI APIs
Startups evaluating AI models
Businesses comparing model costs
ML engineers looking for specialized models
Teams choosing models for production workloads
Researchers exploring available AI models
🔮 Future Scope

Potential future improvements include:

Automatic model discovery from public model repositories
Real-time model metadata updates
More comprehensive benchmark integration
User-specific recommendation profiles
Model deployment integration
API playground
Community reviews and ratings
Advanced cost estimation
Multi-provider model comparison
Automated evaluation pipelines
Continuous model monitoring
🏆 Hackathon Vision

ModelProof aims to make AI model selection simpler, faster, and more transparent.

Instead of asking:

"Which AI model should I use?"

users should be able to ask:

"What model is best for my requirements?"

and receive an evidence-backed, comparable recommendation.

👥 Team
CodeFury Cousins Squad

Built as a hackathon project focused on AI model discovery, retrieval, comparison, and evaluation.

📜 License

This project is developed for educational and hackathon purposes.

⭐ Acknowledgements

This project uses open-source technologies and models from the broader AI/ML ecosystem, including:

Sentence Transformers
ChromaDB
FastAPI
Hugging Face ecosystem
Google Gemini
