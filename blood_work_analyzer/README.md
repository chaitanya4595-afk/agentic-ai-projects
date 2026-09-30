# Blood Work Analyzer

> I keep this folder as an earlier version of the project. The current code and setup instructions are in [blood-work-analyzer](https://github.com/kcrokkam/blood-work-analyzer).

[My other projects](../README.md)

Paste a blood test report and get every value flagged against its reference range, a plain-language health summary, and a practical Indian diet plan.

## How it works

The analysis runs as two chained LLM calls instead of one large prompt.

1. **Extraction.** The model pulls every test value from the report and labels it HIGH, LOW or NORMAL using the report's own reference ranges.
2. **Interpretation.** A second prompt receives only that structured list. Acting as a clinical nutritionist, it writes a short summary and a diet plan with two sections: foods to avoid and foods to eat more of.

Splitting the steps keeps the classification grounded in the report's numbers, and it gives the second prompt a clean input. The app splits the second response on a separator token, so the summary and the diet plan render in separate panels.

## Files

| File | Purpose |
|---|---|
| `blood_work_analysis.ipynb` | Notebook prototype of the two-stage pipeline |
| `streamlit_app/app.py` | Streamlit app with an editable report and results panels |
| `blood_work.txt` | Sample report preloaded in the app |

## Run locally

```bash
uv run streamlit run blood_work_analyzer/streamlit_app/app.py
```

Needs `GOOGLE_API_KEY` in `.env` at the repo root. The app uses Gemma 4 through the Gemini API, and one analysis can take a minute or more.

This is a demo project and does not give medical advice.
