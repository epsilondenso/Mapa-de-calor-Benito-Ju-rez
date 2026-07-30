from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DATOS = ROOT / "datos"

CATALOGO = DATOS / "catlogo-de-colonias.json"
CATALOGO_BJ = DATOS / "catalogo-bj.json"
PRECIOS = DATOS / "clean" / "precios_final.csv"
DATOS_MAPA = DATOS / "clean" / "datos_mapa.csv"