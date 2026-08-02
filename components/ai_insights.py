import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if api_key:
    genai.configure(api_key=api_key)


def generate_ai_insights(df):

    st.title("🤖 AI Executive Analytics")

    if not api_key:
        st.error("GOOGLE_API_KEY not found in .env")
        return

    if st.button("🚀 Generate AI Report", use_container_width=True):

        with st.spinner("Analyzing dataset with Gemini..."):

            summary = f"""
Dataset Shape:
Rows: {df.shape[0]}
Columns: {df.shape[1]}

Column Names:
{list(df.columns)}

Data Types:
{df.dtypes.to_string()}

Missing Values:
{df.isnull().sum().to_string()}

Duplicate Rows:
{df.duplicated().sum()}

Numerical Statistics:
{df.describe().to_string()}

Sample Data:
{df.head(10).to_string()}
"""

            prompt = f"""
You are a Senior Data Scientist with expertise in analytics,
business intelligence, machine learning and AI.

Analyze the dataset below and generate a professional report.

{summary}

Return your answer in EXACTLY the following format.

# Executive Summary

Explain what this dataset is about.

---

# Dataset Health Score

Give a score out of 100.

Explain why.

---

# Data Quality Issues

Mention

- Missing Values
- Duplicate Rows
- Outliers
- Constant Columns
- Data Imbalance

---

# Business Insights

Give 5 important insights.

---

# Machine Learning Readiness

Mention

Target column candidates

Problem Type

Classification

Regression

Clustering

Recommendation

---

# Feature Engineering Ideas

Suggest useful new features.

---

# Recommended Algorithms

Recommend suitable ML algorithms.

Explain why.

---

# Data Cleaning Recommendations

List preprocessing steps.

---

# Next Steps

Give an ordered roadmap.
"""

            model = genai.GenerativeModel("gemini-2.5-flash-lite")

            response = model.generate_content(prompt)

        st.success("Analysis Complete")

        st.markdown(response.text)