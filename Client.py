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
    password: str = Form(...)
):
    print("Username", username)
    print("Password", password)
