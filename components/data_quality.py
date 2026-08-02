import streamlit as st
import pandas as pd


def show_data_quality(df):

    st.title("🩺 Dataset Health Report")

    total_rows = df.shape[0]
    total_cols = df.shape[1]

    missing = df.isnull().sum()
    duplicates = df.duplicated().sum()

    numeric = df.select_dtypes(include="number")
    categorical = df.select_dtypes(exclude="number")

    st.subheader("Overall Dataset")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Rows", total_rows)
    c2.metric("Columns", total_cols)
    c3.metric("Missing", int(missing.sum()))
    c4.metric("Duplicates", int(duplicates))

    st.divider()

    st.subheader("Column Health")

    report = []

    for col in df.columns:

        dtype = str(df[col].dtype)

        miss = int(df[col].isnull().sum())

        unique = int(df[col].nunique())

        percent_missing = round((miss / total_rows) * 100, 2)

        recommendation = "Good"

        if percent_missing > 40:
            recommendation = "⚠ Consider removing"

        elif percent_missing > 0:
            recommendation = "Fill Missing Values"

        elif unique == 1:
            recommendation = "Drop Constant Column"

        report.append({

            "Column": col,
            "Type": dtype,
            "Missing": miss,
            "Missing %": percent_missing,
            "Unique": unique,
            "Recommendation": recommendation

        })

    report_df = pd.DataFrame(report)

    st.dataframe(
        report_df,
        width="stretch",
        hide_index=True
    )

    st.divider()

    st.subheader("AI-style Recommendations")

    if duplicates > 0:
        st.warning(f"• Remove {duplicates} duplicate rows.")

    if missing.sum() > 0:
        st.warning("• Handle missing values before training ML models.")

    if numeric.empty:
        st.info("• Dataset contains no numeric columns.")

    if categorical.empty:
        st.info("• Dataset contains no categorical columns.")

    high_missing = report_df[report_df["Missing %"] > 40]

    if not high_missing.empty:

        st.error(
            "Columns with excessive missing values:\n\n"
            + ", ".join(high_missing["Column"])
        )

    low_unique = report_df[report_df["Unique"] == 1]

    if not low_unique.empty:

        st.error(
            "Constant columns detected:\n\n"
            + ", ".join(low_unique["Column"])
        )

    st.success("Dataset health analysis completed.")