"""Main API module for the chatbot."""

# ruff: noqa: N803 (Twilio API requires Capitalized variable names)
# ruff: noqa: B008 (fastapi makes use of reusable default function calls)

import logging

from fastapi import FastAPI, Form

from ai import get_image_response, get_response

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
    Body: str | None = Form(),
    MediaUrl0: str | None = Form(None),
) -> str:
    """Reply to a WhatsApp message from the user."""
    chat_response = (
        get_response(
            Body,
        )
        if Body
        else get_image_response(MediaUrl0)
        if MediaUrl0
        else None
    )

    logger.info("Received a media message from the user")
    logger.info("Media message: %s", MediaUrl0)

    logger.info("Received a message from the user")
    logger.info("User message: %s", Body)

    if chat_response is None:
        logger.error("Failed to get a response from the chat system")
        return ""

    return chat_response
