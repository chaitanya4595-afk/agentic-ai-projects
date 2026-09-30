# RAG Telecom Chatbot

> I keep this folder as an earlier version of the project. The current code and setup instructions are in [telecom-rag-chatbot](https://github.com/kcrokkam/telecom-rag-chatbot).

[My other projects](../README.md)

A Retrieval-Augmented Generation (RAG) customer care chatbot for telecom support. It answers questions about mobile connectivity, billing, SIM issues, and roaming by retrieving relevant context from three knowledge sources and generating responses with Qwen3.8-27B via Groq.

## Architecture

```
User question
     │
     ▼
Merged Retriever (top-k from each store)
  ├── ChromaDB · faq        (FAQ entries from CSV)
  ├── ChromaDB · tickets    (resolved support tickets from SQLite)
  └── ChromaDB · guides     (PDF guide chunks)
     │
     ▼
ChatPromptTemplate → Qwen3.8-27B (Groq) → Answer
```

**Embedding model:** `sentence-transformers/all-MiniLM-L6-v2` (runs locally via HuggingFace)  
**LLM:** `qwen/qwen3.8-27b` served by [Groq](https://groq.com)

## Project Structure

```
telecom_rag_chatbot/
├── app.py              # Streamlit web UI
├── main.py             # CLI entry point
├── rag_chain.py        # Builds the LangChain RAG chain
├── retriever.py        # Merges the three Chroma retrievers
├── ingest_faq.py       # Loads data/faq.csv → Chroma 'faq' collection
├── ingest_tickets.py   # Loads data/tickets.db → Chroma 'tickets' collection
├── ingest_pdf.py       # Loads data/telecom_guide.pdf → Chroma 'guides' collection
├── data/
│   ├── faq.csv             # FAQ question/answer pairs
│   ├── tickets.db          # SQLite database of resolved support tickets
│   └── telecom_guide.pdf   # Telecom user guide (chunked at ingest)
├── chroma_store/       # Persisted Chroma vector database (created at ingest)
├── pyproject.toml
├── uv.lock
└── .env.example
```

## Prerequisites

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip
- A [Groq API key](https://console.groq.com)
- A [HuggingFace token](https://huggingface.co/settings/tokens) (for downloading the embedding model)

## Setup

**1. Clone and install dependencies**

```bash
git clone https://github.com/kcrokkam/agentic-ai-projects.git
cd agentic-ai-projects/telecom_rag_chatbot
uv sync          # or: pip install -e .
```

**2. Configure environment variables**

```bash
cp .env.example .env
```

Edit `.env` and fill in your keys:

```
GROQ_API_KEY=your_groq_api_key_here
HF_TOKEN=your_huggingface_token_here
```

**3. Ingest data into Chroma**

Run the three ingestion scripts once to build the vector store:

```bash
uv run telecom-ingest
```

Each script embeds the source data and persists it to `chroma_store/`. Re-run a script only when its source data changes.

## Running the App

**Streamlit web UI**

```bash
uv run telecom-web
```

Opens at `http://localhost:8501`. The sidebar has one-click sample questions and a button to clear the conversation history.

**CLI**

```bash
uv run telecom-chat
```

Interactive prompt — type a question and press Enter. Type `quit` to exit.

## Data Sources

| Collection | Source file | Granularity |
|---|---|---|
| `faq` | `data/faq.csv` | 1 document per FAQ row |
| `tickets` | `data/tickets.db` | 1 document per resolved ticket |
| `guides` | `data/telecom_guide.pdf` | Chunks of 600 chars with 100-char overlap |

The retriever fetches the top 3 results from each collection (9 context documents total) for every query.

## Installable package

Build the telecom project from the repository root:

```bash
uv build telecom_rag_chatbot --out-dir telecom_rag_chatbot/dist
```

This produces a wheel (`.whl`) and source distribution (`.tar.gz`). Both include
the FAQ CSV, resolved-ticket SQLite database, and PDF guide. API keys, virtual
environments, and generated vector stores are excluded.

Install the wheel into a Python 3.11+ virtual environment:

```bash
python -m pip install telecom_rag_chatbot/dist/rag_telecom_chatbot-0.1.0-py3-none-any.whl
```

Create a `.env` file in your working directory with `GROQ_API_KEY` and optionally
`HF_TOKEN`, then run:

```bash
telecom-ingest          # all three bundled data sources
telecom-web             # Streamlit UI
telecom-chat            # terminal chat, as an alternative to the UI
```

Use the same working directory for ingestion and chat, or set
`TELECOM_CHROMA_DIR` to an absolute path in `.env`. The vector store defaults to
`./chroma_store`; bundled source data is located relative to the installed
package. Individual sources can be ingested with `telecom-ingest faq`,
`telecom-ingest tickets`, or `telecom-ingest pdf`.

The original `python ingest_faq.py`, `python ingest_tickets.py`,
`python ingest_pdf.py`, `python main.py`, and `streamlit run app.py` commands
also work from the source directory. The current configured model is
`qwen/qwen3.8-27b`; availability depends on your Groq account.

Run packaging smoke tests from the repository root after building:

```bash
python -m unittest discover -s telecom_rag_chatbot/tests -v
```
