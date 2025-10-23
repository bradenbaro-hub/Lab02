# This creates the page for displaying data visualizations.
# It should read data from both 'data.csv' and 'data.json' to create graphs.


import streamlit as st
import pandas as pd
import json
import os
import altair as alt

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visualizations",
    page_icon="📈",
)

# PAGE TITLE AND INTRO
st.title("Data Visualizations 📈")
st.write("This page shows graphs based on the data collected through the survey and the sample JSON file.")

# LOAD DATA SECTION
st.divider()
st.header("Load Data")

csv_path = os.path.join(os.path.dirname(__file__), "..", "data.csv")
json_path = os.path.join(os.path.dirname(__file__), "..", "data.json")

# Load CSV
if os.path.exists(csv_path):
    try:
        df = pd.read_csv(csv_path)
        st.success("Loaded data.csv successfully.")
        st.dataframe(df.head())
    except Exception as e:
        st.error(f"Error loading CSV: {e}")
        df = pd.DataFrame()
else:
    st.warning("data.csv not found.")
    df = pd.DataFrame()

# Load JSON
if os.path.exists(json_path):
    try:
        with open(json_path, "r") as f:
            js = json.load(f)
        st.success("Loaded data.json successfully.")
        st.json(js)
    except Exception as e:
        st.error(f"Error loading JSON: {e}")
        js = {}
else:
    st.warning("data.json not found.")
    js = {}

# GRAPH SECTION
st.divider()
st.header("Graphs")

# GRAPH 1 - STATIC (JSON)
st.subheader("Graph 1: Static — Data Points from JSON")
try:
    if "data_points" in js:
        json_df = pd.DataFrame(js["data_points"])
        st.bar_chart(json_df.set_index("label")["value"])
        st.caption("This static bar chart displays the data points defined in data.json.")
    else:
        st.warning("The JSON file does not contain a 'data_points' list.")
except Exception as e:
    st.error(f"Error displaying static graph: {e}")

# GRAPH 2 - DYNAMIC (CSV)
st.subheader("Graph 2: Dynamic — Values by Category (CSV data)")
if "category" in df.columns and not df.empty:
    categories = df["category"].dropna().unique().tolist()
    selected_category = st.selectbox("Select a category to view:", categories)
    if "selected_category" not in st.session_state:
        st.session_state.selected_category = selected_category
    st.session_state.selected_category = selected_category

    filtered_df = df[df["category"] == st.session_state.selected_category]
    try:
        filtered_df["value"] = pd.to_numeric(filtered_df["value"], errors="coerce")
        filtered_df = filtered_df.dropna(subset=["value"])
        st.line_chart(filtered_df["value"])
        st.caption("This line chart updates automatically based on the selected category.")
    except Exception as e:
        st.error(f"Error creating dynamic line graph: {e}")
else:
    st.info("No categories found in data.csv. Please add data on the Survey page.")

# GRAPH 3 - DYNAMIC WITH FILTER (CSV)
st.subheader("Graph 3: Dynamic — Filtered Scatter Plot")
if not df.empty and "value" in df.columns:
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    df = df.dropna(subset=["value"])
    if not df.empty:
        min_val = int(df["value"].min())
        max_val = int(df["value"].max())
        low, high = st.slider("Filter value range:", min_val, max_val, (min_val, max_val))

        if "filter_range" not in st.session_state:
            st.session_state.filter_range = (low, high)
        st.session_state.filter_range = (low, high)

        filtered = df[
            (df["value"] >= st.session_state.filter_range[0]) &
            (df["value"] <= st.session_state.filter_range[1])
        ]

        if not filtered.empty:
            chart = alt.Chart(filtered).mark_circle(size=70).encode(
                x="timestamp",
                y="value",
                tooltip=["category", "value"]
            ).interactive()
            st.altair_chart(chart, use_container_width=True)
            st.caption("Each point represents one entry. Adjust the slider to filter results.")
        else:
            st.info("No data within the selected range.")
    else:
        st.warning("No numeric values available for visualization.")
else:
    st.warning("The 'data.csv' file is missing or empty.")
