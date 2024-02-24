import ml_function as ftn
import streamlit as st
import pandas as pd

def pre_processing(data):
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
                    new_data = st.selectbox("Replace by", ["Mean", "Median", "Quartile", "Other value"])
                    if(new_data == "Other value"):
                        with col2[1]:
                            other = st.text_input("New value")
            variables = st.multiselect("Choose the variables to update", data.keys())

            if(st.button("Apply")):
                st.error("Save data")
        elif task == "Data Transformation":
            col2 = st.columns(2)
            with col2[0]:
                transformation = st.selectbox("choose the transformation", ["Normalization", "Encodage"])
                if transformation == "Normalization":
                    with col2[1]:
                        normalization = st.selectbox("choose the normalization", ["Standard", "MinMax"])
                elif transformation == "Encodage":
                    with col2[1]:
                        normalization = st.selectbox("choose the encodage", ["LabelEncoder", ""])
            variables = st.multiselect("Choose the variables to transform", data.keys())
            if(st.button("Apply")):
                st.success("Transform with succes")

        elif task == "Code Myself":
            mycode = st.text_area("Write your code in Python")
            if(mycode != None):
                st.write("See your code")
                st.code(mycode)
                if(st.button("Apply")):
                    exec(mycode)
                    st.success("Your code is apply with succes")

    with col[1]:
        st.subheader("History")
        liste_taches = ["Supprimer les valeurs manquantes", "Normaliser les données", "Supprimer les valeurs manquantes", "Encoder les variables catégorielles","Supprimer les valeurs manquantes", "Normaliser les données", "Supprimer les valeurs manquantes", "Encoder les variables catégorielles", "Supprimer les valeurs manquantes", "Normaliser les données", "Supprimer les valeurs manquantes", "Encoder les variables catégorielles","Supprimer les valeurs manquantes", "Normaliser les données", "Supprimer les valeurs manquantes", "Encoder les variables catégorielles"]
        df_taches = pd.DataFrame({"Tasks": liste_taches})
        st.write(df_taches)