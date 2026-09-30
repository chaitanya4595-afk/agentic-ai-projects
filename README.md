# AI & Applied Data Science Portfolio

Python projects by [Krishna Chaitanya](https://github.com/kcrokkam), focused on LLM applications, retrieval, and analysis of unstructured text.

**Start with the standalone repositories below.** Each is the current home for its application, setup instructions, and engineering notes. The code folders in this collection are retained as historical tutorial snapshots.

## Project guide

| Project | Problem and approach | Explore |
| --- | --- | --- |
| **[AI Shopping Agent](https://github.com/kcrokkam/ai-shopping-agent)** | Conversational product discovery: an LLM coordinates catalog search, ratings, image understanding, and demo checkout. | [Architecture](https://github.com/kcrokkam/ai-shopping-agent/blob/main/ARCHITECTURE.md) · [Tests](https://github.com/kcrokkam/ai-shopping-agent/tree/main/tests) · [Demo](https://ai-shopping-agent-fvz8dpwpsfrihivomnkcz2.streamlit.app/) |
| **[Customer Feedback Analyzer](https://github.com/kcrokkam/customer-feedback-analyzer)** | Review analysis: Gemini returns validated sentiment, scores, and themes; a FastAPI service and Streamlit dashboard handle analysis and summaries. | [Architecture](https://github.com/kcrokkam/customer-feedback-analyzer/blob/main/ARCHITECTURE.md) · [Tests](https://github.com/kcrokkam/customer-feedback-analyzer/tree/main/tests) · [Demo](https://customer-feedback-analyzer-748gprrueqgffnaygsoevu.streamlit.app/) |
| **[Telecom RAG Chatbot](https://github.com/kcrokkam/telecom-rag-chatbot)** | Support question answering: retrieval across FAQ rows, resolved tickets, and PDF chunks supplies context to a Groq-hosted model. | [Architecture](https://github.com/kcrokkam/telecom-rag-chatbot/blob/main/ARCHITECTURE.md) · [Package checks](https://github.com/kcrokkam/telecom-rag-chatbot/tree/main/tests) · [Setup](https://github.com/kcrokkam/telecom-rag-chatbot#run-locally) |
| **[Interview Synthesizer](https://github.com/kcrokkam/interview_synthesizer)** | Qualitative research: staged extraction, thematic synthesis, a memo, deterministic quote/number checks, and a critic review. | [Sample memo](https://github.com/kcrokkam/interview_synthesizer/blob/main/output/memo.md) · [Quality report](https://github.com/kcrokkam/interview_synthesizer/blob/main/output/quality_report.md) · [Build log](https://github.com/kcrokkam/interview_synthesizer/blob/main/BUILD_LOG.md) |
| **[Blood Work Analyzer](https://github.com/kcrokkam/blood-work-analyzer)** | Report interpretation demo: separate extraction and interpretation stages with injected model dependencies for testing. | [Architecture](https://github.com/kcrokkam/blood-work-analyzer/blob/main/ARCHITECTURE.md) · [Tests](https://github.com/kcrokkam/blood-work-analyzer/tree/main/tests) · [Demo](https://blood-work-analyzer-ajxxhudcgayqhcsinv7g9u.streamlit.app/) |

## A short review path

**AI / LLM engineering:** start with the Shopping Agent's tool implementations, then review the Telecom Chatbot's retriever and package commands. These show two different application patterns: tool orchestration and retrieval-augmented generation.

**Applied data science:** start with the Feedback Analyzer's validation and summary calculations, then read the Interview Synthesizer's quality report alongside its critic review. These show structured text analysis and the limits of automated evidence checks.

**Pipeline design:** the Blood Work Analyzer separates extraction and interpretation and tests orchestration with a fake model. It is a technical demonstration using sample reports, with no clinical accuracy benchmark.

## What the evidence covers

| Project | Available validation | Boundary |
| --- | --- | --- |
| Shopping Agent | Catalog and rating tests; GitHub Actions | Checkout confirmation is an agent-policy rule; no end-to-end agent quality benchmark |
| Feedback Analyzer | Analytics, API, persistence, and mocked service tests | No measured sentiment/theme accuracy benchmark |
| Telecom Chatbot | Package contents, command help, and installed data-path checks | No retrieval relevance or answer-quality benchmark |
| Interview Synthesizer | Source checks, saved critic output, and versioned build notes | Synthetic interviews; quote/number matches do not guarantee correct attribution or reasoning |
| Blood Work Analyzer | Model-independent two-stage pipeline tests | No clinical validation or extraction-accuracy benchmark |

## Historical tutorial material

These folders preserve the earlier learning versions. Use the standalone repositories above for current work; updates to an application should be made there.

| Snapshot | Current project |
| --- | --- |
| [`ai_shopping_agent/`](ai_shopping_agent/) | [ai-shopping-agent](https://github.com/kcrokkam/ai-shopping-agent) |
| [`blood_work_analyzer/`](blood_work_analyzer/) | [blood-work-analyzer](https://github.com/kcrokkam/blood-work-analyzer) |
| [`telecom_rag_chatbot/`](telecom_rag_chatbot/) | [telecom-rag-chatbot](https://github.com/kcrokkam/telecom-rag-chatbot) |
| [`call_llm.ipynb`](call_llm.ipynb) | Introductory model-call experiments |

The root dependency files belong to these historical examples. Each standalone repository documents its own environment and commands. Earlier commits and the original telecom package release remain available here.
