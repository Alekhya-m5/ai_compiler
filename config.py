import os
from dotenv import load_dotenv

load_dotenv()

# ==========================
# LLM Configuration
# ==========================

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

MODEL_NAME = "llama-3.3-70b-versatile"

# ==========================
# Retry Configuration
# ==========================

MAX_RETRIES = 3

RETRY_DELAY = 5

# ==========================
# Debug Mode
# ==========================

DEBUG = True

# ==========================
# Mock Mode
# ==========================

USE_MOCK_GENERATORS = False