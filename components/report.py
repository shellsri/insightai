import io
import pandas as pd
import streamlit as st

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)


def generate_report(df):

    st.title("📄 Export Report")

    st.write(
        "Generate a professional PDF summary of your dataset."
    )

    if st.button("Generate PDF Report"):

        buffer = io.BytesIO()

        doc = SimpleDocTemplate(buffer)

        styles = getSampleStyleSheet()

        story = []

        story.append(
            Paragraph("<b>InsightAI Data Analytics Report</b>",
                      styles["Title"])
        )

        story.append(Spacer(1,20))

        story.append(
            Paragraph("<b>Dataset Summary</b>",
                      styles["Heading1"])
        )

        story.append(
            Paragraph(f"Rows : {df.shape[0]}",
                      styles["Normal"])
        )

        story.append(
            Paragraph(f"Columns : {df.shape[1]}",
                      styles["Normal"])
        )

        story.append(
            Paragraph(
                f"Missing Values : {int(df.isnull().sum().sum())}",
                styles["Normal"]
            )
        )

        story.append(
            Paragraph(
                f"Duplicate Rows : {int(df.duplicated().sum())}",
                styles["Normal"]
            )
        )

        story.append(Spacer(1,20))

        story.append(
            Paragraph(
                "<b>Columns</b>",
                styles["Heading1"]
            )
        )

        for col in df.columns:

            story.append(
                Paragraph(
                    f"{col} ({df[col].dtype})",
                    styles["Normal"]
                )
            )

        story.append(Spacer(1,20))

        story.append(
            Paragraph(
                "<b>Numerical Statistics</b>",
                styles["Heading1"]
            )
        )

        numeric = df.select_dtypes(include="number")

        if not numeric.empty:

            stats = numeric.describe().round(2)

            story.append(
                Paragraph(
                    stats.to_string().replace("\n","<br/>"),
                    styles["Code"]
                )
            )

        else:

            story.append(
                Paragraph(
                    "No numerical columns found.",
                    styles["Normal"]
                )
            )

        story.append(Spacer(1,20))

        story.append(
            Paragraph(
                "<b>Recommendations</b>",
                styles["Heading1"]
            )
        )

        if df.isnull().sum().sum() > 0:

            story.append(
                Paragraph(
                    "• Handle missing values before machine learning.",
                    styles["Normal"]
                )
            )

        if df.duplicated().sum() > 0:

            story.append(
                Paragraph(
                    "• Remove duplicate rows.",
                    styles["Normal"]
                )
            )

        story.append(
            Paragraph(
                "• Explore feature engineering for better model performance.",
                styles["Normal"]
            )
        )

        story.append(
            Paragraph(
                "• Visualize important variables before training models.",
                styles["Normal"]
            )
        )

        doc.build(story)

        pdf = buffer.getvalue()

        st.success("Report Generated Successfully!")

        st.download_button(
            "⬇ Download PDF",
            pdf,
            file_name="InsightAI_Report.pdf",
            mime="application/pdf"
        )