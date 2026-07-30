import json

def obtener_colonias(geojson:str, alcaldia:str) -> list[str]:
    """
    Extrae las colonias de una alcaldía dada.

    Parámetros
    ----------
    geojson : dict o str
        Diccionario del GeoJSON o ruta al archivo .geojson.
    alcaldia : str
        Nombre de la alcaldía.

    Retorna
    -------
    list[str]
        Lista ordenada alfabéticamente y sin duplicados de las colonias.
    """

    # Si se pasa una ruta, cargar el archivo
    if isinstance(geojson, str):
        with open(geojson, "r", encoding="utf-8") as f:
            geojson = json.load(f)

    colonias = {
        feature["properties"]["colonia"]
        for feature in geojson["features"]
        if feature["properties"]["alc"].strip().lower() == alcaldia.strip().lower()
    }

    return sorted(colonias)

colonias_bj=obtener_colonias(r"..\\datos\\catlogo-de-colonias.json", "Benito Juárez")
