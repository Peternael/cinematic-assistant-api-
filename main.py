from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models.schemas import UserChoice
from services.assistant_service import (
    get_reply,
    get_start_message
)

app = FastAPI(
    title="AI Cinematic Assistant",
    version="1.0.0"
)

# Flutter Access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def home():

    return {
        "status": "AI Cinematic Assistant Running"
    }


@app.get("/assistant/start")
async def start_chat():

    return get_start_message()


@app.post("/assistant/reply")
async def assistant_reply(data: UserChoice):

    return get_reply(data.choice)