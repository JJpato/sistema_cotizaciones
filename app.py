import sys
import os

# Agregar el directorio raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Agregar la carpeta 'app' directamente si el problema es con app.models
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "app")))

from flask import Flask
from app.config import Config
from app.models.database import db
from app.routes.auth import auth
from app.routes.dashboard import dashboard
from app.routes.cotizaciones import cotizaciones

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'app', 'templates'))
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(auth)
app.register_blueprint(dashboard)
app.register_blueprint(cotizaciones)

if __name__ == "__main__":
    print("Rutas en sys.path:")
    print("\n".join(sys.path))  # Imprimir rutas para depuración
    app.run(debug=True)
