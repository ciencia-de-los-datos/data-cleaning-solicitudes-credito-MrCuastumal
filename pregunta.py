"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
import numpy as np


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col='Unnamed: 0')

    df.sexo = df.sexo.str.lower()
    df.sexo = df.sexo.astype('category')
    df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.str.lower()
    df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.astype('category')
    df.idea_negocio = df.idea_negocio.str.lower().str.replace("_|-", " ", regex=True).astype('category')
    df['barrio'] = df['barrio'].str.lower().astype('category').str.replace(r'_|-', ' ', regex=True)
    df.estrato = df.estrato.astype('category')
    df.comuna_ciudadano = df.comuna_ciudadano.astype('category')
    df.fecha_de_beneficio = pd.to_datetime(df['fecha_de_beneficio'], dayfirst= True)
    df['monto_del_credito'] = df['monto_del_credito'].str.replace(r'[^\d.]', '', regex=True).astype(float)
    df['línea_credito'] = df['línea_credito'].str.lower().astype('category')
    df['línea_credito'] = df['línea_credito'].str.replace("_|-", " ", regex=True)
    
    df.dropna(axis='index',inplace=True)
    df.drop_duplicates(inplace=True)

    return df
