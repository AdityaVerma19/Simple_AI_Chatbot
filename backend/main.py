from fastapi import FastAPI

from models import ChatRequest, ChatResponse
from openai_service import generate_response


app = FastAPI(
    title="Chatbot API",
    description="FastAPI + OpenAI Chatbot",
    version="1.0.0"
)


@app.get("/")
async def root():
    return {
        "message": "Chatbot API is running!"
    }


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):

    response = generate_response(
        request.message
    )

    return ChatResponse(
        response=response
    )