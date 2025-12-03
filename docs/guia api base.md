# Guía de Despliegue: API Base con Flask en Render

Este documento explica cómo desplegar una API básica desarrollada con Flask en la plataforma Render.

## Resumen de Pasos Clave

1.  **Preparar el Proyecto**: Asegurarse de que el código esté listo y que el archivo `requirements.txt` incluya todas las dependencias (`Flask` y `Gunicorn`).
2.  **Versionamiento con Git**: Crear un repositorio en Git y subir el código a una plataforma como GitHub.
3.  **Crear Servicio en Render**: Conectar el repositorio de GitHub a Render y crear un nuevo "Web Service".
4.  **Configurar el Despliegue**:
    *   **Entorno**: Python.
    *   **Comando de Build**: `pip install -r requirements.txt`
    *   **Comando de Inicio**: `gunicorn app:app`
5.  **Desplegar**: Iniciar el primer despliegue y configurar despliegues automáticos con cada `git push`.

---

## Guía Detallada

### 1. Preparación del Proyecto

Asegúrate de que tu proyecto tenga la siguiente estructura y contenido.

**`app.py`**:

```python
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def hola():
    return render_template("index.html")


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
```

**`requirements.txt`**:

Para que el servidor de producción funcione, necesitamos `Gunicorn`. Asegúrate de que tu `requirements.txt` contenga lo siguiente:

```
Flask==3.0.3
gunicorn
```

**`templates/index.html`**:

Un archivo HTML simple para la ruta principal.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>API Base</title>
</head>
<body>
    <h1>API Base con Flask funcionando!</h1>
</body>
</html>
```

### 2. Versionamiento con Git

Sube tu proyecto a un repositorio de GitHub. Si no lo has hecho, sigue estos pasos:

```bash
# Inicializa el repositorio de Git
git init
git add .

# Haz tu primer commit
git commit -m "Versión inicial de la API"

# Conecta con tu repositorio remoto de GitHub y sube los cambios
git remote add origin <URL_DE_TU_REPO_EN_GITHUB>
git branch -M main
git push -u origin main
```

### 3. Crear y Configurar el Servicio en Render

1.  **Ve a tu Dashboard de Render**: [https://dashboard.render.com/](https://dashboard.render.com/)
2.  **Crea un Nuevo Servicio Web**: Haz clic en "New" -> "Web Service".
3.  **Conecta tu Repositorio**: Elige el repositorio de GitHub que acabas de crear.
4.  **Configura los Detalles del Servicio**:
    *   **Name**: Elige un nombre para tu servicio (ej. `api-whatsapp-python-v1`).
    *   **Region**: Elige la más cercana a ti.
    *   **Branch**: `main`.
    *   **Runtime**: `Python 3`.
    *   **Build Command**: `pip install -r requirements.txt`. Render suele detectar esto automáticamente.
    *   **Start Command**: `gunicorn app:app`. **Importante**: `app:app` se refiere a `nombre_del_archivo:variable_flask`.
    *   **Instance Type**: `Free`.

5.  **Despliegue Automático (Opcional pero recomendado)**: Asegúrate de que la opción "Auto-Deploy" esté activada ("Yes"). Esto hará que Render despliegue automáticamente cada vez que hagas un `git push` a la rama `main`.

### 4. Desplegar

1.  Haz clic en **"Create Web Service"**.
2.  Render comenzará a construir y desplegar tu aplicación. Puedes ver los logs en tiempo real.
3.  Una vez finalizado, tu API estará disponible en la URL que Render te proporciona (similar a `https://api-whatsapp-python-v1.onrender.com/`).

### Información del Proyecto

*   **Dashboard de Render**: [https://dashboard.render.com/web/srv-d4nmigi4d50c739n7pr0](https://dashboard.render.com/web/srv-d4nmigi4d50c739n7pr0)
*   **URL de la API**: [https://api-whatsapp-python-v1.onrender.com/](https://api-whatsapp-python-v1.onrender.com/)

---
