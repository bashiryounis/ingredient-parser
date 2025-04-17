from firecrawl import FirecrawlApp
from src.agents.schema import ExtractProductList, ExtractSingleProduct
from src.scripts.prompts import product_prompt, sing_product_prompt
from src.core.config import config

app = FirecrawlApp(api_key=config.FIRECRAWL_API_KEY)

def extract_product_list(url: str):
    """Extracts product information from a webpage using Firecrawl."""
    try:
        result = app.extract(
            [url], 
            {
                'prompt': product_prompt,
                'schema': ExtractProductList.model_json_schema(),   
            })
        return {
            "data": result["data"]
        }
    
    except Exception as e:
        raise Exception(f"Failed to extract data from URL: {e}")

def extract_single_product(url: str):
    """Extracts a single product information from a webpage using Firecrawl."""
    try:
        result = app.extract(
            [url], 
            {
                'prompt': sing_product_prompt,
                'schema': ExtractSingleProduct.model_json_schema(),   
            })
        return {
            "data": result["data"]
        }
    
    except Exception as e:
        raise Exception(f"Failed to extract data from URL: {e}")