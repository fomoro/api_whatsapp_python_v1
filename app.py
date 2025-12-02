from flask import Flask, request

app = Flask(__name__)

@app.get("/")
def home():
    return {"msg": "OK - funcionando"}

@app.post("/mensaje")
def recibir_mensaje():
    data = request.json
    return {
        "status": "recibido",
        "contenido": data
    }

if __name__ == "__main__":
    app.run(debug=True, port=5000)
