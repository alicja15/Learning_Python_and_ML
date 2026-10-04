"""Configuration and API client setup. Secrets come from the environment only."""

import os

from dotenv import load_dotenv
from openai import OpenAI

GROQ_BASE_URL = "https://api.groq.com/openai/v1"
# Fastest model with clean JSON output in the notebook benchmark (see notebooks/project.ipynb)
DEFAULT_MODEL = "openai/gpt-oss-20b"


def get_model() -> str:
    load_dotenv()
    return os.getenv("GROQ_MODEL", DEFAULT_MODEL)


def get_client() -> OpenAI:
    """Create a Groq client (OpenAI-compatible) using GROQ_API_KEY from .env / environment."""
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GROQ_API_KEY is not set. Copy .env.example to .env and add your key."
        )
    return OpenAI(base_url=GROQ_BASE_URL, api_key=api_key)
