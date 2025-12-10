from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha_y_hora = db.Column(db.DateTime, default=datetime.utcnow)
    texto = db.Column(db.Text)

def guardar_mensaje(texto):
    nuevo = Log(texto=texto)
    db.session.add(nuevo)
    db.session.commit()

def cargar_datos_prueba():
    """Crea registros iniciales si la base está vacía."""
    if Log.query.count() == 0:
        ejemplos = [
            "Mensaje de prueba 1",
            "Mensaje de prueba 2",
            "Mensaje de prueba 3"
        ]
        for texto in ejemplos:
            db.session.add(Log(texto=texto))
        db.session.commit()

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///metapython.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()
        cargar_datos_prueba()
