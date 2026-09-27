# Agentic AI Projects

LLM apps and agents built with LangChain, Groq, Gemini and Streamlit.

| Folder | What it is |
|---|---|
| `ai_shopping_agent/` | Shopping assistant agent that searches products, checks ratings, places orders and supports search by image |
| `blood_work_analyzer/` | Reads a blood report, flags HIGH/LOW/NORMAL values and suggests an Indian diet plan |
| `telecom_rag_chatbot/` | RAG customer-care chatbot over FAQs, support tickets and a PDF guide (see its own README) |
| `call_llm.ipynb` | Basic LLM calls with LangChain |

## AI Shopping Agent

A LangChain agent running on Groq with four tools:

- `search_products` searches a SQLite product catalog by keyword, price and organic status.
- `get_rating` returns the average customer rating for a product.
- `checkout` places an order and saves it to the database.
- `describe_product_image` uses a vision model to identify a product from an uploaded photo.

Sample images for the image search are in `ai_shopping_agent/resources/`.

```bash
cd ai_shopping_agent
uv run streamlit run app.py
```

Needs `GROQ_API_KEY`. Rebuild the product database with `uv run python setup_db.py`.

## Blood Work Analyzer

A two-stage Gemini pipeline. The first call extracts every test value and classifies it against its reference range. The second writes a plain-language health summary and a diet plan. A sample report is preloaded, and you can paste your own.

```bash
uv run streamlit run blood_work_analyzer/streamlit_app/app.py
```

Needs `GOOGLE_API_KEY`. The notebook version is `blood_work_analyzer/blood_work_analysis.ipynb`.

## Setup

```bash
uv sync
cp telecom_rag_chatbot/.env.example .env   # then add GROQ_API_KEY and GOOGLE_API_KEY
```

## Deploying on Streamlit Community Cloud

Each app has its own `requirements.txt` next to its entry file, so it deploys without the heavier dependencies of the other projects.

| App | Main file path | Secret |
|---|---|---|
| AI Shopping Agent | `ai_shopping_agent/app.py` | `GROQ_API_KEY` |
| Blood Work Analyzer | `blood_work_analyzer/streamlit_app/app.py` | `GOOGLE_API_KEY` |

Choose Python 3.12 under advanced settings.
