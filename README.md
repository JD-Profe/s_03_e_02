# Pruebas automatizadas con FastAPI, pytest y GitHub Actions

Este proyecto es un **ejemplo** que simula cómo un equipo de desarrollo puede usar integración continua (CI) para asegurarse de que una aplicación web **no se rompe al hacer cambios**.

Usaremos:

- 🐍 **Python** para la programación
- ⚡ **FastAPI** para crear una API web sencilla
- 🧪 **pytest** para definir y ejecutar pruebas automatizadas
- ☁️ **GitHub Actions** para automatizar las pruebas en cada cambio del código

---

## Objetivo

Anteriormente hemos visto un error de despliegue causado por la falta de pruebas automatizadas. Veremos cómo una acción de GitHub puede prevenir que un cambio defectuoso llegue a producción.

---

## Requisitos previos

Antes de empezar, asegúrate de tener instalado:

- [Python 3.10](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- Una cuenta en [GitHub](https://github.com/)
- Editor recomendado: [Visual Studio Code](https://code.visualstudio.com/)

---

## Estructura del proyecto

```
s_03_e_02/
├── app/
│   └── main.py               ← Código de la API con FastAPI
├── tests/
│   └── test_main.py          ← Prueba con pytest
├── .github/
│   └── workflows/
│       └── python-ci.yml     ← Configuración de GitHub Actions
├── requirements.txt          ← Dependencias del proyecto
├── conftest.py               ← Añade la ruta `app/` al entorno de pruebas
├── .gitignore                ← Ignora entorno virtual y archivos temporales
└── README.md                 ← Este archivo
```

---

## Paso 1: Crear el entorno virtual y activar

Abre una terminal y ejecuta:

```bash
python -m venv venv
```

Activa el entorno:

- En Windows:

  ```bash
  .\venv\Scripts\activate
  ```

- En macOS/Linux:

  ```bash
  source venv/bin/activate
  ```

---

## Paso 2: Instalar las dependencias

En una sola línea:

```bash
pip install fastapi uvicorn pytest
```

Y guarda las dependencias:

```bash
pip freeze > requirements.txt
```

---

## Paso 3: Crear la API con FastAPI

Crea el archivo `app/main.py` con este contenido:

```python
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/precio-final")
def precio_final(precio: float = Query(...)):
    """
    Calcula el precio final aplicando un 10% de descuento.
    """
    precio_descuento = round(precio * 0.90, 2)
    return {"precio_final": precio_descuento}
```

---

## Paso 4: Crear el test automático

Crea el archivo `tests/test_main.py` con este contenido:

```python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_precio_final_descuento_10():
    response = client.get("/precio-final?precio=100")
    assert response.status_code == 200
    assert response.json() == {"precio_final": 90.0}
```

---

## Paso 5: Configurar `conftest.py` para que funcione pytest

Crea un archivo `conftest.py` en la raíz con:

```python
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "app")))
```

---

## Paso 6: Crear el workflow de GitHub Actions

Crea el archivo `.github/workflows/python-ci.yml` con este contenido:

```yaml
name: Python CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python 3.10
        uses: actions/setup-python@v4
        with:
          python-version: "3.10"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests
        run: pytest
```

---

## Paso 7: Subir a GitHub

Inicializa el repositorio si no lo has hecho:

```bash
git init
git remote add origin https://github.com/TU_USUARIO/s_03_e_02.git
git add .
git commit -m "Primer commit del proyecto s_03_e_02"
git branch -M main
git push -u origin main
```

> Sustituye `TU_USUARIO` por tu nombre de usuario en GitHub.

---

## Paso 8: Ver el resultado en GitHub Actions

1. Ve a la pestaña **Actions** del repositorio.
2. Verás el pipeline ejecutándose automáticamente.
3. Si todo está correcto, los tests pasarán ✅

---

## ✅ ¿Cómo sé si algo falla?

- Si un alumno edita la API y rompe el cálculo (por ejemplo, elimina el `* 0.90`), el test fallará automáticamente en GitHub Actions.
- Así demostramos cómo **la CI evita que errores se desplieguen sin ser detectados.**

---




