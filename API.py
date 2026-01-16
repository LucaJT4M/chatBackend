from fastapi import FastAPI

app = FastAPI()

@app.get ("/chat")
def chat():
    ## hier soll auf die Datenbank zugegriffen werden und die User ID's gezogen werden
    return "Chat wurde erstellt"

@app.get("/users")
def users(): 
    return "Hallo"

@app.post("/message")
async def send_message():
    return "Neue Nachricht verschickt"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)