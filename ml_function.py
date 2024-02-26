import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

def get_data(filename,extention, sep, sheet_name, dtype=None):
    if(filename):
        if extention == "CSV" or extention == "Text":
            if sep=="Tabulation":
                sep_temp = "\t"
            elif sep == "Commas(,)":
                sep_temp = ","
            elif sep == "Point-commas(;)":
                sep_temp = ";"
            return pd.read_csv(filename,sep= sep_temp)
        elif extention == "Excel":
            return pd.read_excel(filename, sheet_name=sheet_name)


# PreProcessing function
def clean_missing(dataset, variables):
    # Variables is array
    dataset.dropna(subset=variables, inplace=True)
    return dataset

def replace_missing(dataset, variables, values):
    dataset # replace by value

def reset_index(dataset):
    return dataset.reset_index()


def replace_missing_values(df, target_variables, method='mean', custom_value=None):
    """
    Remplace les données manquantes dans un DataFrame par la moyenne, la médiane, le quartile
    ou une valeur personnalisée.
    
    Args:
        df (DataFrame): Le DataFrame contenant les données.
        target_variables (list): Liste des noms des variables cibles à traiter.
        method (str, optional): La méthode de remplacement ('mean', 'median', 'quartile' ou 'custom').
            Par défaut, 'mean'.
        custom_value (float or int, optional): La valeur personnalisée à utiliser si method='custom'.
            Par défaut, None.
    
    Returns:
        DataFrame: Le DataFrame avec les données manquantes remplacées.
    """
    df_copy = df.copy()
    
    for variable in target_variables:
        if method == 'Mean':
            replacement_value = df_copy[variable].mean()
        elif method == 'Median':
            replacement_value = df_copy[variable].median()
        elif method == 'Quartile':
            replacement_value = df_copy[variable].quantile(0.5)  # Quartile 50%, équivaut à la médiane
        elif method == 'Custom':
            if custom_value is None:
                raise ValueError("La méthode 'custom' nécessite une valeur personnalisée non nulle.")
            replacement_value = custom_value
        else:
            raise ValueError("La méthode de remplacement doit être 'mean', 'median', 'quartile' ou 'custom'.")

        df_copy[variable].fillna(replacement_value, inplace=True)
    
    return df_copy


def replace_outliers(data, target_columns=None, method='mean', custom_value=None):
    """
    Replace outliers in specified target columns of a dataset with specified method or custom value.

    Parameters:
        data (DataFrame): Input DataFrame.
        target_columns (list): List of column names to replace outliers in. If None, all numeric columns will be considered.
        method (str): Method for replacing outliers. Options: 'mean', 'median', 'quartile', 'custom'.
        custom_value (float): Custom value to replace outliers if method is 'custom'.

    Returns:
        DataFrame: Data with outliers replaced in specified target columns.
    """
    if target_columns is None:
        target_columns = data.select_dtypes(include=np.number).columns.tolist()

    replaced_data = data.copy()

    for column in target_columns:
        column_data = data[column]

        if method == 'mean':
            replace_value = np.mean(column_data)
        elif method == 'median':
            replace_value = np.median(column_data)
        elif method == 'quartile':
            q1 = np.percentile(column_data, 25)
            q3 = np.percentile(column_data, 75)
            replace_value = np.mean([q1, q3])
        elif method == 'custom':
            if custom_value is None:
                raise ValueError("Custom value must be specified when method is 'custom'.")
            replace_value = custom_value
        else:
            raise ValueError("Invalid method. Choose from 'mean', 'median', 'quartile', or 'custom'.")

        # Calculate the interquartile range
        q1 = np.percentile(column_data, 25)
        q3 = np.percentile(column_data, 75)
        iqr = q3 - q1

        # Define the lower and upper bounds
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        # Replace outliers
        replaced_data[column] = np.where((column_data < lower_bound) | (column_data > upper_bound), replace_value, column_data)

    return replaced_data


def remove_outliers(data, target_columns=None):
    """
    Remove outliers from specified target columns of a dataset.

    Parameters:
        data (DataFrame): Input DataFrame.
        target_columns (list): List of column names to remove outliers from. If None, all numeric columns will be considered.

    Returns:
        DataFrame: Data with outliers removed from specified target columns.
    """
    if target_columns is None:
        target_columns = data.select_dtypes(include=np.number).columns.tolist()

    cleaned_data = data.copy()

    for column in target_columns:
        column_data = data[column]

        # Calculate the interquartile range
        q1 = np.percentile(column_data, 25)
        q3 = np.percentile(column_data, 75)
        iqr = q3 - q1

        # Define the lower and upper bounds
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        # Remove outliers
        cleaned_data = cleaned_data[(column_data >= lower_bound) & (column_data <= upper_bound)]

    return cleaned_data


