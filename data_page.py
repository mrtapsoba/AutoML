import streamlit as st
import ml_function as ftn

def data_for_study() :
    st.title("Data for study")
    col = st.columns(2)
    with col[0] :
        data_file = st.file_uploader("Chosse you data file (CSV only)")
    with col[1]:
        sep = st.selectbox("Choose Separator", ["Commas(,)", "Tabulation",  "Point-commas(;)"])
    if(data_file and sep):
        dataset = ftn.get_data(data_file, sep=sep)
        st.session_state['dataset'] = dataset
        with col[1]:
            st.write(f"Your Dataset has")
            nbraw, nbcol = dataset.shape
            st.markdown(f"### Rows: {nbraw} and Columns: {nbcol}")
            selected_columns = st.multiselect("Choose the columns for study", dataset.columns)
        
        st.markdown("#### Preview of imported data")
        st.write("You can modify / update data directly here in live")
            
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
                selected_columns = st.multiselect("Choose the columns for study (all by default)", dataset.columns)
            if(len(selected_columns) != 0):
                dataset_edited = st.data_editor(dataset[selected_columns])
            else:
                dataset_edited = st.data_editor(dataset)
            st.session_state['dataset_edited'] = dataset_edited
            # del st.session_state['dataset_edited']
        else:
            st.markdown("## Please import your data")
        return
