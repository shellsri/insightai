import streamlit as st
import pandas as pd
import plotly.express as px


def show_charts(df):

    st.title("📈 Interactive Visualizations")

    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    categorical_cols = df.select_dtypes(exclude="number").columns.tolist()

    if len(df.columns) == 0:
        st.warning("Dataset has no columns.")
        return

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "📊 Distribution",
            "📦 Box Plot",
            "🔥 Correlation",
            "🥧 Categorical"
        ]
    )

    # -------------------------------------------------------
    # Distribution
    # -------------------------------------------------------

    with tab1:

        if numeric_cols:

            column = st.selectbox(
                "Select Numeric Column",
                numeric_cols,
                key="hist"
            )

            fig = px.histogram(
                df,
                x=column,
                nbins=30,
                title=f"Distribution of {column}"
            )

            fig.update_layout(
                template="plotly_white",
                height=500
            )

            st.plotly_chart(
                fig,
                width="stretch"
            )

        else:

            st.info("No numeric columns found.")

    # -------------------------------------------------------
    # Box Plot
    # -------------------------------------------------------

    with tab2:

        if numeric_cols:

            column = st.selectbox(
                "Numeric Column",
                numeric_cols,
                key="box"
            )

            fig = px.box(
                df,
                y=column,
                title=f"Outlier Detection : {column}"
            )

            fig.update_layout(
                template="plotly_white",
                height=500
            )

            st.plotly_chart(
                fig,
                width="stretch"
            )

        else:

            st.info("No numeric columns found.")

    # -------------------------------------------------------
    # Correlation Heatmap
    # -------------------------------------------------------

    with tab3:

        if len(numeric_cols) >= 2:

            corr = df[numeric_cols].corr()

            fig = px.imshow(
                corr,
                text_auto=".2f",
                aspect="auto",
                color_continuous_scale="Blues",
                title="Correlation Heatmap"
            )

            fig.update_layout(height=650)

            st.plotly_chart(
                fig,
                width="stretch"
            )

        else:

            st.info("Need at least 2 numeric columns.")

    # -------------------------------------------------------
    # Pie Chart
    # -------------------------------------------------------

    with tab4:

        if categorical_cols:

            column = st.selectbox(
                "Categorical Column",
                categorical_cols,
                key="pie"
            )

            counts = (
                df[column]
                .value_counts()
                .reset_index()
            )

            counts.columns = [
                column,
                "Count"
            ]

            fig = px.pie(
                counts,
                names=column,
                values="Count",
                title=f"{column} Distribution"
            )

            fig.update_layout(height=550)

            st.plotly_chart(
                fig,
                width="stretch"
            )

        else:

            st.info("No categorical columns found.")

    st.divider()

    st.subheader("📄 Dataset Preview")

    rows = st.slider(
        "Rows to Display",
        5,
        min(100, len(df)),
        10
    )

    st.dataframe(
        df.head(rows),
        width="stretch",
        hide_index=True
    )