def normalize_data(df, target_variables, method='standard'):
    """
    Normalise les données d'un DataFrame en choisissant le type de normalisation désiré
    et en spécifiant les variables cibles.
    
    Args:
        df (DataFrame): Le DataFrame contenant les données.
        target_variables (list): Liste des noms des variables cibles à normaliser.
        method (str, optional): Le type de normalisation à appliquer ('standard', 'min_max' ou 'robust').
            Par défaut, 'standard'.
    
    Returns:
        DataFrame: Le DataFrame avec les données normalisées.
    """
    df_copy = df.copy()
    
    scaler = None
    if method == 'Standard':
        scaler = StandardScaler()
    elif method == 'MinMax':
        scaler = MinMaxScaler()
    elif method == 'Robust':
        scaler = RobustScaler()
    else:
        raise ValueError("Le type de normalisation doit être 'standard', 'min_max' ou 'robust'.")

    # Normalisation des variables cibles
    df_copy[target_variables] = scaler.fit_transform(df_copy[target_variables])
    
    return df_copy


def encode_data(df, target_variables, method='label'):
    """
    Effectue l'encodage des données d'un DataFrame en choisissant le type d'encodage désiré
    et en spécifiant les variables cibles.
    
    Args:
        df (DataFrame): Le DataFrame contenant les données.
        target_variables (list): Liste des noms des variables cibles à encoder.
        method (str, optional): Le type d'encodage à appliquer ('label' ou 'one_hot').
            Par défaut, 'label'.
    
    Returns:
        DataFrame: Le DataFrame avec les données encodées.
    """
    df_copy = df.copy()
    
    if method == 'Label':
        label_encoder = LabelEncoder()
        for variable in target_variables:
            df_copy[variable] = label_encoder.fit_transform(df_copy[variable])
    elif method == 'OneHot':
        df_copy = pd.get_dummies(df_copy, columns=target_variables)
    else:
        raise ValueError("Le type d'encodage doit être 'label' ou 'one_hot'.")
    
    return df_copy



def encode_data_2(df, target_variables, method='label'):
    """
    Effectue l'encodage des données d'un DataFrame en choisissant le type d'encodage désiré
    et en spécifiant les variables cibles.
    
    Args:
        df (DataFrame): Le DataFrame contenant les données.
        target_variables (list): Liste des noms des variables cibles à encoder.
        method (str, optional): Le type d'encodage à appliquer ('label' ou 'one_hot').
            Par défaut, 'label'.
    
    Returns:
        DataFrame: Le DataFrame avec les données encodées.
    """
    df_copy = df.copy()
    
    if method == 'label':
        label_encoder = LabelEncoder()
        for variable in target_variables:
            df_copy[variable] = label_encoder.fit_transform(df_copy[variable])
    elif method == 'one_hot':
        one_hot_encoder = OneHotEncoder(sparse=False, drop='first')
        encoded_data = one_hot_encoder.fit_transform(df_copy[target_variables])
        # Création de noms de colonnes pour les variables encodées
        column_names = one_hot_encoder.get_feature_names_out(target_variables)
        # Remplacer les colonnes originales par les colonnes encodées
        df_encoded = pd.DataFrame(encoded_data, columns=column_names, index=df_copy.index)
        df_copy = pd.concat([df_copy.drop(columns=target_variables), df_encoded], axis=1)
    else:
        raise ValueError("Le type d'encodage doit être 'label' ou 'one_hot'.")
    
    return df_copy




def reduce_data_pca(df, n_components=2):
    """
    Réduit les dimensions d'un jeu de données en utilisant l'analyse en composantes principales (PCA).
    
    Args:
        df (DataFrame): Le DataFrame contenant les données.
        n_components (int, optional): Le nombre de composantes principales à conserver.
            Par défaut, 2.
    
    Returns:
        DataFrame: Le DataFrame avec les dimensions réduites.
    """
    pca = PCA(n_components=n_components)
    reduced_data = pca.fit_transform(df)
    column_names = [f"PC{i+1}" for i in range(n_components)]
    return pd.DataFrame(data=reduced_data, columns=column_names)
