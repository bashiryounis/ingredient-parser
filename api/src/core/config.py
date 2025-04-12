import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

load_dotenv(verbose=True)

class Config(BaseSettings):
    GOOGLE_API_KEY:str = Field(env="GOOGLE_API_KEY")
    OPENAI_API_KEY:str = Field(env="OPENAI_API_KEY")
    FIRECRAWL_API_KEY:str = Field(env="FIRECRAWL_API_KEY")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

config = Config()
