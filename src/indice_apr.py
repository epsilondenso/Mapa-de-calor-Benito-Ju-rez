import pandas as pd
import numpy as np


def get_indice(df_indices: pd.DataFrame, trimestre: int, año: int) -> float:
    indice = df_indices.loc[
        (df_indices["trimestre"] == trimestre) &
        (df_indices["año"] == año),
        "índice"]
    return indice.iloc[0] 

def obtener_pm2_colonia(ratio: float, ruta_dato_actual:str) -> pd.DataFrame:

    dato_actual = pd.read_csv(ruta_dato_actual)
    p_m2_median = dato_actual["precio_m2"]*ratio

    return pd.DataFrame([dato_actual["colonia"], p_m2_median], index=["colonia", "precio_m2"]).T