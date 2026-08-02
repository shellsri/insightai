import streamlit as st
import pandas as pd

# ================= IMPORT COMPONENTS =================

from components.dashboard import show_dashboard
from components.charts import show_charts
from components.ai_insights import generate_ai_insights
from components.cleaning import show_cleaning
from components.chat import show_chat
# ================= LOAD CSS =================

def load_css():
    with open("assets/style.css", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True,
        )

# ================= PAGE CONFIG =================

st.set_page_config(
    page_title="InsightAI",
    page_icon="📊",
    layout="wide",
)

load_css()

# ================= HERO =================

st.title("📊 InsightAI")
st.caption("AI-Powered Data Analytics Workspace")

st.write(
    """
Upload a **CSV** or **Excel** dataset and instantly clean, visualize,
analyze, chat with your data, generate AI insights, and export a report.
"""
)

st.divider()

# ================= FILE UPLOADER =================

uploaded_file = st.file_uploader(
    "Upload Dataset",
    type=["csv", "xlsx"],
)

if uploaded_file is None:
    st.info("👆 Upload a dataset to begin.")
    st.stop()

# ================= LOAD DATA =================

try:
    if uploaded_file.name.lower().endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

except Exception as e:
    st.error(f"Unable to read file.\n\n{e}")
    st.stop()

# ================= SUCCESS =================

st.success("✅ Dataset Loaded Successfully")

# ================= DATASET METRICS =================

rows = df.shape[0]
cols = df.shape[1]
missing = int(df.isnull().sum().sum())
duplicates = int(df.duplicated().sum())

memory = round(
    df.memory_usage(deep=True).sum() / 1024,
    1
)

quality = round((1 - missing / (rows * cols)) * 100, 1) if rows * cols > 0 else 0.0

st.subheader("Workspace Overview")

c1, c2, c3, c4, c5, c6 = st.columns(6)

c1.metric("Rows", f"{rows:,}")
c2.metric("Columns", cols)
c3.metric("Missing", missing)
c4.metric("Duplicates", duplicates)
c5.metric("Memory", f"{memory} KB")
c6.metric("Quality", f"{quality}%")

st.divider()

# ================= TABS =================

overview_tab, chart_tab, ai_tab, cleaning_tab, chat_tab, report_tab = st.tabs(
    [
        "📊 Overview",
        "📈 Charts",
        "🧹 Cleaning",
        "💬 Chat",
        "📄 Report",
    ]
)

# ================= OVERVIEW =================

with overview_tab:
    show_dashboard(df)

# ================= CHARTS =================

with chart_tab:
    show_charts(df)

# ================= AI =================


# ================= CLEANING =================

with cleaning_tab:
    show_cleaning(df)

# ================= CHAT =================

with chat_tab:
    show_chat(df)

# ================= REPORT =================

with report_tab:
    generate_report(df)