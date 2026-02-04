# ChatBackend

## Kurze Beschreibung

Dieses Repository enthält ein kleines Chat-Backend geschrieben in Python mit FastAPI. Es bietet einfache REST-Endpoints für Benutzerverwaltung, Erstellung von Chats und Senden/Abrufen von Nachrichten. Ein schlichtes HTML-Frontend befindet sich im Ordner `html/`.

**Voraussetzungen**

- Python 3.10 oder neuer
- Virtuelle Umgebung empfohlen (im Projekt liegt eine venv unter `chatBackend`)
- Abhängigkeiten: `requirements.txt`

**Schnellstart (Windows, PowerShell)**

1. Virtuelle Umgebung aktivieren:

```powershell
& .\chatBackend\Scripts\Activate.ps1
```

2. Abhängigkeiten installieren:

```powershell
pip install -r requirements.txt
```

3. Entwicklermanagement-Server starten:

```powershell
uvicorn API:app --reload --host 127.0.0.1 --port 8000
```

Die API ist jetzt unter `http://127.0.0.1:8000` erreichbar; die interaktive Swagger-Dokumentation unter `http://127.0.0.1:8000/docs`.

**API-Endpoints (Kurzreferenz mit Beispielen)**

- `POST /create_user/{username},{password}` — Benutzer anlegen
  - Beispiel (curl):

```bash
curl -X POST "http://127.0.0.1:8000/create_user/alice,secret"
```

- `DELETE /delete_user/{user_id}` — Benutzer löschen

```bash
curl -X DELETE "http://127.0.0.1:8000/delete_user/1"
```

- `GET /users` — Alle Benutzer anzeigen

```bash
curl "http://127.0.0.1:8000/users"
```

- `GET /login/{username},{password}` — Login prüfen

```bash
curl "http://127.0.0.1:8000/login/alice,secret"
```

- `POST /send_message/{sendername},{chat_id},{message}` — Nachricht senden

```bash
curl -X POST "http://127.0.0.1:8000/send_message/alice,1,Hallo%20Welt"
```

- `GET /show_chat/{chat_id}` — Einzelnen Chat anzeigen

```bash
curl "http://127.0.0.1:8000/show_chat/1"
```

- `POST /create_chat/{user1_id},{user2_id}` — Chat erstellen

```bash
curl -X POST "http://127.0.0.1:8000/create_chat/1,2"
```

- `GET /get_chats_from_users/{username}` — Chats eines Benutzers abrufen

```bash
curl "http://127.0.0.1:8000/get_chats_from_users/alice"
```

Hinweis: Einige Endpoints verwenden Pfadparameter mit Kommas. Beim Verwenden in Shells oder mit bestimmten HTTP-Clients auf URL-Encoding achten.

**Wichtige Projektdateien**

- `API.py` — FastAPI-Anwendung und Routing ([API.py](API.py))
- `DB_Manager.py` — Datenbank-/Speicher-Operationen ([DB_Manager.py](DB_Manager.py))
- `Classes/` — `chat.py`, `user.py`, `message.py` und Hilfsdateien ([Classes](Classes))
- `chatData.db` — lokale SQLite-Datenbank (falls verwendet)
- `html/` — kleines Frontend: `index.html`, `chat.html`, `register.html` ([html](html))

**Sicherheit & Hinweise**

- Dieses Projekt ist als Lern-/Entwicklungsprojekt gedacht — nicht produktionsreif.
- Passwörter werden aktuell im Klartext verarbeitet. Für Produktion: Password-Hashing (z. B. `bcrypt`) und HTTPS verwenden.
- Input-Validierung und Fehlerbehandlung sind rudimentär; für robuste Anwendungen erweitern und Tests hinzufügen.

**Entwicklung & Tests**

- Es sind keine automatischen Tests im Repository vorhanden. Nutze Postman, HTTPie oder curl für manuelle Tests.
- Zum Entwickeln: `uvicorn` mit `--reload` benutzen, Codeänderungen werden automatisch neu geladen.

**Mitwirken**

- Pull Requests willkommen. Beschreibe Änderungen kurz und liefere reproduzierbare Schritte.

**Lizenz**

- Kein Lizenztext enthalten — bei Bedarf eine Lizenzdatei (`LICENSE`) hinzufügen.

Wenn du möchtest, kann ich noch eine englische Version, ausführliche cURL- und JavaScript-Beispiele für das Frontend oder eine Liste sicherheitsrelevanter Verbesserungen ergänzen.

# ChatBackend

## Kurze Beschreibung

Dieses Repository enthält ein einfaches Chat-Backend in Python (FastAPI). Es stellt REST-Endpoints zur Benutzerverwaltung, Chat-Erstellung und Nachrichtenübertragung bereit. Ein kleines HTML-Frontend liegt im Ordner `html/` bei.

**Voraussetzungen**

- Python 3.10+ (oder kompatibel)
- virtuelle Umgebung (im Projektordner liegt eine venv unter `chatBackend`)
- Abhängigkeiten in `requirements.txt`

**Installation**

1. Virtuelle Umgebung aktivieren (Windows PowerShell):

   `& .\chatBackend\Scripts\Activate.ps1`

2. Abhängigkeiten installieren:

   `pip install -r requirements.txt`

**Starten (Entwicklung)**
Im Projektstamm starten Sie den Server mit uvicorn:

`uvicorn API:app --reload --host 127.0.0.1 --port 8000`

Danach ist die API unter `http://127.0.0.1:8000` erreichbar. Die automatische API-Dokumentation: `http://127.0.0.1:8000/docs`.

**Wichtige Endpoints (Kurzreferenz)**

- `POST /create_user/{username},{password}` — Benutzer anlegen
  - Beispiel: `POST http://127.0.0.1:8000/create_user/alice,secret`
- `DELETE /delete_user/{user_id}` — Benutzer löschen
- `GET /users` — Alle Benutzer anzeigen
- `GET /login/{username},{password}` — Login prüfen
- `POST /send_message/{sendername},{chat_id},{message}` — Nachricht senden
- `GET /show_chat/{chat_id}` — Einzelnen Chat anzeigen
- `POST /create_chat/{user1_id},{user2_id}` — Chat zwischen zwei Benutzern erstellen
- `GET /get_chats_from_users/{username}` — Chats eines Benutzers abrufen

Hinweis: Die Endpoints verwenden einfache Pfadparameter; beim Testen ggf. URL-Encodierung beachten.

**Projektdateien (Auswahl)**

- `API.py` — FastAPI-Anwendung und Routing ([API.py](API.py))
- `DB_Manager.py` — Datenbank‑/Speicherfunktionen ([DB_Manager.py](DB_Manager.py))
- `Classes/` — Domain-Modelle und Hilfsfunktionen ([Classes](Classes))
- `html/` — kleines Frontend mit `chat.html`, `index.html`, `register.html` ([html](html))

**Entwicklung & Hinweise**

- Fehlerbehandlung und Security sind minimal — nicht produktionsreif.
- Passwords werden derzeit im Klartext verarbeitet — für Produktion unbedingt Hashing verwenden.
- Tests sind nicht enthalten; bitte manuelle API-Tests oder Postman/HTTPie verwenden.

Wenn du möchtest, formatiere ich die README noch ausführlicher (Beispiele, cURL-Requests, Diagramme).

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
