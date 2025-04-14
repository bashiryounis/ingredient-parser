from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from enum import Enum

class ContentEnum(str, Enum):
    recipe = "recipe"
    product = "product"

class WebClassifier(BaseModel):
    type: ContentEnum


class IngredientBase(BaseModel):
    """Structured information for a single ingredient."""
    name: str
    category: Optional[str] = None

class ExtractProductItem(IngredientBase):
    price: Optional[str] = None  
    quantity: Optional[str] = None 

class ExtractProductList(BaseModel):
    """List of products extracted from a webpage."""
    products: List[ExtractProductItem]


class Step(BaseModel):
    """A single step in the cooking process."""
    order: int
    instruction: str


class NutritionInfo(BaseModel):
    """Nutritional details per serving."""
    calories: Optional[str] = None
    fat: Optional[str] = None
    carbs: Optional[str] = None
    protein: Optional[str] = None

class IngredientRecipe(IngredientBase):
    """Ingredient with optional quantity and preparation details."""
    quantity: Optional[str] = None

class ExtractRecipe(BaseModel):
    """Comprehensive schema for a recipe."""
    title: str
    description: Optional[str]
    ingredients: List[IngredientRecipe]
    steps: List[Step]
    servings: Optional[int]
    prep_time: Optional[str]
    cook_time: Optional[str]
    total_time: Optional[str]
    image_url: Optional[str]
    video_url: Optional[str]
    source_url: Optional[str]
    author: Optional[str]
    cuisine: Optional[str]
    tags: Optional[List[str]]
    nutrition: Optional[NutritionInfo]
    notes: Optional[List[str]]

class ExtractIngredients(BaseModel):
    """Response schema for ingredient extraction."""
    ingredient : Optional[list[IngredientBase]]
    recipe: Optional[ExtractRecipe]