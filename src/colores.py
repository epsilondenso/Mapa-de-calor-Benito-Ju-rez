#IMPORTS

import pandas as pd
from branca.colormap import LinearColormap
from .colonias import colonias_bj
from .config import CATALOGO, CATALOGO_BJ, PRECIOS

ruta_precios: str = PRECIOS
precios = pd.read_csv(ruta_precios)
min_precio = precios.iloc[:, 1:].to_numpy().min()
max_precio = precios.iloc[:, 1:].to_numpy().max()

def precio_colonia(col_period:tuple[str,int], precios: pd.DataFrame = precios):     
    return  float(precios[precios["colonia"]==col_period[0]][f"precio_m2_{col_period[1]}"].values[0])



colors = ["green", "yellow", "orange", "red"]

cmap = LinearColormap(
    colors=colors,
    vmin=min_precio,
    vmax=max_precio)

#Crear diccionarios
dict_colores_20 = {colonia: cmap(precio_colonia((colonia, 20))) for colonia in precios["colonia"]}
dict_colores_22 = {colonia: cmap(precio_colonia((colonia, 22))) for colonia in precios["colonia"]}
dict_colores_24 = {colonia: cmap(precio_colonia((colonia, 24))) for colonia in precios["colonia"]}
dict_colores_26 = {colonia: cmap(precio_colonia((colonia, 26))) for colonia in precios["colonia"]}
dicts = [dict_colores_20, dict_colores_22, dict_colores_24, dict_colores_26]

for dict_colores in dicts:
    for colonia in colonias_bj:
        if colonia not in dict_colores:
            dict_colores[colonia] = "gray"