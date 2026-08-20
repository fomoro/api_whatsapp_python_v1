# Aplicación Pipe

Aplicación Flask que conserva las capacidades de `app_old.py` y `database_old.py`, incorpora el dashboard responsive y estructura los mensajes por conversación.

## Estructura

```text
app/
├── app.py
├── backend/
│   ├── infrastructure/
│   │   ├── database.py
│   │   └── whatsapp.py
│   ├── business/
│   │   └── bot.py
│   └── services/
│       └── message_service.py
├── templates/
│   └── messages.html
├── static/
│   ├── css/app.css
│   └── js/messages.js
└── requirements.txt
```

`app_old.py` y `database_old.py` se conservan como referencia de compatibilidad; el nuevo runtime no los importa.

## Persistencia

- `Log` conserva el formato y los registros legados.
- `Message` almacena teléfono, dirección, tipo, contenido, estado, fecha e identificador de Meta.
- Al iniciar, SQLAlchemy crea las tablas faltantes.
- Los registros legados reconocibles se incorporan a `Message` sin modificar ni borrar `Log`.
- `DATABASE_URL` permite sustituir la ubicación SQLite predeterminada.

## Rutas

- `GET /`: dashboard de conversaciones.
- `GET /health`: estado del servicio para Render.
- `GET /mensaje`: respuesta de compatibilidad del POC.
- `POST /mensaje`: registro manual compatible con el POC.
- `GET /webhook`: validación del webhook de Meta.
- `POST /webhook`: recepción, registro y respuesta de mensajes.

## Variables de entorno

| Variable | Uso |
|---|---|
| `WEBHOOK_VERIFY_TOKEN` | Token elegido para validar el webhook. |
| `WHATSAPP_TOKEN` | Token de acceso de WhatsApp Cloud API. |
| `WHATSAPP_PHONE_NUMBER_ID` | Identificador del número emisor en Meta. |
| `WHATSAPP_API_VERSION` | Versión de Graph API; por compatibilidad inicia en `v22.0`. |
| `DATABASE_URL` | URI de SQLAlchemy; opcional para ejecución local. |

Las credenciales reales no deben almacenarse en el repositorio.

Para ejecución local, estos valores se cargan desde `app/.env`. Ese archivo está ignorado por Git. `.env.example` documenta únicamente los nombres requeridos y no contiene secretos.

Render no recibe el archivo local `.env`: las mismas variables deben registrarse en la sección **Environment** del servicio nuevo.

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

La base SQLite debe ubicarse en almacenamiento persistente o reemplazarse mediante `DATABASE_URL` para evitar pérdida de registros durante despliegues o reinicios.
