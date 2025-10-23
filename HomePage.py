# This creates the main landing page for the Streamlit application.
# Contains an introduction to the project and guide users to other pages.

import streamlit as st

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Homepage",
    page_icon="🏠",
)

# PAGE TITLE
st.title("CS 1301 - Data Dashboard 📊")

# INTRODUCTION
st.write("""
Welcome to the **Data Dashboard**, a Streamlit web application created as part of **CS 1301: Introduction to Computing (Lab 2)**.

This project demonstrates how Python can be used to collect, organize, and visualize data in a web-based environment.
""")

# HOW TO USE SECTION
st.subheader("How to Use This Application")
st.write("""
Use the sidebar on the left to move between sections of the app:

- **Survey Page:** Enter new data to be stored in the CSV file.
- **Visuals Page:** View the data displayed through various charts and graphs.
""")

# ABOUT THE PROJECT SECTION
st.subheader("About This Project")
st.write("""
This project was developed to explore how user input, data storage, and visualizations can work together inside a single Python web application.

The app uses **Streamlit** to handle the user interface, **Pandas** for managing datasets, and **Altair** for generating interactive graphs.  
Together, these tools provide a practical example of how Python can be used for both programming logic and web-based presentation.
""")

# PROJECT PURPOSE SECTION
st.subheader("Learning Goals")
st.write("""
By completing this lab, students will gain experience with:
- Building simple web apps in Python.
- Handling and saving user input data.
- Displaying information through interactive charts.
""")

# OPTIONAL IMAGE SECTION
# To include an image:
# 1. Create an 'images' folder in the same directory as this file.
# 2. Add your image file (e.g., 'dashboard_banner.png') inside that folder.
# 3. Uncomment the line below and update the file name if needed.
#
# st.image("images/dashboard_banner.png", caption="CS 1301 - Data Dashboard", use_column_width=True)

# CREDITS
st.divider()
st.caption("Developed by Braden Baro for CS 1301, Fall 2025.")
