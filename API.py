from fastapi import FastAPI
from Classes.class_importer import *

app = FastAPI()

@app.post("/create_user/{username},{password}")
def add_user(username: str, password: str):
    response = {
        "created": False,
        "msg": "User konnte nicht erstellt werden.",
        "user": None,
        "exception": ""
    }
    try:
        user = create_user(username, password)
        create_user(username, password)
        response["created"] = True
        response["msg"] = "User wurde erstellt."
        response["user"] = user

    except Exception as e: 
        response["msg"] = "User konnte nicht erstellt werden."
        response["exception"] = e
        
    return response


@app.delete("/delete_user/{user_id}")
def del_user(user_id: int):
    response = {
        "deleted": False,
        "msg": "User konnte nicht gelöscht werden.",
        "user": None,
        "exception": ""
    }
    try:
        user = delete_user(user_id)
        delete_user(user_id)
        response["deleted"] = True
        response["msg"] = "User wurde gelöscht."
        response["user"] = user
    except Exception as e: 
        response["msg"] = "User konnte nicht gelöscht werden."
        response["exception"] = e
    return response

@app.get("/show_chat/{chat_id}")
def show_chat(chat_id: int):
    return_chat = None
    for c in get_chats():
        if c.id == chat_id: # Checkt jede Chat ID aus der DB und vergleich sie mit der zu suchenden ID
            return_chat = c # Weist der return_chat variable dem aktuellen Chat zu 
            break
    return return_chat


@app.get("/users")
def users(): 
    return get_users()


@app.get("/login/{username},{password}")
def login(username: str, password: str):
    response = {
        "login": False,
        "msg": "Logindaten falsch"
    }
    user = get_user_by_name(username)
    if user: # if user checkt, ob user nicht gleich 0 ist
        if user.password == password: # checkt passwort vom user 
            # Geht hier her, wenn Passwort richtig ist.
            response["msg"] = "Passwort ist richtig, Sie werden eingeloggt."
            response["login"] = True
        else:
            response["msg"] = "Passwort falsch, bitte erneut versuchen."
    else:
        response["msg"] = "User wurde nicht gefunden."
    return response


@app.post("/send_message/{sendername},{chat_id},{message}")
async def send_message(sendername: str, chat_id: int, message: str):
    response = {
        "sended": False,
        "msg": "Nachricht konnte nicht versendet werden",
        "exception": ""
    }
    try:
        sender = get_user_by_name(sendername)
        create_message(chat_id, sender.id, content = message)
        # Wenn try user und message bekommen hat, wird response auf true gesetzt
        response["sended"] = True
        response["msg"] = "Nachricht wurde gesendet."
    except Exception as e: 
        response["msg"] = "Nachricht konnte nicht gesendet werden, bitte erneut versuchen."
        response["exception"] = e
    return response


@app.get("/get_chats_from_users/{username}")
def get_chats_from_users(username: str):
    user = get_user_by_name(username)
    chats = get_chats()
    user_chats = []
    for c in chats: # for schleife, die durch jeden Chat durch geht und weist das aktuelle Chatobjekt der Variable "c" zu
        if c.user1_id == user.id or c.user2_id == user.id: # Prüft, ob angegebener User in dem Chat mit drin ist
            user_chats.append(c) # Wenn ja, wird der Liste das aktuelle Objekt "c" hinzugefügt.
    return user_chats


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)

