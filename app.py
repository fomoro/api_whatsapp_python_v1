from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def hola():
    return render_template("holaflask.html")


@app.get("/mensaje")
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
    app.run(host='0.0.0.0',port=80,debug=True)
