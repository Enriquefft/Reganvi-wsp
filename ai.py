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
    system_message: str = (
        "Eres Reganvi AI, un asistente experto en reciclaje. Tu función es proporcionar a los usuarios consejos precisos, "
        "útiles y amigables sobre cómo reciclar materiales y conectarlos con los recursos de reciclaje adecuados. "
        "Tus respuestas deben ser concisas e informativas, y siempre debes fomentar prácticas sostenibles.\n\n"
    ),
) -> Optional[str]:
    """Get a response from the OpenAI API."""
    user_role_message: ChatCompletionMessageParam = {
        "role": "user",
        "content": user_message,
    }
    system_role_message: ChatCompletionSystemMessageParam | None = {
        "role": "system",
        "content": system_message,
    }

    completion = openai_client.chat.completions.create(
        model="gpt-4o", messages=[system_role_message, user_role_message]
    )
    return completion.choices[0].message.content


def identify_image(user_message: str, material_image_url: str) -> Optional[str]:
    """Analyze the image and return the closest material match in a specific format."""

    system_message = (
        "Eres un asistente experto que analiza imágenes y las compara con el nombre de material más cercano "
        "de la siguiente lista:\n" + formatted_material_data + "\n\n"
        "Para esta tarea, después de analizar la imagen proporcionada, genera una respuesta en el siguiente formato:\n\n"
        "¡Gracias por la foto!\n"
        "Después de analizar los datos, puedo constatar que el material que deseas vender es [MATERIAL_NAME].\n\n"
        "Características:\n\n"
        "    [LISTA DE CARACTERÍSTICAS]\n\n"
        "El precio máximo es de [PRECIO POR KG] el kilo sin IGV ajeno a tu ubicación.\n\n"
        "¡Existen empresas que desean comprar tus materiales! 😁\n\n"
        "Ingresa a nuestra E-Commerce y Conecta 👉 https://reganvi.pe/\n\n\n"
        "Asegúrate de reemplazar los marcadores como [MATERIAL_NAME], [LISTA DE CARACTERÍSTICAS] (esto al analizar la imagen), etc., con los valores apropiados basados en el análisis de la imagen, tampoco olvides incluir el link."
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
