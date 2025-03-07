from flask import Flask
from app.config import Config
from models.database import db
from routes.auth import auth
from routes.dashboard import dashboard
from routes.cotizaciones import cotizaciones

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(auth)
app.register_blueprint(dashboard)
app.register_blueprint(cotizaciones)

if __name__ == "__main__":
    app.run(debug=True)
