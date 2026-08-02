# 📊 InsightAI

> AI-Powered Data Analytics Platform built with Streamlit, Python, Plotly, and Google Gemini.

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🚀 Overview

InsightAI is an intelligent data analytics platform that enables users to upload datasets and instantly explore, clean, visualize, analyze, and generate AI-powered business insights.

Designed to simplify exploratory data analysis (EDA), InsightAI combines traditional analytics with Large Language Models (LLMs) to help users understand datasets without writing code.

---

## ✨ Features

### 📂 Dataset Upload
- Upload CSV files
- Upload Excel (.xlsx) files
- Automatic dataset loading

### 📊 Dashboard
- Dataset overview
- Number of rows & columns
- Missing values
- Duplicate rows
- Memory usage
- Data quality score

### 📈 Interactive Visualizations
- Histogram
- Box Plot
- Correlation Heatmap
- Scatter Plot
- Line Chart
- Pie Chart
- Bar Chart

Built using Plotly for fully interactive charts.

### 🧹 Data Cleaning
- Missing value detection
- Duplicate detection
- Column information
- Numerical statistics
- Categorical statistics

### 🤖 AI Insights
Powered by Google Gemini.

Generates:
- Executive Summary
- Business Insights
- Data Quality Analysis
- Recommendations
- Dataset Understanding

### 💬 AI Chat
Chat with your dataset using natural language.

Example questions:

- Which columns have missing values?
- Summarize this dataset.
- What preprocessing is recommended?
- Explain important trends.

### 📄 PDF Report Export

Generate a downloadable report containing:

- Dataset Summary
- Column Information
- Numerical Statistics
- Data Quality Metrics
- Recommendations

---

# 🛠 Tech Stack

## Frontend

- Streamlit

## Backend

- Python

## Data Processing

- Pandas
- NumPy

## Visualization

- Plotly

## AI

- Google Gemini API

## PDF Generation

- ReportLab

---

# 📁 Project Structure

```
InsightAI/
│
├── app.py
├── requirements.txt
├── README.md
│
├── assets/
│   └── style.css
│
├── components/
│   ├── dashboard.py
│   ├── charts.py
│   ├── cleaning.py
│   ├── ai_insights.py
│   ├── chat.py
│   └── report.py
│
├── utils/
│
└── sample_data/
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/shellsri/InsightAI.git

cd InsightAI
```

Create a virtual environment

```bash
python -m venv venv
```

Activate

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
streamlit run app.py
```

---

# 🔑 Environment Variables

Create a `.env` file.

```
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

# 📌 Future Improvements

- Automated anomaly detection
- Machine learning model recommendations
- Time series forecasting
- Predictive analytics
- SQL database connectivity
- Multi-file analysis
- Team collaboration
- Dashboard sharing

---

# 🎯 Use Cases

- Business Analytics
- Exploratory Data Analysis (EDA)
- Academic Projects
- Data Cleaning
- AI-assisted Dataset Understanding
- Business Intelligence
- Rapid Data Exploration

---

# 👨‍💻 Author

**Shelly Srivastava**

GitHub:
https://github.com/shellsri

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
