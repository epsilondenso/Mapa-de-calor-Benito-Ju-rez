import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import streamlit as st
import streamlit.components.v1 as components

from src.mapa import crear_mapa
from src.colores import dict_colores_20, dict_colores_22, dict_colores_24, dict_colores_26, cmap



st.title("Precio mediano de vivienda en la alcaldía Benito Juárez (CDMX)")

#Selector de periodo

opcion = st.selectbox(
    "Selecciona un periodo",
    [
        "2020",
        "2022",
        "2024",
        "2026",
    ]
)


col_mapa, col_info = st.columns([4, 1])


dict_colores = {
    "2020": dict_colores_20,
    "2022": dict_colores_22,
    "2024": dict_colores_24,
    "2026": dict_colores_26,
}
#Creamos un mapa
mapa = crear_mapa(dict_colores[opcion], año=int(opcion[-2:]), zoom_start=13)

#Añadimos la leyenda al mapa
cmap.caption = "Precio mediano por m² (MXN)"
cmap.add_to(mapa)

#Mostramos mapa
with col_mapa:
    components.html(
        mapa._repr_html_(),
        height=900
    )
#Mostramos instrucciones
with col_info:
    #st.markdown("### Instrucciones")
    st.write(
        "Posiciona el cursor sobre una colonia para ver más detalles."
    )