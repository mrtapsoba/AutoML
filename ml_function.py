import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

def get_data(filename, sep, dtype=None):
    if(filename):
        if sep=="Tabulation":
            sep_temp = "\t"
        elif sep == "Commas(,)":
            sep_temp = ","
        elif sep == "Point-commas(;)":
            sep_temp = ";"
        return pd.read_csv(filename,sep= sep_temp)
    
# PreProcessing function
def clean_missing(dataset, variables):
    # Variables is array
    dataset.dropna(subset=variables, inplace=True)
    return dataset

def replace_missing(dataset, variables, values):
    dataset # replace by value

def reset_index(dataset):
    return dataset.reset_index()

def normalize(dataset, type):
    if(type == "Standard"):
        scaler = StandardScaler()
    elif(type == "MinMax"):
        scaler = MinMaxScaler()
    elif(type == "Robust"):
        scaler = MinMaxScaler()
    scaler = scaler.fit(dataset)
    return scaler.transform(dataset)