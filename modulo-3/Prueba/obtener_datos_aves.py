# obtener_datos_aves.py
import requests


def obtener_datos_aves():
    url = "https://aves.ninjas.cl/api/birds"
    respuesta = requests.get(url)
    datos = respuesta.json()
    return datos
