from fastapi import APIRouter, Request
from twilio.twiml.messaging_response import MessagingResponse
from services.furia_logic import generate_response

router = APIRouter()

@router.post("/webhook/whatsapp")
async def handle_whatsapp(request: Request):
    form_data = await request.form()
    user_message = form_data.get("Body", "")
    bot_response = generate_response(user_message, platform="whatsapp")
    resp = MessagingResponse()
    resp.message(bot_response)
    return str(resp)