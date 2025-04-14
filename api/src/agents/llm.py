from llama_index.llms.openai import OpenAI
from llama_index.llms.google_genai import GoogleGenAI
from src.core.config import config

llm_gpt = OpenAI(model="gpt-4o-mini", api_key=config.OPENAI_API_KEY)
llm_gemini = GoogleGenAI(model="gemini-1.5-pro", api_key=config.GOOGLE_API_KEY)