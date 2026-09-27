# Agentic AI Crash Course

Projects built while following the Codebasics Agentic AI crash course.

## Projects

| Folder | What it is |
|---|---|
| `call_llm.ipynb` | First steps calling LLMs with LangChain |
| `2_health_analysis/` | Blood work analysis notebook plus a Streamlit app |
| `10_project_shopping_agent/` | AI shopping assistant agent: searches products, checks ratings, places orders, and supports search by image |
| `11_project_telecom_chatbot/` | RAG customer-care chatbot over FAQs, support tickets and a PDF guide (see its own README) |

## AI Shopping Assistant

A LangChain agent running on Groq with four tools:

- `search_products` searches a SQLite product catalog by keyword, price and organic status.
- `get_rating` returns the average customer rating for a product.
- `checkout` places an order and saves it to the database.
- `describe_product_image` uses a vision model to identify a product from an uploaded photo.

Sample images to try the image search are in `10_project_shopping_agent/resources/`.

### Run locally

```bash
uv sync
echo "GROQ_API_KEY=your_key" > .env
cd 10_project_shopping_agent
uv run streamlit run app.py
```

To rebuild the product database, run `uv run python setup_db.py`.

### Deploy on Streamlit Community Cloud

1. Create a new app from this repo with main file path `10_project_shopping_agent/app.py` and Python 3.12.
2. In the app's secrets, add `GROQ_API_KEY = "your_key"`.

Dependencies for the deployed app are in `10_project_shopping_agent/requirements.txt`.
