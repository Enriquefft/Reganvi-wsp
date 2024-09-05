"""OpenAI API client for chat completions."""

from typing import TYPE_CHECKING

from openai import OpenAI

if TYPE_CHECKING:
    from openai.types.chat import (
        ChatCompletionMessageParam,
        ChatCompletionSystemMessageParam,
    )

from typing import Optional

from data import formatted_material_data
from env import OPENAI_API_KEY

openai_client = OpenAI(api_key=OPENAI_API_KEY)


def get_response(
    user_message: str,
    system_message: Optional[str] = None,
) -> Optional[str]:
    """Get a response from the OpenAI API."""
    user_role_message: ChatCompletionMessageParam = {
        "role": "user",
        "content": user_message,
    }
    system_role_message: ChatCompletionSystemMessageParam | None = (
        {"role": "system", "content": system_message} if system_message else None
    )

    completion = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[system_role_message, user_role_message]
        if system_role_message
        else [user_role_message],
    )
    return completion.choices[0].message.content


def identify_image(user_message: str, material_image_url: str) -> Optional[str]:
    """Analyze the image and return the closest material match in a specific format."""
    # Step 2: Prepare the prompt with the original task and desired response structure
    system_message = (
        "You are an expert assistant that analyzes images and matches them with the closest material name "
        "from the following list:\n" + formatted_material_data + "\n\n"
        "For this task, after analyzing the provided image, generate a response in the following format:\n\n"
        "Here is the text from the image you provided:\n\n"
        "¡Gracias por la foto!\n"
        "Después de analizar los datos, puedo constatar que el material al que deseas vender es [MATERIAL_NAME].\n\n"
        "Características:\n\n"
        "    [LIST OF CHARACTERISTICS]\n\n"
        "El precio máximo es de [PRICE PER KG] el kilo sin IGV ajeno a tu ubicación.\n\n"
        "¡Existen empresas que desean comprar tus materiales! 😁\n\n"
        "Ingresa a nuestra E-Commerce y Conecta 👉 https://reganvi.pe/\n\n"
        "Ensure that you replace placeholders like [MATERIAL_NAME], [LIST OF CHARACTERISTICS] (this one by ananlyzing the image), etc., with appropriate values based on the image analysis."
    )

    # Step 4: Generate the system and user messages
    user_role_message: ChatCompletionMessageParam = {
        "role": "user",
        "content": [
            {"type": "text", "text": user_message},
            {
                "type": "image_url",
                "image_url": {"url": material_image_url},
            },
        ],
    }

    system_role_message: ChatCompletionSystemMessageParam = {
        "role": "system",
        "content": system_message,
    }

    # Step 5: Call GPT-4o to process the request
    completion = openai_client.chat.completions.create(
        model="gpt-4o", messages=[system_role_message, user_role_message]
    )

    # Step 6: Extract and return the response
    return completion.choices[0].message.content
