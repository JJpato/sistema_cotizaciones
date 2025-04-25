from models.database import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'  # Nombre de la tabla en la base de datos

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)  # BigInt para 'id'
    username = db.Column(db.String(150), unique=True, nullable=False)    # 'username'
    password = db.Column(db.String(200), nullable=False)                 # 'password' (ajustado a 200)
    email = db.Column(db.String(120), unique=True, nullable=False)       # 'email'
    position = db.Column(db.String(150), default=None)                   # 'position'
    phone = db.Column(db.String(20), default=None)                       # 'phone'
    active = db.Column(db.Boolean, default=True)                          # 'active' (activo por defecto)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)  # 'date_created'

    def __repr__(self):
        return f'<User {self.username}>'