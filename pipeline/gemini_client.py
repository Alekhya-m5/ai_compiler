import time

from google import genai

from config import (
    GEMINI_API_KEY,
    MODEL_NAME,
    MAX_RETRIES,
    RETRY_DELAY,
    DEBUG,
)

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found.")

client = genai.Client(api_key=GEMINI_API_KEY)


def generate(prompt: str):

    last_exception = None

    for attempt in range(1, MAX_RETRIES + 1):

        try:

            if DEBUG:
                print(f"\n🔹 Gemini Request ({attempt}/{MAX_RETRIES})")
                print(f"Model : {MODEL_NAME}")

            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt,
            )

            text = response.text

            if not text:
                raise Exception("Empty response from Gemini.")

            return text.strip()

        except Exception as e:

            last_exception = e

            print(f"⚠ {e}")

            if attempt < MAX_RETRIES:

                print(f"Retrying in {RETRY_DELAY} seconds...")

                time.sleep(RETRY_DELAY)

    raise last_exception