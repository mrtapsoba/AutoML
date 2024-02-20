import streamlit as st
import altair as alt
import plotly.express as px
from streamlit_option_menu import option_menu
import geopandas as gpd
import home_page as hmpg
import data_page as dtpg
import pre_page as prpg

#######################
st.set_page_config(
    page_title = "Free ML by HAI",
    layout = "wide",
    initial_sidebar_state = "expanded",
    page_icon="🧊"
)

with st.sidebar:
    st.title("Free Machine Learning")
    selected_page = option_menu("Main menu", ["About Project", "Data for study", "Data Exploring", "PreProcessing", 'Machine Learning'], icons=['house', 'cloud'], menu_icon="", default_index=0)
    st.title("Halal Artificial Intelligence")
    
# Page for present projet
if(selected_page == "About Project"):
    hmpg.home_page()
else:
    # Page for get data
    if(selected_page == "Data for study"):
        data = dtpg.data_for_study()
    else:
        # Missing data
        if('dataset_edited' not in st.session_state):
            hmpg.no_data()
        else:
            # Page for exploring data
            if(selected_page == 'Data Exploring'):
                #
                st.markdown("# Data Exploring")
            # Page for prepreocessing data
            elif(selected_page == "PreProcessing"):
                #
                prpg.pre_processing(st.session_state['dataset_edited'])
            # Page for training data
            elif(selected_page == 'Machine Learning'):
                #
                st.markdown("# Machine Learning")