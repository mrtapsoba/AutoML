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
        #columns_to_drop = [col for col in dataset.columns if 'Unnamed' in col]
        #dataset = dataset.drop(columns=columns_to_drop)
        st.session_state['dataset'] = dataset
        with col[1]:
            st.write(f"Your Dataset has")
            nbraw, nbcol = dataset.shape
            st.markdown(f"#### Rows: {nbraw} and Columns: {nbcol}")
            selected_columns = st.multiselect("Choose the columns for study", dataset.columns)
        
        st.markdown("#### Preview of imported data")
        st.write("You can modify / update data directly here in live")
        if st.button("Edit data"):
            if(len(selected_columns) != 0):
                dataset_edited = AgGrid(dataset[selected_columns], editable=True, height= 650)
            else:
                dataset_edited = AgGrid(dataset, editable=True, height= 650)
            st.session_state['dataset_edited'] = dataset_edited["data"]
        else :
            if(len(selected_columns) != 0):
                dataset_edited = dataset[selected_columns]
                st.dataframe(dataset[selected_columns].head())
            else :
                dataset_edited = dataset
                st.dataframe(dataset.head())
            st.session_state['dataset_edited'] = dataset_edited
        return
    else:
        if 'dataset_edited' in st.session_state:
            dataset = st.session_state['dataset_edited']
            with col[1]:
                selected_columns = st.multiselect("Choose the columns for study", dataset.keys())
            st.markdown("### You have already import the data and this data is")
            st.write("You can modify / update data directly here in live")
            if st.button("Edit data"):
                dataset_edited = AgGrid(dataset, editable=True, height= 650)
                st.session_state['dataset_edited'] = dataset_edited['data']
            else :
                dataset_edited = dataset
                st.dataframe(dataset.head())
            # del st.session_state['dataset_edited']
        else:
            st.markdown("## Please import your data")
            m = st.columns((1,1.2,1.2))
            with m[0]:
                st.image("https://i.pinimg.com/564x/78/a9/fb/78a9fba0b7d02d1f07b74be1bd777656.jpg", caption="CSV File")
            with m[1]:
                st.image("https://i.pinimg.com/564x/7b/a5/69/7ba569f82b3d3b0c18fc7b43399e3d67.jpg", caption="Data in CSV, Excel, Text")
            with m[2]:
                st.image("https://i.pinimg.com/564x/c8/68/c8/c868c8dc77e7c068b64575a8c48453a6.jpg", caption="Excel File")
        return
