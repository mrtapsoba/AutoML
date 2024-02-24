import pandas as pd
import streamlit as st
#from pandas_profiling import ProfileReport
#from streamlit_pandas_profiling import st_profile_report

def data_explore(data):
    explore = st.selectbox("Choose the exploring", ["Descriptive analisis", "Graphic"])
    #penguin_profile = ProfileReport(data, explorative=True)
    #st_profile_report(penguin_profile)
