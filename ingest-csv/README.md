# Procesamiento masivo de comentarios

## ¿Qué?
Programa en python que utiliza Lenguaje Natural Procesado para dado un archivo CSV donde cada fila representa un comentario del cliente, este extrae el sentimiento y los topics de cada comentario.

Herramientas utilizadas
* Python
* Langchain
* OpenAI

## ¿Como?
Es recomendado utilizar un virtual environment para descargar las librerias necesarias. e.g. Anaconda.

```
pip install -r requirements.txt
python ingest_csv.py
```
Despues de esto se generará el archivo csv de sentimientos extraidos.



