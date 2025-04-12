import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from src.core.logger_config import setup_logging
from src.service.url_extractor import router as url_extractor_router
# ----------------------------------------
# Logging setup
# ----------------------------------------
setup_logging()
logger = logging.getLogger(__name__)

# ----------------------------------------
# App metadata
# ----------------------------------------
app = FastAPI(
    debug=True,
    title="Intelligent Ingredient Extractor",
    description=(
        "A FastAPI application for classifying and extracting structured ingredient "
        "or product data from web content.\n\n"
        "Use this service to analyze and classify web page content for recipe or product data."
    ),
    version="1.0.0",
)

# ----------------------------------------
# CORS configuration
# ----------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],            # Allow requests from any origin
    allow_credentials=True,
    allow_methods=["*"],            # Allow all HTTP methods
    allow_headers=["*"],            # Allow all HTTP headers
)

# ----------------------------------------
# Root redirection to Swagger UI
# ----------------------------------------
@app.get("/", include_in_schema=False)
def root_redirect():
    """
    Redirects the root URL to the API documentation UI.
    """
    return RedirectResponse(url="/docs")

# ----------------------------------------
# Routers (uncomment and register your endpoints here)
# ----------------------------------------
# from src.routers.repo import repo_router
app.include_router(
    url_extractor_router,
    prefix="/extract",
    tags=["Ingredient & Recipe Extraction"]
)
