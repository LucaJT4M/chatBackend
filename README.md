# Chat Backend

Ein einfaches Chat-Anwendungs-Backend, das mit FastAPI entwickelt wurde. Es ermöglicht Benutzern, Konten zu erstellen, Chats zu führen und Nachrichten auszutauschen.

## Features

- 👤 **Benutzerverwaltung**: Benutzer erstellen und verwalten
- 💬 **Chat-System**: Chats zwischen zwei Benutzern erstellen
- 📨 **Nachrichten**: Nachrichten in Chats senden und abrufen
- 💾 **SQLite Datenbank**: Persistente Datenspeicherung

## Anforderungen

- Python 3.8+
- FastAPI
- Uvicorn

## Installation

1. Repository klonen oder herunterladen

```bash
git clone <repository-url>
cd chatBackend
```

2. Virtuelle Umgebung erstellen (optional aber empfohlen)

```bash
python -m venv venv
venv\Scripts\activate
```

3. Dependencies installieren

```bash
pip install -r requirements.txt
```

## Verwendung

### Server starten

```bash
python API.py
```

Der Server läuft dann unter `http://localhost:8000`

### API Endpoints

| Methode | Endpoint                                          | Beschreibung             |
| ------- | ------------------------------------------------- | ------------------------ |
| GET     | `/users`                                          | Alle Benutzer abrufen    |
| GET     | `/create_user/{username},{password}`              | Neuen Benutzer erstellen |
| GET     | `/show_chat/{chat_id}`                            | Chat anzeigen            |
| POST    | `/send_message/{username1},{username2},{message}` | Nachricht senden         |

## Projektstruktur

```
chatBackend/
├── API.py                    # FastAPI Anwendung & Endpoints
├── DB_Manager.py             # Datenbank-Operationen
├── Client.py                 # Client-Implementierung
├── requirements.txt          # Python Dependencies
├── chatData.db               # SQLite Datenbank (wird automatisch erstellt)
└── Classes/
    ├── user.py               # User Klasse
    ├── chat.py               # Chat Klasse
    ├── message.py            # Message Klasse
    └── class_importer.py     # Import aller Klassen
```

## Datenbank-Schema

Die Anwendung nutzt SQLite mit folgenden Tabellen:

- `users` - Benutzerinformationen
- `chats` - Chat-Sessionen zwischen Benutzern
- `messages` - Nachrichten in Chats

## Lizenz

Dieses Projekt ist Teil eines Schulprojekts.
