import time
import logging
import re

from django.conf import settings
from google import genai
from google.genai import types

logger = logging.getLogger(__name__)


class GeminiServiceError(Exception):
    pass


class GeminiRateLimitError(GeminiServiceError):
    pass


def get_error_code(error):

    return getattr(error, "code", None)


def get_retry_seconds(error):

    message = str(error)

    patterns = [
        r"retry in ([0-9.]+)s",
        r'"retryDelay":\s*"([0-9]+)s"'
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            message,
            re.IGNORECASE
        )

        if match:
            return int(float(match.group(1))) + 2

    return 60


def generate_with_model(client, model, prompt, system_instruction):

    delays = [2, 5, 10]

    for attempt in range(3):

        try:

            response = client.models.generate_content(
                model=model,
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction,
                    temperature=0.85,
                    max_output_tokens=4000
                )
            )

            if not response.text:
                raise GeminiServiceError(
                    "Gemini returned an empty response."
                )

            return response.text.strip()

        except Exception as error:

            code = get_error_code(error)

            # Handle rate limits separately.
            if code == 429:

                retry_after = get_retry_seconds(error)

                raise GeminiRateLimitError(
                    f"Gemini request limit reached. "
                    f"Please wait approximately {retry_after} "
                    f"seconds before trying again."
                )

            # Retry temporary server errors.
            if code == 503:

                logger.warning(
                    "Gemini 503 error. Attempt %s",
                    attempt + 1
                )

                if attempt < 2:
                    time.sleep(delays[attempt])
                    continue

                raise GeminiServiceError(
                    f"Model {model} is temporarily unavailable."
                )

            logger.exception(
                "Gemini API request failed."
            )

            raise GeminiServiceError(
                f"Gemini API error: {error}"
            ) from error


def generate_song_lyrics(data):

    if not settings.GEMINI_API_KEY:
        raise GeminiServiceError(
            "Gemini API key is missing."
        )

    client = genai.Client(
        api_key=settings.GEMINI_API_KEY
    )

    system_instruction = """
    You are MelodyVerse AI, a professional songwriter.

    Create original, meaningful and emotionally engaging lyrics.

    Prioritize storytelling over forced rhyming.

    Maintain narrative continuity.

    Avoid repetitive and generic expressions.

    Create memorable choruses.

    Follow the requested language naturally.

    Preserve emotional depth and lyrical flow.

    Return properly structured song lyrics only.
    """

    prompt = f"""
    SONG TITLE:
    {data.get('song_title') or 'Create a suitable title'}

    STORY:
    {data['creative_prompt']}

    LANGUAGE: {data['language']}
    GENRE: {data['genre']}
    MOOD: {data['mood']}
    VOCAL: {data['vocal']}
    DURATION: {data['duration']}
    STRUCTURE: {data['structure']}

    ADDITIONAL INSTRUCTIONS:
    {data.get('instructions', '')}

    Create a complete original song.
    """

    models = [
        settings.GEMINI_MODEL,
        *settings.GEMINI_FALLBACK_MODELS
    ]

    try:

        for model in models:

            try:

                logger.info(
                    "Trying Gemini model: %s",
                    model
                )

                result = generate_with_model(
                    client,
                    model,
                    prompt,
                    system_instruction
                )

                return result

            except GeminiRateLimitError:
                # Never switch models just to bypass a rate limit.
                raise

            except GeminiServiceError as error:

                logger.warning(
                    "Model %s failed: %s",
                    model,
                    error
                )

                continue

        raise GeminiServiceError(
            "All configured Gemini models are unavailable."
        )

    finally:
        client.close()