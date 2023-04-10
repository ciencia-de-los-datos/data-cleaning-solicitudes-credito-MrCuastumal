"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
import numpy as np


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    df.replace(r'^\s*$', np.NaN, regex=True, inplace=True)
    df.dropna(inplace=True)
    df.drop(columns=["Unnamed: 0"], inplace=True)
    df = df.astype({'sexo':'string', 'tipo_de_emprendimiento':'string', 'idea_negocio':'string', 'barrio':'string', 'línea_credito':'string'})
    df = df.apply(lambda x: x.str.lower() if x.dtype == 'string' else x)
    df['monto_del_credito'] = df['monto_del_credito'].apply(lambda x: float(x.replace('$', '').replace(',', '')) if isinstance(x, str) else x)
    for col in ["idea_negocio", "barrio", "línea_credito"]:
        df[col] = (df[col]
                .str.replace(r"[._]", " ", regex=True)
                .str.replace(r"-", " ", regex=True)
                .str.replace(r"\s+", " ", regex=True)
                .str.normalize('NFKD')
                .str.encode('ascii', errors='ignore')
                .str.decode('utf-8'))
    df.drop_duplicates(inplace=True)
    df.reset_index(drop=True, inplace=True)

    return df
