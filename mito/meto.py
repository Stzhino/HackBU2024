import streamlit as st
from mitosheet.streamlit.v1 import spreadsheet
import pandas as pd
import os 
from st_on_hover_tabs import on_hover_tabs

st.set_page_config(layout="wide")

st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)

with st.sidebar:
    tabs = on_hover_tabs(tabName=['Home', 'Finance', 'Groups'], 
                        iconName=['home', 'money', 'apps'], default_choice=0)
    
st.title("Member Information")
st.write("Import member/event data in the form of a csv file in a spreadsheet format with sorting tools available.")
st.divider()

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True) # Allow user to add more files to the program
st.caption("Add more files by importing files above")

if uploaded_files is not None:
    for uploaded_file in uploaded_files:
        file_name = uploaded_file.name
        target_path = "./import_files/" + file_name  # Specify target folder and filename

        try:
            with open(target_path, "wb") as f:  # Open in binary mode for CSV files
                f.write(uploaded_file.getbuffer())
            st.success("File uploaded successfully: " + file_name)
        except Exception as e:
            st.error(f"Error saving file: {e}")

import_folder = "./import_files"  # Use the folder where you saved the uploaded files
new_dfs, usrdata = spreadsheet(import_folder=import_folder)

