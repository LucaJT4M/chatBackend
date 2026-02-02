from fastapi import FastAPI
from Classes.class_importer import *

app = FastAPI()

@app.post("/create_user/{username},{password}")
def add_user(username: str, password: str):
    return create_user(username, password)

@app.delete("/delete_user/{user_id}")
def del_user(user_id: int):
    if delete_user(user_id):
        return f"User mit der ID: {user_id} wurde gelöscht."
    else:
        return "User konnte nicht gelöscht werden."

@app.get("/show_chat/{chat_id}")
def show_chat(chat_id: int):
    # Chat anzeigen lassen
    return get_chats()

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
    if user: #if user checkt, ob user nicht gleich 0 ist
        if user.password == password: # checkt passwort vom user
            response["msg"] = "Passwort ist richtig, Sie werden eingeloggt."
            response["login"] = True
        else:
            response["msg"] = "Passwort falsch, bitte erneut versuchen."
    else:
        response["msg"] = "User wurde nicht gefunden."

    return response


@app.post("/send_message/{username1},{username2},{message}")
async def send_message(user1_id: int, user2_id: int, message: str):
    # Input: user1_Id, user2_id, message
    # User sendet Nachricht an anderen User. Wenn Chat noch nicht erstellt, dann einen erstellen. Wenn einer schon
    # erstellt ist, passiert nix und nachricht wird in den chat geschickt
    # UserID herausfinden und dem jeweiligen User zuweisen
    # return output : Nachricht versendet

    
    return "Neue Nachricht verschickt"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)