# This creates the page for users to input data.
# The collected data should be appended to the 'data.csv' file.

import streamlit as st
import pandas as pd
import os
from datetime import datetime

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Survey",
    page_icon="📝",
)

# PAGE TITLE AND DESCRIPTION
st.title("Data Collection Survey 📝")
st.write("Please fill out the form below to record your data entry. The information you provide will be added to the dataset for visualization.")

# FORM SECTION
with st.form("survey_form"):
    category_input = st.text_input("Enter a category:")
    value_input = st.text_input("Enter a value:")
    submitted = st.form_submit_button("Submit Data")

    if submitted:
        csv_path = os.path.join(os.path.dirname(__file__), "..", "data.csv")
        new_row = pd.DataFrame([{
            "timestamp": datetime.now().isoformat(),
            "category": category_input.strip(),
            "value": value_input.strip()
        }])

        if os.path.exists(csv_path):
            existing_df = pd.read_csv(csv_path)
            updated_df = pd.concat([existing_df, new_row], ignore_index=True)
        else:
            updated_df = new_row

        updated_df.to_csv(csv_path, index=False)
        st.success("Your data has been saved successfully.")
        st.write(f"Category: **{category_input}**, Value: **{value_input}**")

# DISPLAY CURRENT DATA
st.divider()
st.header("Current Data in CSV")

csv_display_path = os.path.join(os.path.dirname(__file__), "..", "data.csv")
if os.path.exists(csv_display_path) and os.path.getsize(csv_display_path) > 0:
    df = pd.read_csv(csv_display_path)
    st.dataframe(df)
else:
    st.warning("The 'data.csv' file is empty or does not exist yet.")
