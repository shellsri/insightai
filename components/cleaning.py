import streamlit as st
import pandas as pd


def show_cleaning(df):

    st.title("🧹 Data Cleaning")

    cleaned_df = df.copy()

    st.markdown("### Dataset Health")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Missing Values",
        int(cleaned_df.isnull().sum().sum())
    )

    c2.metric(
        "Duplicate Rows",
        int(cleaned_df.duplicated().sum())
    )

    c3.metric(
        "Columns",
        cleaned_df.shape[1]
    )

    st.divider()

    st.subheader("Missing Values by Column")

    missing = cleaned_df.isnull().sum()

    missing = missing[missing > 0]

    if missing.empty:

        st.success("🎉 No missing values found!")

    else:

        st.dataframe(
            missing.reset_index().rename(
                columns={
                    "index": "Column",
                    0: "Missing Values"
                }
            ),
            width="stretch",
            hide_index=True
        )

    st.divider()

    st.subheader("Cleaning Options")

    remove_duplicates = st.checkbox("Remove Duplicate Rows")

    fill_numeric = st.selectbox(
        "Fill Missing Numeric Values",
        [
            "Do Nothing",
            "Mean",
            "Median",
            "Zero"
        ]
    )

    fill_categorical = st.selectbox(
        "Fill Missing Categorical Values",
        [
            "Do Nothing",
            "Mode",
            "Unknown"
        ]
    )

    if st.button("🚀 Apply Cleaning"):

        if remove_duplicates:
            cleaned_df = cleaned_df.drop_duplicates()

        numeric_cols = cleaned_df.select_dtypes(include="number").columns

        categorical_cols = cleaned_df.select_dtypes(exclude="number").columns

        if fill_numeric == "Mean":

            for col in numeric_cols:
                cleaned_df[col] = cleaned_df[col].fillna(
                    cleaned_df[col].mean()
                )

        elif fill_numeric == "Median":

            for col in numeric_cols:
                cleaned_df[col] = cleaned_df[col].fillna(
                    cleaned_df[col].median()
                )

        elif fill_numeric == "Zero":

            for col in numeric_cols:
                cleaned_df[col] = cleaned_df[col].fillna(0)

        if fill_categorical == "Mode":

            for col in categorical_cols:
                if not cleaned_df[col].mode().empty:
                    cleaned_df[col] = cleaned_df[col].fillna(
                        cleaned_df[col].mode()[0]
                    )

        elif fill_categorical == "Unknown":

            for col in categorical_cols:
                cleaned_df[col] = cleaned_df[col].fillna("Unknown")

        st.success("✅ Cleaning Applied Successfully")

        st.subheader("Cleaned Dataset Preview")

        st.dataframe(
            cleaned_df.head(),
            width="stretch"
        )

        csv = cleaned_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            "⬇ Download Cleaned Dataset",
            csv,
            file_name="cleaned_dataset.csv",
            mime="text/csv"
        )