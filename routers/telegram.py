from fastapi import APIRouter, Request
from services.furia_logic import generate_response

router = APIRouter()

@router.post("/webhook/telegram")
async def handle_telegram(request: Request):
    data = await request.json()
    chat_id = data["message"]["chat"]["id"]
    user_message = data["message"]["text"]
    bot_response = generate_response(user_message, platform="telegram")
    return {"method": "sendMessage", "chat_id": chat_id, "text": bot_response}