from flask import Blueprint

# Crear el Blueprint de cotizaciones
cotizaciones = Blueprint("cotizaciones", __name__)

@cotizaciones.route("/cotizaciones")
def home():
    return "¡Página de cotizaciones!"
