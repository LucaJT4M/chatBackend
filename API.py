from fastapi import FastAPI


app = FastAPI()

@app.get ("/create_user/{username},{password}")
def create_user(username: str, password: str):
    

@app.get ("/chat")
def chat():
    # hier soll auf die Datenbank zugegriffen werden und die User ID's gezogen werden
    return "Chat wurde erstellt"

@app.get("/users")
def users(): 
    return "Hallo"

@app.post("/send_message/{username1},{username2},{message}")
async def send_message(user1_ID: int, user2_ID: int, message: str):
    # Input: user1_Id, user2_id, message
    # User sendet Nachricht an anderen User. Wenn Chat noch nicht erstellt, dann einen erstellen. Wenn einer schon
    # erstellt ist, passiert nix und nachricht wird in den chat geschickt
    # UserID herausfinden und dem jeweiligen User zuweisen
    # return output : Nachricht versendet

    
    return "Neue Nachricht verschickt"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)