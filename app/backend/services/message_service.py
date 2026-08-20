import json
from collections import defaultdict

from backend.business.bot import build_response
from backend.infrastructure.database import (
    delete_message_by_external_id,
    display_content,
    list_messages,
    save_log,
    save_message,
)
from backend.infrastructure.whatsapp import send_message


def process_webhook(payload):
    incoming = extract_incoming_message(payload)
    if not incoming:
        return {"numero": None, "texto": "", "duplicado": False}

    phone = incoming["phone"]
    text = incoming["text"]
    save_log(f"Numero: {phone} | Mensaje: {text}")

    created = save_message(
        phone=phone,
        direction="inbound",
        message_type=incoming["message_type"],
        content=text,
        status="Recibido",
        external_message_id=incoming["external_message_id"],
    )
    if not created:
        return {"numero": phone, "texto": text, "duplicado": True}

    response_payload = build_response(text, phone)

    try:
        result = send_message(response_payload)
    except Exception as error:
        save_outbound_error(response_payload, error)
        delete_message_by_external_id(incoming["external_message_id"])
        raise

    save_outbound_result(response_payload, result)
    return {
        "numero": phone,
        "texto": text,
        "duplicado": False,
        "estado_envio": result["status_code"],
    }


def extract_incoming_message(payload):
    try:
        value = payload["entry"][0]["changes"][0]["value"]
        message = value.get("messages", [])[0]
    except (IndexError, KeyError, TypeError):
        return None

    phone = message.get("from")
    if not phone:
        return None

    return {
        "phone": phone,
        "text": extract_user_text(message),
        "message_type": message.get("type") or "unknown",
        "external_message_id": message.get("id"),
    }


def extract_user_text(message):
    message_type = message.get("type")
    if message_type == "text":
        return message.get("text", {}).get("body", "")
    if message_type != "interactive":
        return ""

    interactive = message.get("interactive", {})
    if interactive.get("type") == "button_reply":
        return interactive.get("button_reply", {}).get("id", "")
    if interactive.get("type") == "list_reply":
        return interactive.get("list_reply", {}).get("id", "")
    return ""


def save_outbound_result(payload, result):
    message_type = payload.get("type") or "text"
    content = payload.get(message_type, {})
    status = f"{result['status_code']} {result['reason']}".strip()
    legacy_log = {
        "type": message_type,
        "to": payload.get("to"),
        "content": content,
        "status": result["status_code"],
        "reason": result["reason"],
    }

    save_log(json.dumps(legacy_log, ensure_ascii=False))
    save_message(
        phone=payload.get("to"),
        direction="outbound",
        message_type=message_type,
        content=display_content(message_type, content),
        status=status,
        external_message_id=result.get("external_message_id"),
    )


def save_outbound_error(payload, error):
    message_type = payload.get("type") or "text"
    content = payload.get(message_type, {})
    error_name = type(error).__name__
    status_code = getattr(error, "status_code", None)
    reason = getattr(error, "reason", None)
    status = " ".join(str(value) for value in (status_code, reason) if value)
    if not status:
        status = f"Error: {error_name}"

    save_log(json.dumps({"error": error_name}, ensure_ascii=False))
    save_message(
        phone=payload.get("to"),
        direction="outbound",
        message_type=message_type,
        content=display_content(message_type, content),
        status=status,
    )


def build_conversations():
    grouped = defaultdict(list)

    for message in list_messages():
        grouped[message.phone].append(
            {
                "direction": message.direction,
                "text": message.content,
                "time": format_timestamp(message.created_at),
                "status": message.status or "Sin estado",
                "type": message.message_type,
                "sort_value": message.created_at,
            }
        )

    conversations = []
    for phone, messages in grouped.items():
        last_digits = "".join(character for character in phone if character.isdigit())[-4:]
        conversations.append(
            {
                "id": phone,
                "name": f"Cliente {last_digits}" if last_digits else "Sin número",
                "phone": phone,
                "messages": [
                    {key: value for key, value in message.items() if key != "sort_value"}
                    for message in messages
                ],
                "last_activity": messages[-1]["sort_value"],
            }
        )

    conversations.sort(key=lambda item: item["last_activity"], reverse=True)
    return [
        {key: value for key, value in conversation.items() if key != "last_activity"}
        for conversation in conversations
    ]


def format_timestamp(value):
    if not value:
        return "Sin fecha"
    return value.strftime("%d/%m/%Y %H:%M")
