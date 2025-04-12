from llama_index.core.prompts import PromptTemplate

RECIPE_RPOMPT = """
You are a structured data extraction agent. You MUST return data using the provided function schema. Do NOT return freeform text.
You are a helpful assistant that extracts detailed recipe data from the given text. 
The content comes from a cooking blog or recipe website and may contain editorial content, tips, and reviews.

Your job is to extract structured information and return it as a JSON object with the following fields:

Required:
- title: The name of the recipe.
- description: A short summary describing the dish.
- ingredients: A list of ingredients. Each ingredient must include:
  - name: The name of the ingredient (e.g., "all-purpose flour").
  - category: The type/category of the ingredient (e.g., "dairy", "spice", "vegetable"). Leave empty if uncertain.
  - quantity: The amount (e.g., "1 ½ cups", "2 tablespoons", "a pinch"). Leave empty if not specified.

- steps: A list of cooking instructions in order. Each step should include:
  - order: Step number starting from 1.
  - instruction: A single, clear action from the recipe.

Optional:
- servings: Number of servings the recipe makes.
- prep_time: Time to prepare ingredients (e.g., "15 minutes").
- cook_time: Time to cook (e.g., "20 minutes").
- total_time: Combined prep and cook time if available.
- image_url: URL of the main recipe image, if available.
- video_url: URL of a recipe video, if available.
- source_url: Original recipe URL if mentioned.
- author: Name of the person who submitted or wrote the recipe.
- cuisine: The cuisine type (e.g., "Italian", "Middle Eastern").
- tags: Keywords or categories mentioned (e.g., "easy", "low-carb").
- nutrition: Nutrition information per serving if available. Include:
  - calories
  - fat
  - carbs
  - protein
- notes: A list of extra tips, editor remarks, or serving suggestions mentioned in the recipe content.

Important Instructions:
- Avoid extracting editorial content, reviews, or advertisements.
- Focus only on the actual recipe content and ignore unrelated sections.
- If the recipe steps contain sub-steps (e.g., make batter, then fry), preserve this logically in the ordered steps as separate entries.
- If any required fields are missing or cannot be determined, leave them empty.
Here is the text:
{input_text}

Return the result as a well-structured JSON object that matches the field names exactly.
"""


PRODUCT_PROMPT = """
You are a helpful assistant that extracts product information from a given text.

Here is the text:
{input_text}

Please extract **all products** mentioned in the text. For each product, extract the following fields:
- name
- category
- quantity
- price

Respond with a JSON array in the following format:
[
  {
    "name": "...",
    "category": "...",
    "quantity": ...,
    "price": ...
  },
  ...
]

Make sure all objects are valid and follow the schema. Only include products that contain at least a name and category.
"""

CLASSIFICATION_PROMPT = PromptTemplate("""
You are a smart content classifier for web pages.

Your job is to classify the **primary purpose** of the page as one of:

- "recipe": if the main purpose of the content is to teach the reader how to prepare or cook a meal. This includes step-by-step instructions, ingredient lists, and cooking methods. It may mention product brands or links to purchase items, but the focus should be on preparing a dish.

- "product": if the main purpose of the content is to present, describe, compare, review, or sell one or more products. This includes product listings, ecommerce pages, shopping guides, or top-10 comparisons. The content may mention how a product is used in cooking, but it does not provide a full recipe.

- "other": if the content does not fall into either category above. This may include blog posts, opinion pieces, lifestyle articles, or content unrelated to food or products.

Return ONLY the type.

Content:
{text}
""")