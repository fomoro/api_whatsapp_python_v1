import os

from flask import Flask, jsonify, render_template, request
from dotenv import load_dotenv


load_dotenv()

from backend.infrastructure.database import init_db, save_log
from backend.infrastructure.whatsapp import (
    WhatsAppAPIError,
    WhatsAppConfigurationError,
    verify_webhook_token,
)
from backend.services.message_service import build_conversations, process_webhook


def create_app():
    flask_app = Flask(__name__)
    init_db(flask_app)
    register_routes(flask_app)
    return flask_app


def register_routes(flask_app):
    @flask_app.get("/")
    def messages():
        return render_template(
            "messages.html",
            conversations=build_conversations(),
        )

    @flask_app.get("/health")
    def health():
        return {"status": "ok"}

    @flask_app.get("/mensaje")
    def message_status():
        return {"msg": "OK - funcionando"}

    @flask_app.post("/mensaje")
    def receive_manual_message():
        data = request.get_json(silent=True) or {}
        text = data.get("texto", "")
        if text:
            save_log(text)
        return {"status": "recibido", "contenido": text}

    @flask_app.get("/webhook")
    def verify_webhook():
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if challenge is None:
            return jsonify({"error": "Falta el parámetro de validación"}), 400

        try:
            valid = verify_webhook_token(token)
        except WhatsAppConfigurationError:
            flask_app.logger.exception("Configuración incompleta del webhook")
            return jsonify({"error": "Webhook no configurado"}), 503

        if not valid:
            return jsonify({"error": "Token inválido"}), 401
        return challenge, 200

    @flask_app.post("/webhook")
    def receive_webhook():
        payload = request.get_json(silent=True) or {}
        try:
            result = process_webhook(payload)
        except WhatsAppConfigurationError:
            flask_app.logger.exception("Configuración incompleta de WhatsApp")
            return jsonify({"error": "Canal de WhatsApp no configurado"}), 503
        except WhatsAppAPIError:
            flask_app.logger.exception("WhatsApp rechazó el mensaje")
            return jsonify({"error": "WhatsApp rechazó el mensaje"}), 502
        except Exception:
            flask_app.logger.exception("No fue posible procesar el webhook")
            return jsonify({"error": "No fue posible procesar el mensaje"}), 400

        return jsonify(result), 200


app = create_app()


if __name__ == "__main__":
    app.run(
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", "5000")),
        debug=os.getenv("FLASK_DEBUG", "false").lower() == "true",
    )
