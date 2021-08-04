from JsonDB import JsonDB
from fastapi import FastAPI
from BaseModelForm import AppForm
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"messgage": "content"}


@app.post("/form")
async def addAppForm(appForm: AppForm):
    db = JsonDB()
    db.insert(appForm.dict())
    return {"status": "202", "statusText": "Registrado con éxito"}


@app.get("/forms")
def get_app_forms():
    db = JsonDB()
    data = db.get_all_appforms()
    return data
