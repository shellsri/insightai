import streamlit as st
import pandas as pd


def show_dashboard(df):

    st.markdown("## 📊 Dataset Overview")

    rows = df.shape[0]
    cols = df.shape[1]
    missing = df.isnull().sum().sum()
    duplicate = df.duplicated().sum()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Rows", f"{rows:,}")
    c2.metric("Columns", cols)
    c3.metric("Missing Values", missing)
    c4.metric("Duplicate Rows", duplicate)

    st.divider()

    st.subheader("Dataset Preview")

    st.dataframe(
        df.head(10),
        width="stretch",
        hide_index=True
    )

    st.divider()

    st.subheader("Column Information")

    info = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str),
        "Missing Values": df.isnull().sum().values,
        "Unique Values": df.nunique().values
    })

    st.dataframe(
        info,
        width="stretch",
        hide_index=True
    )

    st.divider()

    st.subheader("Numerical Statistics")

    numeric_df = df.select_dtypes(include="number")

    if not numeric_df.empty:
        st.dataframe(
            numeric_df.describe(),
            width="stretch"
        )

    st.subheader("Categorical Statistics")

    categorical_df = df.select_dtypes(exclude="number")

    if not categorical_df.empty:
        cat_summary = pd.DataFrame({
            "Column": categorical_df.columns,
            "Unique Values": categorical_df.nunique().values,
            "Most Frequent": categorical_df.mode().iloc[0].values,
            "Missing": categorical_df.isnull().sum().values
        })

        st.dataframe(
            cat_summary,
            width="stretch"
        )