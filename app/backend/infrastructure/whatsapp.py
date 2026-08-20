import http.client
import hmac
import json
import os


class WhatsAppConfigurationError(RuntimeError):
    pass


class WhatsAppAPIError(RuntimeError):
    def __init__(self, status_code, reason):
        super().__init__(f"WhatsApp respondió {status_code} {reason}")
        self.status_code = status_code
        self.reason = reason


def verify_webhook_token(provided_token):
    expected_token = os.getenv("WEBHOOK_VERIFY_TOKEN")
    if not expected_token:
        raise WhatsAppConfigurationError(
            "Falta la variable de entorno requerida: WEBHOOK_VERIFY_TOKEN"
        )
    if not provided_token:
        return False
    return hmac.compare_digest(provided_token, expected_token)


def send_message(payload):
    token = os.getenv("WHATSAPP_TOKEN")
    phone_number_id = os.getenv("WHATSAPP_PHONE_NUMBER_ID")
    api_version = os.getenv("WHATSAPP_API_VERSION", "v22.0")

    missing = [
        name
        for name, value in (
            ("WHATSAPP_TOKEN", token),
            ("WHATSAPP_PHONE_NUMBER_ID", phone_number_id),
        )
        if not value
    ]
    if missing:
        raise WhatsAppConfigurationError(
            f"Faltan variables de entorno requeridas: {', '.join(missing)}"
        )

    connection = http.client.HTTPSConnection("graph.facebook.com", timeout=10)
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }

    try:
        connection.request(
            "POST",
            f"/{api_version}/{phone_number_id}/messages",
            body=body,
            headers=headers,
        )
        response = connection.getresponse()
        response_body = response.read().decode("utf-8", errors="replace")
        if not 200 <= response.status < 300:
            raise WhatsAppAPIError(response.status, response.reason)
        return {
            "status_code": response.status,
            "reason": response.reason,
            "body": response_body,
            "external_message_id": extract_message_id(response_body),
        }
    finally:
        connection.close()


def extract_message_id(response_body):
    try:
        payload = json.loads(response_body)
        return payload.get("messages", [{}])[0].get("id")
    except (AttributeError, IndexError, TypeError, json.JSONDecodeError):
        return None
