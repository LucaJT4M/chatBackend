from fastapi import FastAPI


app = FastAPI()

@app.get("/users")
def users():
    
    return "Hallo"


@app.post("/message")
async def send_message():
    return "post"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)