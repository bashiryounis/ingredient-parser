product_prompt = """
You are a smart assistant that extracts structured product data from the HTML content of a webpage.

Your task is to extract **all valid products** from the page, no matter where they appear. A product is valid if it has at least a `name` and a `category`. Do **not** skip products in sections like:
- "You May Also Like"
- "Also of Interest"
- "Complete Your Routine"
- "Complete Your [Product Name] Routine"

For each valid product, extract the following fields:

- `name`: The exact name of the product as it appears, including symbols and formatting (required)
- `category`: The category or section it belongs to (can be inferred from the page headings or breadcrumbs) (required)
- `description`: A short tagline or summary describing the product (if available)
- `image_url`: Direct link to the product image (if available)
- `quantity`: Number of available options or formats (e.g. "One size available" → quantity = 1)
- `price`: Price as a float (e.g. "$145.00" → 145.00)

Respond with a JSON array structured like this:

[
  {
    "name": "string",
    "category": "string",
    "description": "string or null",
    "image_url": "string or null",
    "quantity": int or null,
    "price": float or null
  },
  ...
]

Guidelines:
- Search the **entire page**, including main content, product grids, and recommendation areas.
- Only include **complete products**, not partial mentions or references.
- Always return the **name exactly as written**, including special characters or symbols (e.g. “C E Ferulic® with 15% L-Ascorbic Acid”).
- Clean prices and quantities but keep formatting in names.
- If a product appears multiple times, include **only the most complete version** (prefer entries with images, descriptions, or full prices).
"""

sing_product_prompt = """
You are an intelligent data extractor.

Your task is to analyze a product detail webpage and extract structured information that matches the following schema.

Only return a JSON object that conforms to the schema below, even if some fields are missing.

### SCHEMA OVERVIEW (ExtractSingleProduct):

{
  "name": string,
  "price": string | null,
  "quantity": string | null,
  "description": string | null,
  "category": string | null,
  "image_url": string | null,
  "recommended_for": [string] | null,

  "key_ingredients": [
    {
      "name": string | null,
      "purpose": string | null
    }
  ] | null,
  
  "usage_instructions": [
    {
      "step": string | null,
      "title": string | null,
      "action": string | null
    }
  ] | null,

  "routine": [
    {
      "step": string | null,
      "purpose": string | null,
      "product": {
        "name": string | null,
        "price": string | null,
        "quantity": string | null,
        "description": string | null,
        "image_url": string | null,
      }
    }
  ] | null,
}

### INSTRUCTIONS:

1. Read the entire webpage and understand the visual structure (sections, headers, titles, lists).
2. Extract values from visual sections like Highlights, Ingredients, Clinical Claims, How to Use, and Routine.
3. Do not hallucinate or add values not found on the page.
4. For repeated product names (e.g., in Routine), match names exactly.
5. If an array section is not found, return `null`.

Return only the filled JSON object. Do not include any explanations.

"""