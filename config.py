import os
from dotenv import load_dotenv

load_dotenv()

# ==========================
# Gemini Configuration
# ==========================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

MODEL_NAME = "gemini-2.5-flash"

# ==========================
# Retry Configuration
# ==========================

MAX_RETRIES = 3

RETRY_DELAY = 5

# ==========================
# Debug Mode
# ==========================

DEBUG = True