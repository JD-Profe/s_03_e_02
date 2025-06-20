# Importamos la clase FastAPI, que nos permite crear una aplicación web moderna y ligera.
from fastapi import FastAPI

# Importamos Query, que nos sirve para declarar parámetros opcionales o requeridos en la URL.
from fastapi import Query

# Creamos una instancia de la aplicación FastAPI.
# Esta instancia será usada para definir los endpoints de nuestra API.
app = FastAPI()

# Definimos un endpoint HTTP GET que se activa cuando el usuario accede a /precio-final.
@app.get("/precio-final")
def precio_final(precio: float = Query(...)):
    """
    Calcula el precio final aplicando un 10% de descuento al valor original.

    Parámetros:
    - precio (float): Precio original introducido como parámetro en la URL. 
                      Se usa Query(...) para indicar que es obligatorio.

    Retorna:
    - dict: Un diccionario con el precio final tras aplicar el descuento.
    """

    # Aplicamos el descuento del 10% y redondeamos el resultado a 2 decimales.
    precio_descuento = round(precio * 0.90, 2)

    # Devolvemos el resultado en formato JSON.
    return {"precio_final": precio_descuento}
