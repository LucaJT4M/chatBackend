from Classes.class_importer import *
import requests

url = 'http://localhost:8000'

# response = requests.get(url+"/users")

# if response.status_code == 200:
#     ##print(response.json())

#     import json
#     print(json.dumps(response.json()))
# else:
#     print(f'Fehler: {response.status_code}\n{response.content}')

app = FastAPI()
temp = Jinja2Templates(directory="html")

@app.get("/")
def index(request: Request):
 
    return temp.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )

@app.post("/login")
def login(
    username: str = Form(...),
    password: str = Form(...), 
    request: Request = None
):
    response = requests.get(url+f"/login/{username},{password}")
    if response.status_code == 200:
        loginCorrect = json.dumps(response.json()["login"])

        if loginCorrect: #wenn login true ist, dann geht er hier rein
            response = requests.get(url+"/users") #hier holt er alle user
            users = response.json()
            
            response = requests.get(url+f"/get_chats_from_users/{username}")
            chats = response.json()

            print("Passwort is korrekt")

            return temp.TemplateResponse(
                "chat.html",
                {
                    "request": request,
                    "users": users,
                    "chats": chats
    
                }
            )
        else: #wenn login falsch ist dann geht er hier rein
            print(loginCorrect) 
    else:
        print(f'Fehler: {response.status_code}\n{response.content}')

    
