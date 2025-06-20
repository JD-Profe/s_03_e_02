# Importamos TestClient, una herramienta que nos permite probar nuestra API FastAPI como si fuéramos un cliente externo.
from fastapi.testclient import TestClient

# Importamos la instancia 'app' desde nuestra aplicación principal.
from app.main import app

# Creamos un cliente de pruebas usando la instancia de FastAPI.
client = TestClient(app)

# Definimos una función de prueba. En pytest, toda función de test debe empezar con 'test_'.
def test_precio_final_descuento_10():
    """
    Prueba que el endpoint /precio-final devuelve correctamente un 10% de descuento.
    """
    # Simulamos una petición GET con el parámetro precio=100
    response = client.get("/precio-final?precio=100")

    # Verificamos que la respuesta tenga código HTTP 200 (OK)
    assert response.status_code == 200

    # Verificamos que el resultado sea exactamente {"precio_final": 90.0}
    assert response.json() == {"precio_final": 90.0}
