from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# ---------------------------------------------------------
# Configuración base
# ---------------------------------------------------------

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///metapython.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ---------------------------------------------------------
# Modelo
# ---------------------------------------------------------

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha_y_hora = db.Column(db.DateTime, default=datetime.utcnow)
    texto = db.Column(db.Text)

# ---------------------------------------------------------
# Funciones auxiliares
# ---------------------------------------------------------

def ordenar_por_fecha(registros):
    return sorted(registros, key=lambda x: x.fecha_y_hora, reverse=True)

def guardar_mensaje(texto):
    nuevo = Log(texto=texto)
    db.session.add(nuevo)
    db.session.commit()

# ---------------------------------------------------------
# Rutas principales
# ---------------------------------------------------------

@app.route('/')
def index():
    registros = Log.query.all()
    registros_ordenados = ordenar_por_fecha(registros)
    return render_template('index.html', registros=registros_ordenados)

@app.get("/mensaje")
def estado():
    return {"msg": "OK - funcionando"}

@app.post("/mensaje")
def recibir_mensaje():
    data = request.json or {}
    texto = data.get("texto", "")

    if texto:
        guardar_mensaje(texto)

    return {
        "status": "recibido",
        "contenido": texto
    }


TOKEN_ANDERCODE = "wolfan_12345"

@app.route('/webhook', methods=['GET','POST'])
def webhook():
    if request.method == 'GET':
        #challenge = verificar_token(request)
        #return challenge
        return "GET recibido"
    elif request.method == 'POST':
        #reponse = recibir_mensajes(request)
        #return reponse
        return "POST recibido"
    

# ---------------------------------------------------------
# Inicialización y datos de prueba
# ---------------------------------------------------------

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

with app.app_context():
    db.create_all()
    cargar_datos_prueba()

# ---------------------------------------------------------
# Arranque
# ---------------------------------------------------------

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
