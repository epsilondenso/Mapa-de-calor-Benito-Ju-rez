# Metodología

## Scraper

Para obtener los datos actuales se utilizó como base el siguiente repositorio:

https://github.com/Haseeb536/inmuebles24-scraper

El repositorio fue clonado y adaptado para:
- Buscar propiedades dentro de la alcaldía seleccionada.
- Considerar únicamente propiedades en venta.
- Extraer únicamente las variables relevantes para esta prueba.

Los datos obtenidos mediante scraping se encuentran en: datos/properties.csv


En total, se recopilaron **395 anuncios publicados durante el año en curso** provenientes del portal Inmuebles24.

---

## Interpretación de datos

Debido a que el índice SHF de 2026 únicamente cuenta con información de apreciación correspondiente al **primer trimestre del año**, la estimación para los años 2020, 2022 y 2024 se realizó utilizando también los valores correspondientes al primer trimestre de cada año.

El procedimiento fue el siguiente:

1. Se calculó el **precio mediano por colonia** a partir de los datos obtenidos mediante scraping.

   La elección de la mediana sobre la media se debe a que la media es más sensible a valores extremos, como propiedades de lujo, que pueden sesgar la distribución hacia precios elevados.

2. Para estimar los precios históricos por colonia se aplicó el ajuste utilizando el índice de apreciación SHF:

   $$
   Precio = Precio_{2026}\frac{I_{año}}{I_{2026}}
   $$
   Donde $I_{2026}$ e $I_{año}$ corresponde a los respectivos índices de apreciación.
   Los índices utilizados tienen como base el año 2017 con valor 100.
   La asunción principal es que todas las colonias evolucionaron de la misma forma entre 2020 y el presente año. 
---

## Visualización

La visualización fue desarrollada utilizando:

- **Streamlit** para la interfaz interactiva.
- **Folium** para la generación del mapa.

El mapa permite:
- Seleccionar el año de visualización.
- Consultar información de cada colonia al posicionar el cursor sobre ella.
- Mostrar datos como:
  - Precio estimado por colonia.
  - Tamaño de muestra utilizado para el cálculo.
