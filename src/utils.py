import unicodedata

def quitar_acentos(texto):
    if texto is None:
        return texto

    return "".join(
        c for c in unicodedata.normalize("NFD", str(texto))
        if unicodedata.category(c) != "Mn"
    )
