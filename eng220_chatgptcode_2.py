# -*- coding: utf-8 -*-
"""eng220_chatgptcode_2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gZLD3KsrQUIy9pargVPX6PZvUagAYREz
"""

import streamlit as st
import pandas as pd
import altair as alt

# Set the page title
st.title("CSV Data Graphing App")

# Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
#uploaded_file = "C:\Users\skeeb\OneDrive\Desktop\School\UNM\PENG\FlowData-2024-11-12.csv"

if uploaded_file:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)

    st.write("### Data Preview")
    st.write(df.head())

    # Select numeric columns for graphing
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

    if len(numeric_cols) >= 2:
        x_axis = st.selectbox("Select X-axis", numeric_cols)
        y_axis = st.selectbox("Select Y-axis", numeric_cols)

        # Select chart type
        chart_type = st.radio("Select Chart Type", ["Scatterplot", "Line Chart", "Bar Chart"])

        # Create chart
        if chart_type == "Scatterplot":
            chart = alt.Chart(df).mark_circle(size=60).encode(
                x=x_axis,
                y=y_axis,
                tooltip=[x_axis, y_axis]
            ).interactive()
        elif chart_type == "Line Chart":
            chart = alt.Chart(df).mark_line().encode(
                x=x_axis,
                y=y_axis,
                tooltip=[x_axis, y_axis]
            ).interactive()
        elif chart_type == "Bar Chart":
            chart = alt.Chart(df).mark_bar().encode(
                x=x_axis,
                y=y_axis,
                tooltip=[x_axis, y_axis]
            ).interactive()

        st.altair_chart(chart, use_container_width=True)
    else:
        st.write("The uploaded file must contain at least two numeric columns for visualization.")
else:
    st.write("Please upload a CSV file to get started.")
