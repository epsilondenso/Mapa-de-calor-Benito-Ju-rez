import json
from .config import CATALOGO, CATALOGO_BJ
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
    #if isinstance(geojson, str):
    with open(geojson, "r", encoding="utf-8") as f:
            geojson = json.load(f)

    colonias = {
        feature["properties"]["colonia"]
        for feature in geojson["features"]
        if feature["properties"]["alc"].strip().lower() == alcaldia.strip().lower()
    }

    return sorted(colonias)

colonias_bj=obtener_colonias(CATALOGO, "Benito Juárez")

def filtrar_alcaldia_inplace(ruta_geojson: str, alcaldia: str, propiedad: str = "alc"):
    """
    Elimina del GeoJSON todas las features cuya alcaldía no coincida.

    Modifica el diccionario geojson in-place.
    """
    with open(ruta_geojson, "r", encoding="utf-8") as f:
        geojson = json.load(f)

    geojson["features"][:] = [
        feature
        for feature in geojson["features"]
        if feature["properties"][propiedad].strip().lower()
        == alcaldia.strip().lower()
    ]

    with open(ruta_geojson, "w", encoding="utf-8") as f:
        json.dump(geojson, f, ensure_ascii=False, indent=1)


filtrar_alcaldia_inplace(ruta_geojson=CATALOGO_BJ, alcaldia="Benito Juárez")