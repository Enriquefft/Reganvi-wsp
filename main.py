"""Main API module for the chatbot."""

# ruff: noqa: N803 (Twilio API requires Capitalized variable names)
# ruff: noqa: B008 (fastapi makes use of reusable default function calls)

import logging

from fastapi import FastAPI, Form, Response

from ai import get_response

# Set up logging
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/health")
async def health() -> dict[str, str]:
    """Health check endpoint."""
    return {"msg": "up & running"}


@app.post("/message")
async def reply(
    response: Response,
    Body: str = Form(),
) -> str:
    """Reply to a WhatsApp message from the user."""
    chat_response = get_response(
        Body,
    )

    response.headers["ngrok-skip-browser-warning"] = "any-value"
    # response.headers["User-Agent"] = "Your-Custom-User-Agent"

    logger.info("Received a message from the user")
    logger.info("User message: %s", Body)

    if chat_response is None:
        logger.error("Failed to get a response from the chat system")
        return ""

    return chat_response
