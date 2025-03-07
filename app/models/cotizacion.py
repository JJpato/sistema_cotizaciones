from models.database import db

class Cotizacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Float, nullable=False)