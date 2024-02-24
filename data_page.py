import streamlit as st
from st_aggrid import AgGrid
import ml_function as ftn
import data_explore_page as xplr
import pandas as pd

def data_for_study() :
    st.title("Data for study")
    col = st.columns(2)
    with col[0] :
        extention = st.selectbox("Choose File extention", ["CSV", "Excel", "Text"])
        data_file = st.file_uploader("Chosse you data file")
    with col[1]:
        if extention == "Excel" and data_file:
            df = pd.read_excel(data_file, sheet_name=None)
            sep = None
            sheet_name = st.selectbox("Choose Excel Sheet Name", df.keys())
        elif (extention == "CSV" or  extention == "Text") and data_file:
            sheet_name = None
            sep = st.selectbox("Choose Separator", ["Commas(,)", "Tabulation",  "Point-commas(;)"])
    if(data_file):
        dataset = ftn.get_data(data_file,extention = extention, sep=sep, sheet_name = sheet_name)
        st.session_state['dataset'] = dataset
        with col[1]:
            st.write(f"Your Dataset has")
            nbraw, nbcol = dataset.shape
            st.markdown(f"#### Rows: {nbraw} and Columns: {nbcol}")
            selected_columns = st.multiselect("Choose the columns for study", dataset.columns)
        
        st.markdown("#### Preview of imported data")
        st.write("You can modify / update data directly here in live")
        if(len(selected_columns) != 0):
            dataset_edited = AgGrid(dataset[selected_columns], editable=True, height= 650)
        else:
            dataset_edited = AgGrid(dataset, editable=True, height= 650)
        st.session_state['dataset_edited'] = dataset_edited["data"]
        return
    else:
        if 'dataset_edited' in st.session_state:
            dataset = st.session_state['dataset_edited']
            with col[1]:
                selected_columns = st.multiselect("Choose the columns for study", dataset.keys())
            st.markdown("### You have already import the data and this data is")
            st.write("You can modify / update data directly here in live")
            dataset_edited = AgGrid(dataset, editable=True, height= 650)
            st.session_state['dataset_edited'] = dataset_edited['data']
            # del st.session_state['dataset_edited']
        else:
            st.markdown("## Please import your data")
        return
