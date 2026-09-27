# Agentic AI Projects

LLM applications built with LangChain: a tool-using shopping agent, a two-stage medical report analyzer, and a retrieval-augmented support chatbot.

## Live demos

| App | Try it | What to try |
|---|---|---|
| AI Shopping Agent | [chaitanya4595-ai-shopping-agent.streamlit.app](https://chaitanya4595-ai-shopping-agent.streamlit.app) | "I want organic honey under $20 with a 4.5+ rating", then "order #1" |
| Blood Work Analyzer | [chaitanya4595-blood-work-analyzer.streamlit.app](https://chaitanya4595-blood-work-analyzer.streamlit.app) | Click **Analyze** on the preloaded sample report |

## Projects

| Project | Summary | Stack |
|---|---|---|
| [AI Shopping Agent](ai_shopping_agent/) | An agent that searches a product catalog, checks ratings, places orders on confirmation, and finds products from an uploaded photo | LangChain agents, Groq (Qwen3, Llama 4 Scout vision), SQLite, Streamlit |
| [Blood Work Analyzer](blood_work_analyzer/) | Flags each test value as HIGH, LOW or NORMAL, then writes a plain-language summary and an Indian diet plan | LangChain, Gemini API (Gemma 4), Streamlit |
| [Telecom RAG Chatbot](telecom_rag_chatbot/) | Customer-care chatbot that answers from FAQs, resolved support tickets and a PDF guide | LangChain, ChromaDB, Hugging Face embeddings, Groq (Qwen3), Streamlit |

`call_llm.ipynb` holds the basic model calls the projects build on: system prompts, temperature, and switching between Gemini and Groq.

## Run locally

Requires Python 3.12 and [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/chaitanya4595-afk/agentic-ai-projects.git
cd agentic-ai-projects
uv sync
cp .env.example .env   # add your API keys

uv run streamlit run ai_shopping_agent/app.py
uv run streamlit run blood_work_analyzer/streamlit_app/app.py
```

The telecom chatbot needs a one-time ingestion step first. See [its README](telecom_rag_chatbot/README.md).

## Repository layout

```
ai_shopping_agent/      Tool-calling shopping agent + Streamlit UI
blood_work_analyzer/    Notebook prototype + Streamlit app
telecom_rag_chatbot/    RAG pipeline, ingestion scripts, CLI and Streamlit UI
call_llm.ipynb          Model-calling basics
```

Each deployable app has its own `requirements.txt` beside its entry file, so it deploys without the heavier dependencies of the other projects.
