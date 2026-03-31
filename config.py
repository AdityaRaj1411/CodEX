import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Secure API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
API_URL=os.getenv("API_URL")

# Models
GENERATOR_MODEL = "deepseek/deepseek-chat"
CRITIC_MODEL = "deepseek/deepseek-chat"
ANALYZER_MODEL = "mistralai/mistral-7b-instruct"
SELECTOR_MODEL = "gpt-4o-mini"

# Temperatures
GENERATOR_TEMP = 0.4
CRITIC_TEMP = 0.2
SELECTOR_TEMP = 0.1
ANALYZER_TEMP = 0

# System settings
FAST_MODE = True
TIMEOUT = 5