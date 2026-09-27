from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

APP_DIR = Path(__file__).parent
SAMPLE_REPORT = APP_DIR.parent / "blood_work.txt"
SECTION_SEPARATOR = "===DIET PLAN==="

load_dotenv(APP_DIR.parents[1] / ".env")

EXTRACTION_PROMPT = """
You are a medical data extraction assistant.

From the blood report below, extract ALL test values and classify each one as HIGH, LOW, or NORMAL
based on the reference ranges provided in the report.

Format your response as:
- Test Name: value | Status: HIGH/LOW/NORMAL | Reference: range

Blood Report:
{blood_report}
"""

DIET_PROMPT = """
You are a clinical nutritionist specializing in Indian dietary habits.

Based on the blood work analysis below, write:
1. A short health summary in 4-5 lines explaining the patient's condition in simple language
2. A short, practical Indian diet plan having only two sections (1) Foods to avoid (2) Foods to eat more of.
   Do not include any other sections in diet plan. Use a bold subheading and bullet points for each section.

Do not add a heading to the health summary or the diet plan. Put a line containing only
{separator} between the health summary and the diet plan.

Blood Work Analysis:
{extracted_values}
"""


@st.cache_resource
def get_llm():
    return ChatGoogleGenerativeAI(model="gemma-4-31b-it")


def analyze_blood_work(blood_report: str) -> tuple[str, str]:
    llm = get_llm()

    # Stage 1: extract values and classify each as HIGH / LOW / NORMAL
    extracted_values = llm.invoke(EXTRACTION_PROMPT.format(blood_report=blood_report)).text

    # Stage 2: health summary and Indian diet plan
    response = llm.invoke(
        DIET_PROMPT.format(extracted_values=extracted_values, separator=SECTION_SEPARATOR)
    ).text

    summary, _, diet_plan = response.partition(SECTION_SEPARATOR)
    return summary.strip(), diet_plan.strip()


st.set_page_config(page_title="Blood Work Analyzer", page_icon="🩸", layout="wide")
st.title("Blood Work Analyzer")

left, right = st.columns(2, gap="large")

with left:
    st.header("Blood Work Report")
    blood_report = st.text_area(
        "Blood work report",
        value=SAMPLE_REPORT.read_text(),
        height=620,
        label_visibility="collapsed",
    )
    analyze = st.button("Analyze", type="primary", disabled=not blood_report.strip())

if analyze:
    with right, st.spinner("Analyzing blood work..."):
        st.session_state["summary"], st.session_state["diet_plan"] = analyze_blood_work(blood_report)

with right:
    st.header("Health Summary")
    with st.container(border=True, height=240):
        st.markdown(st.session_state.get("summary", ""))

    st.header("Suggested Diet Plan")
    with st.container(border=True, height=420):
        st.markdown(st.session_state.get("diet_plan", ""))
