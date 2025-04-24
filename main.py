from fastapi import FastAPI
from routers import telegram, whatsapp

app = FastAPI(title="FURIA Bot", version="1.0")

app.include_router(telegram.router)
app.include_router(whatsapp.router)

@app.get("/")
def home():
    return {"status": "FURIA Bot Online! 🐆"}