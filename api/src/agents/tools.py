from src.agents.agents import (
    recipe_extractor,
    product_extractor
)
from src.agents.prompts import CLASSIFICATION_PROMPT 
from src.agents.llm import llm_gemini
from src.agents.schema import WebClassifier
from src.agents.reader import firecrawl_reader

def classify_web_content(text: str):
    result = llm_gemini.structured_predict(WebClassifier, CLASSIFICATION_PROMPT, text=text)
    return result.type

def extract_recipe(text: str):
    return recipe_extractor(input_text=text)

def extract_products(text: str):
    return product_extractor(input_text=text)

def read_url_content(url: str):
    docs = firecrawl_reader.load_data(url=url)
    return docs[0].text if docs else ""


