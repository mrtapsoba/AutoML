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
    initial_sidebar_state = "expanded",
    page_icon="🧊"
)


with st.sidebar:
    st.title("Auto Machine Learning")
    selected_page = option_menu("Main menu", ["About Project", "Data for study", "PreProcessing", 'Analisis', 'Machine Learning'], icons=['house', 'cloud'], menu_icon="", default_index=0)
    st.title("Halal Artificial Intelligence")

def home_page():
    st.title("Artificial Intelligence for All")
    st.divider()
    col = st.columns(2)
    with col[0]:
        st.image('https://i.pinimg.com/564x/73/3a/ab/733aabf56ce0435dd693e4e821996e24.jpg', caption='Image for illustration')
    with col[1]:
        st.subheader("What is AI and ML ?")
        st.markdown("**AI (Artificial Intelligence)**: AI refers to the simulation of human intelligence processes by computer systems. These processes include learning (the acquisition of information and rules for using the information), reasoning (using rules to reach approximate or definite conclusions), and self-correction.")
        st.markdown("**ML (Machine Learning)**: ML is a subset of AI that focuses on the development of algorithms that enable computers to learn from and make predictions or decisions based on data. It involves creating and training models that can recognize patterns in data and make intelligent decisions without being explicitly programmed to do so.")
    st.divider()
    col2 = st.columns((2,1))
    with col2[0]:
        st.subheader("What is AutoML ?")
        st.write("AutoML, or Automated Machine Learning, is an approach aimed at simplifying and automating the process of building machine learning models. By using AutoML, developers and data science practitioners can create models efficiently, without having to manually perform every step of the process.")
        st.write("With an AutoML interface, instead of writing code, users interact with a user-friendly platform that allows them to specify input data, select the types of models to explore, and define performance metrics to optimize. The interface then automatically handles all steps of the process, including data preprocessing, selecting the best algorithm, optimizing hyperparameters, and evaluating the generated models.")
    with col2[1]:
        st.image("https://i.pinimg.com/564x/62/65/6a/62656abd85e08ca48c55cc43e9959354.jpg", caption="Auto Ml")
    st.divider()
    col4 = st.columns((1,2))
    with col4[0]:
        st.image("https://i.pinimg.com/564x/42/73/28/427328eb1a8e264cc8243307bae64974.jpg", caption="AI for All")
    with col4[1]:
        st.subheader("Why AutoML ?")
        st.write("The importance of AutoML lies in its ability to democratize access to machine learning. By simplifying the model creation process, AutoML enables a wider range of people, even those without deep expertise in data science, to benefit from the advantages of artificial intelligence. This accelerates the development of AI-based solutions in various domains such as healthcare, finance, e-commerce, and more. Additionally, by automating repetitive and tedious tasks, AutoML frees up time for data science practitioners, allowing them to focus on more complex and strategic tasks.")
    st.divider()
    col3 = st.columns(2)
    with col3[0]:
        st.image("https://i.pinimg.com/564x/e4/73/86/e4738693fbcb586ab4286a4458ed9acb.jpg", caption="Contribution")
    with col3[1]:
        st.subheader("For contribution")
        st.write("Whatsapp : +226 56 90 66 66")
        st.write("Email : ktapsoba80@gmail.com")
        st.write("Github : https://github.com/mrtapsoba/AutoML")
        st.write("Open Source AI")
        st.subheader("Halal Artificial Intelligence")


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

def pre_processing():
    st.title("PreProcessing")
    col = st.columns((3,1))
    with col[0]:
        st.subheader("PreProcessing Tasks")
        task = st.selectbox("Choose a preprocessing task", ('Delete Missing data', 'Replace Missing data'),index=None)
        st.write("Small message which explain the task")
        st.divider()

    with col[1]:
        st.subheader("History")
        liste_taches = ["Supprimer les valeurs manquantes", "Normaliser les données", "Supprimer les valeurs manquantes", "Encoder les variables catégorielles", "Normaliser les données", "Supprimer les valeurs manquantes", "Supprimer les valeurs manquantes", "Normaliser les données", "Supprimer les valeurs manquantes", "Encoder les variables catégorielles", "Normaliser les données", "Supprimer les valeurs manquantes"]
        df_taches = pd.DataFrame({"Tasks": liste_taches})
        st.write(df_taches)
    

if(selected_page == "About Project"):
    home_page()
else:
    if(selected_page == "Data for study"):
        data = data_for_study()
    else:
        if('dataset_edited' not in st.session_state):
            col = st.columns((2,1))
            with col[0]:
                st.image("https://i.pinimg.com/564x/c9/22/68/c92268d92cf2dbf96e3195683d9e14fb.jpg", caption="No data found for preprocessing")
            with col[1]:
                st.title("No Data Found")
                st.write("Hello")
                st.write("We noticed that no data has been found to perform the preparation. We encourage you to go to the \"Data for study\" tab to add the necessary data.")
                st.write("Thank you very much!")

        else:
            if(selected_page == "PreProcessing"):
                #
                pre_processing()
            elif(selected_page == 'Analisis'):
                #
                st.markdown("# Analisis")
            elif(selected_page == 'Machine Learning'):
                #
                st.markdown("# Machine Learning")
        




