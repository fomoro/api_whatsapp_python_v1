Aquí tienes el **README.md** completo, claro y listo para pegar en tu repo.

---

# API WhatsApp Python v1 — Test Project

Este es un proyecto simple con Flask para probar **endpoints GET y POST**.

## Requisitos

* Python 3.x
* pip

## Instalación

### 1. Clonar el repositorio

```bash
git clone <repository_url>
cd api_whatsapp_python_v1
```

### 2. Instalar dependencias

```bash
pip install Flask
```

## Estructura del proyecto

```
api_whatsapp_python_v1/
│
├── app.py
└── README.md
```

## Código básico (`app.py`)

```python
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
```

## Ejecutar la API

```bash
python app.py
```

Abrir en navegador o Postman:

* GET:
  [http://localhost:5000/](http://localhost:5000/)

* POST:
  [http://localhost:5000/mensaje](http://localhost:5000/mensaje)
  Body → JSON

  ```json
  {
    "texto": "hola"
  }
  ```

## Subir cambios a GitHub

```bash
git status
git add .
git commit -m "Agregar API básica GET y POST"
git push origin main
```

---

Si quieres, te armo también el `requirements.txt` y un flujo para producción (Docker, venv, etc.).
