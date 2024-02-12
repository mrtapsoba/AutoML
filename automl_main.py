import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
from streamlit_option_menu import option_menu
import geopandas as gpd

#######################

st.set_page_config(
    page_title = "Auto ML by HAI",
    layout = "wide",
    initial_sidebar_state = "expanded"
)


with st.sidebar:
    st.title("Auto Machine Learning")
    selected_page = option_menu("Features", ["Data for study", "PreProcessing", 'Analisis', 'Machine Learning'], icons=['cloud'], menu_icon="", default_index=0)
    st.write("Halal Artificial Intelligence")


def data_for_study() :
    st.title("Data for study")
    col = st.columns(2)
    with col[0] :
        data_file = st.file_uploader("Chosse you data file (CSV only)")
    if(data_file):
        dataset = pd.read_csv(data_file)
        st.session_state['dataset'] = dataset
        with col[1]:
            st.write(f"Your Dataset has")
            st.markdown(f"### Rows: {len(dataset)} and Columns: {len(dataset.columns)}")
            selected_columns = st.multiselect("Choose the columns for study", dataset.columns)
        st.markdown("#### Preview of imported data")
        st.write("You can modify / update data directly here ")
            
        if(len(selected_columns) != 0):
            dataset_edited = st.data_editor(dataset[selected_columns])
        else:
            dataset_edited = st.data_editor(dataset)
        st.session_state['dataset_edited'] = dataset_edited
        return dataset_edited
    else:
        if 'dataset_edited' in st.session_state:
            with col[1]:
                dataset = st.session_state['dataset']
                st.write(f"Your Dataset has")
                st.markdown(f"### Rows: {len(dataset)} and Columns: {len(dataset.columns)}")
                selected_columns = st.multiselect("Choose the columns for study", dataset.columns)
            if(len(selected_columns) != 0):
                dataset_edited = st.data_editor(dataset[selected_columns])
            else:
                dataset_edited = st.data_editor(dataset)
            st.session_state['dataset_edited'] = dataset_edited
            # del st.session_state['dataset_edited']
        else:
            st.markdown("## Please import your data")
        return
    

if(selected_page == "Data for study"):
    data = data_for_study()
else:
    if('dataset_edited' not in st.session_state):
        st.write("No Data")
    else:
        if(selected_page == "PreProcessing"):
            #
            st.markdown("# PreProcessing")
        elif(selected_page == 'Analisis'):
            #
            st.markdown("# Analisis")
        elif(selected_page == 'Machine Learning'):
            #
            st.markdown("# Machine Learning")
    




