from llama_index.core.prompts import PromptTemplate

RECIPE_RPOMPT = """
You are a structured data extraction agent. You MUST return data using the provided function schema. Do NOT return freeform text.
You are a helpful assistant that extracts detailed recipe data from the given text. 
The content comes  recipe website and may contain editorial content, tips, and reviews.

Your job is to extract structured information and return it as a JSON object with the following fields:

Required:
- title: The name of the recipe.
- description: A short summary describing the dish.
- ingredients: A list of ingredients. Each ingredient must include:
  - name: The name of the ingredient (e.g., "all-purpose flour").
  - category: The type/category of the ingredient (e.g., "grain", "herb", "wax"). Leave empty if uncertain.
  - quantity: The amount (e.g., "1 ½ cups", "2 tablespoons", "a pinch"). Leave empty if not specified.

- steps: A list of instructions in order. Each step should include:
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

Respond with a JSON object containing a single key "products". The value of "products" should be an array of JSON objects, where each object represents a product in the following format:
{{
  "name": "...",
  "category": "...",
  "quantity": ...,
  "price": ...
}}

Example Response Format:
{{
  "products": [
    {{
      "name": "Example Product 1",
      "category": "Example Category A",
      "quantity": "1 unit",
      "price": "10.99"
    }},
    {{
      "name": "Example Product 2",
      "category": "Example Category B",
      "quantity": "500g",
      "price": "5.49"
    }}
  ]
}}

Make sure the entire response is a single valid JSON object and the product objects within the array are valid and follow the schema. Only include products that contain at least a name and category.
"""

OTHER_CONTENT_PROMPT = """
You are a helpful assistant that extracts ingredients information from a given text from web pgae.

Here is the text from the web page:
{input_text}

Please scan the text and extract any information related to ingredients and any structured recipe-like content that might be present. Structure your output as a JSON object with the following optional fields:

Optional:
- mentioned_ingredients: A list of ingredients explicitly discussed or mentioned on the page. Each ingredient should be represented as a JSON object with the following keys:
  - name (string, required): The name of the ingredient.
  - category (string, optional): The type or category of the ingredient (e.g., "chemical", "plant extract").

- embedded_recipe: If a structured set of ingredients and instructions (resembling a recipe) is found on the page, extract it according to the following schema (leave empty or null if no such structure is found):
  {{
    "title": (string, optional): The title or name associated with the instructions.
    "description": (string, optional): A brief summary of what the instructions are for.
    "ingredients": (array of objects, optional): A list of ingredient objects, where each object has:
      - "name": (string, required)
      - "category": (string, optional)
      - "quantity": (string, optional)
    "steps": (array of objects, optional): A list of step objects, where each object has:
      - "order": (integer, optional): The step number (if available).
      - "instruction": (string, required): A single action or instruction.
    "notes": (array of strings, optional): Any additional notes or information related to the instructions.
  }}

Return the result as a single valid JSON object that matches the structure described above. If no ingredients or recipe-like content are found, return an empty JSON object: `{}`.
"""


CLASSIFICATION_PROMPT = PromptTemplate("""
You are a smart content classifier for web pages.

Your job is to classify the **primary purpose** of the page as one of:

- "recipe": if the main purpose of the content is to provide a detailed guide on how to prepare or create something by combining a list of ingredients or components through a series of steps. This could include food recipes, health remedies, DIY mixtures, etc. The key elements are a list of required components and sequential instructions for their combination or use.

- "product": if the main purpose of the content is to present, describe, compare, review, or sell one or more products. Mentions of ingredients might be in the context of product composition or usage.

- "blog": if the main purpose of the content is to share information, stories, opinions, or other content that is not primarily a recipe or product listing. This can include general discussions about ingredients, food science, wellness tips, without providing a specific, step-by-step guide to create something.

Return ONLY the type.

Content:
{text}
""")