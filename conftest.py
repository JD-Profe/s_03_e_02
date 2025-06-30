# Añadimos un fichero conftest.py al proyecto para configurar y compartir recursos comunes entre pruebas en pytest, 
# sin necesidad de importar manualmente esos recursos en cada archivo de test.

import sys
import os

# Añade la ruta absoluta del directorio 'app' al PYTHONPATH en tiempo de ejecución
# Esto permite que los módulos dentro de 'app' sean importados correctamente durante las pruebas.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "app")))
