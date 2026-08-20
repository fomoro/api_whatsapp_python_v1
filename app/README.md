# Aplicación Pipe

Aplicación Flask independiente que convierte el demo visual del registro de mensajes en una interfaz ejecutable.

## Estado actual

- La ruta `/` muestra el dashboard responsive.
- La ruta `/health` permite verificar que el servicio está disponible.
- Los datos son demostrativos y todavía no existe conexión con la base del POC.
- `poc/` permanece como aplicación histórica independiente.

## Ejecución local

Desde esta carpeta:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
flask --app app run --debug
```

Abrir `http://127.0.0.1:5000/`.

## Render

- Root Directory: `app`
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`
- Health Check Path: `/health`
