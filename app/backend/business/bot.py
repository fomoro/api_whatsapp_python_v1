MENU_TEXT = """🚀 Hola, visita mi web planesenbogota.com para más información.

📌Por favor, ingresa un número #️⃣ para recibir información.

1️⃣. Información del Curso. ❔
2️⃣. Ubicación del local. 📍
3️⃣. Enviar temario en PDF. 📄
4️⃣. Audio explicando curso. 🎧
5️⃣. Video de Introducción. ⏯️
6️⃣. Hablar con chatico. 🙋‍♂️
7️⃣. Horario de Atención. 🕜
0️⃣. Regresar al Menú. 🕜"""


def build_response(text, phone):
    """Build the same deterministic response family exposed by app_old.py."""
    normalized = (text or "").lower()

    if "hola" in normalized:
        return text_payload(phone, f"🚀 Hola, ¿Cómo estás? Bienvenido {phone}.")
    if "1" in normalized:
        return text_payload(
            phone,
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
            "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "
            "when an unknown printer took a galley of type and scrambled it to make a type "
            "specimen book. It has survived not only five centuries, but also the leap into "
            "electronic typesetting, remaining essentially unchanged. It was popularised in "
            "the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, "
            "and more recently with desktop publishing software like Aldus PageMaker "
            "including versions of Lorem Ipsum.",
        )
    if "2" in normalized:
        return {
            "messaging_product": "whatsapp",
            "to": phone,
            "type": "location",
            "location": {
                "latitude": "-12.067158831865067",
                "longitude": "-77.03377940839486",
                "name": "Estadio Nacional del Perú",
                "address": "Cercado de Lima",
            },
        }
    if "3" in normalized:
        return {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": phone,
            "type": "document",
            "document": {
                "link": "https://www.turnerlibros.com/wp-content/uploads/2021/02/ejemplo.pdf",
                "caption": "Temario del Curso #001",
            },
        }
    if "4" in normalized:
        return {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": phone,
            "type": "audio",
            "audio": {
                "link": "https://filesamples.com/samples/audio/mp3/sample1.mp3",
            },
        }
    if "5" in normalized:
        return text_payload(
            phone,
            "Introduccion al curso! https://youtu.be/n1WGGQHVnP0",
            preview_url=True,
        )
    if "6" in normalized:
        return text_payload(phone, "🤝 En breve me pondre en contacto contigo. 🤓")
    if "7" in normalized:
        return text_payload(
            phone,
            "📅 Horario de Atención : Lunes a Viernes.\n🕜 Horario : 9:00 am a 5:00 pm 🤓",
        )
    if "0" in normalized:
        return text_payload(phone, MENU_TEXT)
    if "boton" in normalized:
        return button_payload(phone)
    if "btnsi" in normalized:
        return text_payload(phone, "Muchas Gracias por Aceptar.")
    if "btnno" in normalized:
        return text_payload(phone, "Es una Lastima.")
    if "btntalvez" in normalized:
        return text_payload(phone, "Estare a la espera.")
    if "lista" in normalized:
        return list_payload(phone)
    if "btncompra" in normalized:
        return text_payload(phone, "Los mejos articulos top en ofertas.")
    if "btnvender" in normalized:
        return text_payload(phone, "Excelente elección.")

    return text_payload(phone, MENU_TEXT)


def text_payload(phone, body, *, preview_url=False):
    return {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": phone,
        "type": "text",
        "text": {
            "preview_url": preview_url,
            "body": body,
        },
    }


def button_payload(phone):
    return {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": phone,
        "type": "interactive",
        "interactive": {
            "type": "button",
            "body": {"text": "¿Confirmas tu registro?"},
            "footer": {"text": "Selecciona una de las opciones"},
            "action": {
                "buttons": [
                    {"type": "reply", "reply": {"id": "btnsi", "title": "Si"}},
                    {"type": "reply", "reply": {"id": "btnno", "title": "No"}},
                    {"type": "reply", "reply": {"id": "btntalvez", "title": "Tal Vez"}},
                ]
            },
        },
    }


def list_payload(phone):
    return {
        "messaging_product": "whatsapp",
        "to": phone,
        "type": "interactive",
        "interactive": {
            "type": "list",
            "body": {"text": "Selecciona Alguna Opción"},
            "footer": {"text": "Selecciona una de las opciones para poder ayudarte"},
            "action": {
                "button": "Ver Opciones",
                "sections": [
                    {
                        "title": "Compra y Venta",
                        "rows": [
                            {
                                "id": "btncompra",
                                "title": "Comprar",
                                "description": "Compra los mejores articulos de tecnologia",
                            },
                            {
                                "id": "btnvender",
                                "title": "Vender",
                                "description": "Vende lo que ya no estes usando",
                            },
                        ],
                    },
                    {
                        "title": "Distribución y Entrega",
                        "rows": [
                            {
                                "id": "btndireccion",
                                "title": "Local",
                                "description": "Puedes visitar nuestro local.",
                            },
                            {
                                "id": "btnentrega",
                                "title": "Entrega",
                                "description": "La entrega se realiza todos los dias.",
                            },
                        ],
                    },
                ],
            },
        },
    }
