from flask import Flask, render_template


app = Flask(__name__)


def load_demo_conversations() -> list[dict]:
    """Return isolated sample data until a real message repository is connected."""
    return [
        {
            "id": "c1",
            "name": "Cliente 0101",
            "phone": "+57 300 000 0101",
            "messages": [
                {"direction": "inbound", "text": "Hola", "time": "09:14", "status": "Recibido"},
                {
                    "direction": "outbound",
                    "text": "Hola, ¿cómo estás? Bienvenido a Pipe.\n\nEscribe 0 para ver el menú de opciones.",
                    "time": "09:14",
                    "status": "Entregado",
                },
                {"direction": "inbound", "text": "0", "time": "09:15", "status": "Recibido"},
                {
                    "direction": "outbound",
                    "text": (
                        "Selecciona una opción para continuar:\n\n"
                        "1. Información\n2. Ubicación\n3. Documento\n4. Audio\n"
                        "5. Video\n6. Hablar con una persona\n7. Horario"
                    ),
                    "time": "09:15",
                    "status": "Entregado",
                },
            ],
        },
        {
            "id": "c2",
            "name": "Cliente 0202",
            "phone": "+57 300 000 0202",
            "messages": [
                {"direction": "inbound", "text": "2", "time": "08:46", "status": "Recibido"},
                {
                    "direction": "outbound",
                    "text": "Esta es la ubicación registrada para el punto de atención.",
                    "time": "08:46",
                    "status": "Entregado",
                },
            ],
        },
        {
            "id": "c3",
            "name": "Cliente 0303",
            "phone": "+57 300 000 0303",
            "messages": [
                {
                    "direction": "inbound",
                    "text": "Quiero hablar con una persona",
                    "time": "Ayer",
                    "status": "Recibido",
                },
                {
                    "direction": "outbound",
                    "text": "Registramos tu solicitud. Una persona continuará la conversación.",
                    "time": "Ayer",
                    "status": "Enviado",
                },
            ],
        },
        {
            "id": "c4",
            "name": "Cliente 0404",
            "phone": "+57 300 000 0404",
            "messages": [
                {"direction": "inbound", "text": "Horario", "time": "Ayer", "status": "Recibido"}
            ],
        },
    ]


@app.get("/")
def messages():
    return render_template("messages.html", conversations=load_demo_conversations())


@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(debug=True)
