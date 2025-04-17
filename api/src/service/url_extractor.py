import logging
from fastapi import APIRouter, HTTPException, Query
from src.agents.tools import (
    read_url_content,
    classify_web_content,
    extract_recipe,
    extract_products,
    extract_ingredient_info
)
from src.agents.schema import ContentEnum
from src.scripts.firecrawl import extract_product_list, extract_single_product

router = APIRouter()
logger = logging.getLogger(__name__)

# @router.get("/extract_with_llm",summary="Extract using HTML scraping and LLM-based classification")
# def extract_ingredient_llm(url: str = Query(..., description="The URL to extract content from")):
#     """Extracts ingredients or product information using LLM and HTML scraping."""
#     try:
#         page_content = read_url_content(url)

#         if not page_content:
#             raise HTTPException(status_code=404, detail="No content found at the provided URL.")

#         classification = classify_web_content(page_content)

#         logger.info(f"Content classified as: {classification}")

#         if classification == ContentEnum.recipe:
#             result = extract_recipe(page_content)
#             return {
#                 "data": result.model_dump()  # or result.dict()
#             }

#         elif classification == ContentEnum.product:
#             result = extract_products(page_content)
#             return {
#                 "data": result.model_dump()
#             }

#         else:
#             result =  extract_ingredient_info(page_content)
#             return {
#                 "data": result.model_dump()
#             }

#     except Exception as e:
#         logger.exception("Failed to extract data from URL")
#         raise HTTPException(status_code=500, detail=str(e))


@router.get("/extract_firecrawl_products",summary="Extract using Firecrawl structured extraction")
def extract_firecrawl_products(
    url: str = Query(..., description="The URL to extract content from")
):
    """Endpoint to extract product or ingredient data using Firecrawl."""
    try:
        return extract_product_list(url)
    except Exception as e:
        logger.exception("Firecrawl-based extraction failed")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/extract_firecrawl_single_product", summary="Extract singe product page strcuture with Firecrawl")
def extract_firecrawl_single_product(    
        url: str = Query(..., description="The URL to extract content from")
):
    """Endpoint to extract product for singe product web page structure  ingredient data using Firecrawl."""
    try:
        return extract_single_product(url)
    except Exception as e:
        logger.exception("Firecrawl-based extraction failed")
        raise HTTPException(status_code=500, detail=str(e))