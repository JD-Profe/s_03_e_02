import sys
import os

# Añade la ruta absoluta del directorio 'app' al PYTHONPATH en tiempo de ejecución
# Esto permite que los módulos dentro de 'app' sean importados correctamente durante las pruebas.
# Importamos pytest para poder usar sus funcionalidades de pruebas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "app")))
