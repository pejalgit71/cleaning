import streamlit as st
import pandas as pd
from datetime import datetime

# Google Sheets setup (replace with actual setup)
# Make sure to use the gspread or pygsheets library to interact with Google Sheets
# Example: import gspread

# Define pages
st.sidebar.title("Cleaning/Cuci Service App")
page = st.sidebar.selectbox("Select Role", ["Customer", "Cleaner", "Admin"])

# Function to calculate cost
def calculate_cost(storey_type, areas):
    base_cost = 100 if storey_type == "Double Storey" else 50
    extra_areas = ['Kitchen', 'Garage']
    extra_cost = sum([30 for area in areas if area in extra_areas])
    total_cost = base_cost + extra_cost
    return total_cost

# Customer Page
if page == "Customer":
    st.title("Book a Cleaning Service")
    customer_name = st.text_input("Customer Name")
    contact_info = st.text_input("Contact Info")
    storey_type = st.selectbox("House Type", ["Single Storey", "Double Storey"])
    areas_to_clean = st.multiselect("Areas to Clean", ["Toilet", "Rooms", "Living Room", "Kitchen", "Garage"])

    if st.button("Submit Cleaning Request"):
        total_cost = calculate_cost(storey_type, areas_to_clean)
        # Google Sheets integration to save request
        st.success(f"Request submitted! Total cost: RM{total_cost}")

# Cleaner Page
if page == "Cleaner":
    st.title("Available Jobs")
    # Load jobs from Google Sheets (example)
    # jobs_df = pd.read_csv('jobs.csv')  # Replace with actual Google Sheets load
    jobs_df = pd.DataFrame({
        "Job ID": [1, 2],
        "Customer Name": ["John Doe", "Jane Smith"],
        "Areas to Clean": ["Toilet, Rooms", "Kitchen, Garage"],
        "Total Cost": [100, 130]
    })
    
    st.table(jobs_df)

    job_id = st.text_input("Enter Job ID to Accept")
    if st.button("Accept Job"):
        # Update Google Sheets with job assignment
        st.success(f"Job {job_id} accepted!")

    st.title("Upload Cleaning Photos")
    before_photo = st.file_uploader("Upload Before Cleaning Photo")
    after_photo = st.file_uploader("Upload After Cleaning Photo")

    if st.button("Submit Cleaning Photos"):
        # Save photos to database or cloud
        st.success("Photos submitted!")

# Admin Page
if page == "Admin":
    st.title("Admin Dashboard")
    # Display and manage customer and job data
    # Load from Google Sheets (replace with actual Sheets)
    st.write("Admin functionalities to manage customers, cleaners, and job requests.")

