"""Yquando backend env keys & settings module."""

import os
from typing import Optional


def get_required_env[T](env_name: str, default_value: Optional[str] = None) -> str:
    """Validate and return an environmental variable."""
    env_var = os.getenv(env_name)

    if env_var is None:
        if default_value is not None:
            return default_value
        error_message = f"{env_name} environmental variable not found."
        raise RuntimeError(error_message)

    return env_var


PROJECT_NAME = get_required_env("PROJECT_NAME")

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
TWILIO_ACCOUNT_SID = get_required_env("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = get_required_env("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = get_required_env("TWILIO_NUMBER")
TWILIO_MESSAGING_SERVICE_SID = get_required_env("TWILIO_MESSAGING_SERVICE_SID")

OPENAI_API_KEY = get_required_env("OPENAI_API_KEY")
