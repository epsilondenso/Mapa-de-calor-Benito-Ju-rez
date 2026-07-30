import json
import folium
import pandas as pd
from .config import CATALOGO_BJ, DATOS_MAPA
#cargar json
with open(CATALOGO_BJ, encoding="utf8") as f:
    geojson = json.load(f)
#cargar datos del mapa
datos_mapa= pd.read_csv(DATOS_MAPA).set_index("colonia").to_dict("index")
#añadimos las columnas del df al json
for feature in geojson["features"]:
    colonia = feature["properties"]["colonia"]    
    datos = datos_mapa.get(colonia, {
        "precio_m2_20": "Sin datos",
        "precio_m2_22": "Sin datos",
        "precio_m2_24": "Sin datos",
        "precio_m2_26": "Sin datos",
        "Tam_muestra": "Sin datos"
    })
    feature["properties"].update(datos)



def crear_mapa(dict_colores: dict, año: int, zoom_start: int = 11):

    columna_precio = f"precio_m2_{año}"

    mapa = folium.Map(
    location=[19.3849, -99.1676],
    zoom_start=zoom_start, 
    tiles="CartoDB positron"
)
#añadimos el json
    folium.GeoJson(
    geojson,
    style_function=lambda feature: {
        "fillColor": dict_colores[feature["properties"]["colonia"]],
        "color": "blue",
        "weight": 0.5,
        "fillOpacity": 0.6,
    },
    name="Colonias",
    tooltip=folium.GeoJsonTooltip(
    fields=["colonia", columna_precio, "Tam_muestra"],
    aliases=["Col.:", "Precio", "Tamaño muestra"])
    ).add_to(mapa)
    return mapa
    #mapa.save(f"mapa_{name}.html")