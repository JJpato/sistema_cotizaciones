from flask import Blueprint

# Crear el Blueprint de dashboard
dashboard = Blueprint("dashboard", __name__)

@dashboard.route("/dashboard")
def home():
    return "¡Bienvenido al Dashboard!"

