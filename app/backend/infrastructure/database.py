import json
import os
import re
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint
from sqlalchemy.exc import IntegrityError


db = SQLAlchemy()


class Log(db.Model):
    """Legacy audit table kept compatible with database_old.py."""

    __tablename__ = "log"

    id = db.Column(db.Integer, primary_key=True)
    fecha_y_hora = db.Column(db.DateTime, default=datetime.utcnow)
    texto = db.Column(db.Text)


class Message(db.Model):
    """Structured message record used by the conversation dashboard."""

    __tablename__ = "message"
    __table_args__ = (
        CheckConstraint(
            "direction IN ('inbound', 'outbound')",
            name="ck_message_direction",
        ),
    )

    id = db.Column(db.Integer, primary_key=True)
    external_message_id = db.Column(db.String(255), unique=True, nullable=True, index=True)
    phone = db.Column(db.String(32), nullable=False, index=True)
    direction = db.Column(db.String(16), nullable=False, index=True)
    message_type = db.Column(db.String(32), nullable=False, default="text")
    content = db.Column(db.Text, nullable=False, default="")
    status = db.Column(db.String(64), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, index=True)


def init_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL",
        "sqlite:///metapython.db",
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()
        seed_legacy_logs()
        backfill_messages_from_logs()


def seed_legacy_logs():
    """Preserve the legacy startup behavior without seeding structured messages."""
    if Log.query.count() != 0:
        return

    db.session.add_all(
        [
            Log(texto="Mensaje de prueba 1"),
            Log(texto="Mensaje de prueba 2"),
            Log(texto="Mensaje de prueba 3"),
        ]
    )
    db.session.commit()


def save_log(text):
    db.session.add(Log(texto=text))
    db.session.commit()


def save_message(
    *,
    phone,
    direction,
    content,
    message_type="text",
    status=None,
    external_message_id=None,
    created_at=None,
):
    if external_message_id and message_exists(external_message_id):
        return False

    message = Message(
        phone=phone,
        direction=direction,
        message_type=message_type or "text",
        content=content or "",
        status=status,
        external_message_id=external_message_id,
        created_at=created_at or datetime.utcnow(),
    )
    db.session.add(message)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return False

    return True


def message_exists(external_message_id):
    if not external_message_id:
        return False
    return Message.query.filter_by(external_message_id=external_message_id).first() is not None


def delete_message_by_external_id(external_message_id):
    if not external_message_id:
        return

    message = Message.query.filter_by(external_message_id=external_message_id).first()
    if not message:
        return

    db.session.delete(message)
    db.session.commit()


def list_messages():
    return Message.query.order_by(Message.created_at.asc(), Message.id.asc()).all()


def backfill_messages_from_logs():
    """Import recognizable legacy records once, without deleting or changing Log."""
    for log in Log.query.order_by(Log.id.asc()).all():
        external_id = f"legacy-log-{log.id}"
        if message_exists(external_id):
            continue

        parsed = parse_legacy_log(log.texto)
        if not parsed:
            continue

        save_message(
            **parsed,
            external_message_id=external_id,
            created_at=log.fecha_y_hora,
        )


def parse_legacy_log(text):
    if not text:
        return None

    inbound = re.match(r"^Numero:\s*(.*?)\s*\|\s*Mensaje:\s*(.*)$", text, re.DOTALL)
    if inbound:
        phone = inbound.group(1).strip()
        if not phone or phone == "None":
            return None
        return {
            "phone": phone,
            "direction": "inbound",
            "message_type": "text",
            "content": inbound.group(2).strip(),
            "status": "Recibido",
        }

    try:
        payload = json.loads(text)
    except (TypeError, json.JSONDecodeError):
        return None

    if not isinstance(payload, dict) or not payload.get("to"):
        return None

    message_type = payload.get("type") or "text"
    status = " ".join(
        str(value) for value in (payload.get("status"), payload.get("reason")) if value
    ) or None

    return {
        "phone": str(payload["to"]),
        "direction": "outbound",
        "message_type": message_type,
        "content": display_content(message_type, payload.get("content")),
        "status": status,
    }


def display_content(message_type, content):
    if not isinstance(content, dict):
        return str(content or "")

    if message_type == "text":
        return content.get("body", "")
    if message_type == "location":
        return content.get("name") or content.get("address") or "Ubicación"
    if message_type == "document":
        return content.get("caption") or content.get("link") or "Documento"
    if message_type == "audio":
        return content.get("link") or "Audio"
    if message_type == "interactive":
        body = content.get("body", {})
        return body.get("text") or "Mensaje interactivo"

    return json.dumps(content, ensure_ascii=False)
