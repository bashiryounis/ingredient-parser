import logging
from fastapi import APIRouter, HTTPException, Query
from src.agents.tools import (
    classify_web_content,
    extract_recipe,
    extract_products,
    read_url_content,
)
from src.agents.schema import ContentEnum

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/ingredient_extractor", summary="Classify and extract data from a webpage")
def extract_ingredient(url: str = Query(..., description="The URL to extract content from")):
    """
    Extracts ingredients or product information from the given URL.
    Automatically classifies the page as either 'recipe' or 'product' and invokes the appropriate extractor.
    """
    try:
        page_content = read_url_content(url)

        if not page_content:
            raise HTTPException(status_code=404, detail="No content found at the provided URL.")

        classification = classify_web_content(page_content)

        logger.info(f"Content classified as: {classification}")

        if classification == ContentEnum.recipe:
            result = extract_recipe(page_content)
            return {
                "type": "recipe",
                "data": result.model_dump()  # or result.dict()
            }

        elif classification == ContentEnum.product:
            result = extract_products(page_content)
            return {
                "type": "product",
                "data": result.model_dump()
            }

        else:
            logger.warning(f"Unclassified content for URL: {url}")
            return {
                "type": "other",
                "data": {}
            }

    except Exception as e:
        logger.exception("Failed to extract data from URL")
        raise HTTPException(status_code=500, detail=str(e))
