from llama_index.readers.web import FireCrawlWebReader
from src.core.config import config

firecrawl_reader = FireCrawlWebReader(
    api_key=config.FIRECRAWL_API_KEY,
    mode="scrape",
    params={
        'formats': ['markdown'],
        "onlyMainContent":True,
        
    }
)
