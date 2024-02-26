import ml_function as ftn
import streamlit as st
import pandas as pd

def pre_processing(data):
    if 'pre_history' in st.session_state:
        hisories = st.session_state['pre_history']
    else :
        hisories = []
    st.title("PreProcessing")
    tasks_list = ['Data cleaning', 'Data Transformation', 'Data Reduction', 'Code Myself']
    col = st.columns((2.5,1))
    with col[0]:
        task = st.selectbox("Choose a preprocessing task", tasks_list)
        st.write("Small message which explain the task")
        st.divider()
        if task == "Data cleaning":
            col2 = st.columns(2)
            with col2[0]:
                clean_data = st.selectbox("Choose type data", ["Missing data", "Aberrante"])
            with col2[1]:
                clean_type = st.selectbox("Choose clean data", ["Delete it", "Replace it"])
            if(clean_type == "Replace it"):
                with col2[0]:
                    new_data = st.selectbox("Replace by", ["Mean", "Median", "Quartile", "Custom"])
                    custom = None
                    if(new_data == "Other value"):
                        with col2[1]:
                            custom = st.text_input("New value")
            variables = st.multiselect("Choose the variables to update", data.keys())

            if(st.button("Apply")):
                if clean_data == "Missing data" and clean_type == "Delete it":
                    data = ftn.clean_missing(data, variables= variables)
                    hisories.append(f"{clean_data} {clean_type} -- {variables}")
                elif clean_data == "Missing data" and clean_type == "Replace it":
                    data = ftn.replace_missing_values(data, variables, method=new_data, custom_value=custom)
                    hisories.append(f"{clean_data} {clean_type} -- {variables} - {new_data} {custom}")
                st.session_state['dataset_edited'] = data
                st.session_state['pre_history'] = hisories
                st.success("Cleaning with succes")

        elif task == "Data Transformation":
            col2 = st.columns(2)
            with col2[0]:
                transformation = st.selectbox("choose the transformation", ["Reset index", "Normalization", "Encodage"])
                if transformation == "Reset index":
                    st.write("Just apply please")
                elif transformation == "Normalization":
                    with col2[1]:
                        normalization = st.selectbox("choose the normalization", ["Standard", "MinMax", "Robust"])
                elif transformation == "Encodage":
                    with col2[1]:
                        encodage = st.selectbox("choose the encodage", ["Label", "OneHot"])
            if transformation != "Reset index":
                variables = st.multiselect("Choose the variables to transform", data.keys())
            if(st.button("Apply")):
                if transformation == "Reset index":
                    data = ftn.reset_index(data)
                    hisories.append(f"{transformation} ")
                elif transformation == "Normalization":
                    data = ftn.normalize_data(data, variables, method=normalization)
                    hisories.append(f"{transformation} {normalization} -- {variables}")
                elif transformation == "Encodage":
                    data = ftn.encode_data(data, variables, method=encodage)
                    hisories.append(f"{transformation} {encodage} -- {variables}")
                st.session_state['dataset_edited'] = data
                st.session_state['pre_history'] = hisories
                st.success("Transform with succes")

        elif task == "Code Myself":
            mycode = st.text_area("Write your code in Python")
            if(mycode != None):
                st.write("See your code")
                st.code(mycode)
                if(st.button("Apply")):
                    exec(mycode)
                    hisories.append(f"Code by user -- {mycode}")
                    st.session_state['dataset_edited'] = data
                    st.session_state['pre_history'] = hisories
                    st.success("Your code is apply with succes")

    with col[1]:
        st.subheader("History")
        df_taches = pd.DataFrame({"Tasks": hisories})
        st.write(df_taches)