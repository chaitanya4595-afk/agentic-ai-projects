# AI Applications

I'm Krishna Chaitanya Rokkam. My background is in data science, enterprise analytics, and automation. I built these projects to explore how LLMs can work with tools, structured data, and documents to solve practical problems.

Each project has its own repository with the implementation, setup instructions, and design notes. This page brings them together.

## AI Shopping Agent

I built a conversational shopping assistant that searches a catalog, looks up ratings, and identifies products from images. The model chooses which tools to call; Python and SQLite handle the catalog and demo orders. I wanted to understand how an agent moves through a task that involves several tools and follow-up questions.

**Built with:** Python, LangChain, Groq, SQLite, Streamlit.

[Repository](https://github.com/kcrokkam/ai-shopping-agent) · [Demo](https://ai-shopping-agent-fvz8dpwpsfrihivomnkcz2.streamlit.app/) · [Architecture](https://github.com/kcrokkam/ai-shopping-agent/blob/main/ARCHITECTURE.md)

## Telecom RAG Assistant

I built a support assistant that retrieves information from FAQs, resolved tickets, and a PDF guide before generating a response. The main design decision was to keep the sources in separate collections and combine their results when answering a question. I also packaged the application so the same workflow runs through a browser or terminal.

**Built with:** Python, LangChain, Chroma, Hugging Face embeddings, Groq, Streamlit.

[Repository](https://github.com/kcrokkam/telecom-rag-chatbot) · [Demo](https://telecom-rag-chatbot-zr7jytflnhserbkps7uhaq.streamlit.app/) · [Architecture](https://github.com/kcrokkam/telecom-rag-chatbot/blob/main/ARCHITECTURE.md) · [Downloads](https://github.com/kcrokkam/telecom-rag-chatbot/releases)

## Customer Feedback Analyzer

I built this to turn unstructured reviews into a table of sentiment, satisfaction scores, and themes. The dashboard summarizes successful analyses and keeps individual results available for review. I separated the FastAPI service from the UI and used Pydantic to validate model responses before they reach the analytics layer.

**Built with:** Python, Gemini, FastAPI, Pydantic, Streamlit, SQLite.

[Repository](https://github.com/kcrokkam/customer-feedback-analyzer) · [Demo](https://customer-feedback-analyzer-748gprrueqgffnaygsoevu.streamlit.app/) · [Tests](https://github.com/kcrokkam/customer-feedback-analyzer/tree/main/tests)

## Interview Synthesizer

I built a workflow that turns interview transcripts into themes and a short memo. I added quote and number checks because a readable summary is only useful if its claims can be traced back to the source. The saved outputs and build log show what worked and where the workflow overstated or misattributed information.

**Built with:** Python and Claude Code workflows. The example interviews are synthetic.

[Repository](https://github.com/kcrokkam/interview_synthesizer) · [Sample memo](https://github.com/kcrokkam/interview_synthesizer/blob/main/output/memo.md) · [Build log](https://github.com/kcrokkam/interview_synthesizer/blob/main/BUILD_LOG.md)

## Blood Work Analyzer

I built this as an experiment in separating extraction from interpretation. One model call reads the sample report and classifies values; a second uses that result to write a summary and dietary guidance. I test the orchestration with a fake model. This is an educational application, with no clinical validation.

**Built with:** Python, LangChain, Gemini API, Streamlit.

[Repository](https://github.com/kcrokkam/blood-work-analyzer) · [Demo](https://blood-work-analyzer-ajxxhudcgayqhcsinv7g9u.streamlit.app/) · [Pipeline design](https://github.com/kcrokkam/blood-work-analyzer/blob/main/ARCHITECTURE.md)

## Earlier versions

I started the shopping, telecom, and blood-work projects in this repository before giving each application its own home. I keep those versions here alongside my introductory model-call notebook:

- [`ai_shopping_agent/`](ai_shopping_agent/)
- [`telecom_rag_chatbot/`](telecom_rag_chatbot/)
- [`blood_work_analyzer/`](blood_work_analyzer/)
- [`call_llm.ipynb`](call_llm.ipynb)

For current setup instructions and code, use the project repositories linked above. The dependency files in this collection belong to the earlier versions.

[About me](https://github.com/kcrokkam) · [LinkedIn](https://www.linkedin.com/in/krishna-chaitanya-rokkam/)
