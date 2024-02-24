from st_aggrid import AgGrid
import pandas as pd
import plotly.express as px
import requests
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_lottie import st_lottie
from streamlit_pandas_profiling import st_profile_report
from streamlit_plotly_events import plotly_events

df = pd.read_excel(r'C:\Users\Mr TAPS\Documents\Python Scripts\Halal Artificial Intelligence\AutoML\data_test\Donnees_deplaces_inter.xlsx', sheet_name="Centre")
penguin_profile = ProfileReport(df, explorative=True)
st_profile_report(penguin_profile)
