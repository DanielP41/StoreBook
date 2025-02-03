import sys
import os
from flask import Flask

# Agrega el directorio actual al sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Intenta importar el módulo config directamente
try:
    from app.config import Config
    print("Importación exitosa")
except ImportError as e:
    print(f"Error de importación: {e}")

app = Flask(__name__)
app.config.from_object(Config)

if __name__ == '__main__':
    app.run()


