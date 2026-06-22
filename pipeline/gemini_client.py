import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate(prompt):

    retries = 3

    for attempt in range(retries):

        try:

            response = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=prompt
            )

            return response.text

        except Exception as e:

            print(f"Retry {attempt+1}/{retries}")

            if attempt == retries - 1:
                raise e

            time.sleep(5)