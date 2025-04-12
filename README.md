# 🧠 Ingredient Parser

**Ingredient Parser** is an intelligent web content extractor powered by LLMs (Google Gemini via LlamaIndex). It automatically classifies web pages as either **recipes**, **products**, or **other**, and then extracts structured information accordingly.

Built for food-related sites, shopping guides, and cooking blogs, this service provides clean structured JSON output for recipes and products.

---

## 🚀 Features

- ✅ Automatic content classification (`recipe`, `product`, `other`)
- 🍝 Extracts detailed recipe data: ingredients, steps, nutrition, etc.
- 🛒 Extracts product listings: name, price, category, quantity
- 🌐 Supports content extraction from public URLs
- 🔥 Powered by [LlamaIndex](https://www.llamaindex.ai/) + [Google Gemini](https://deepmind.google/technologies/gemini/)

---

## 📁 Project Structure

```
ingredient-parser/
├── api/                    # API container and dependencies
│   ├── Dockerfile
│   ├── dev_start.sh
│   ├── poetry.lock
│   ├── pyproject.toml
│   └── src/
│       ├── agents/         # Core LLM logic and schemas
│       │   ├── agents.py
│       │   ├── llm.py
│       │   ├── prompts.py
│       │   ├── reader.py
│       │   ├── schema.py
│       │   └── tools.py
│       ├── core/           # Config and logger setup
│       │   ├── config.py
│       │   └── logger_config.py
│       ├── main.py         # FastAPI entrypoint
│       └── service/
│           └── url_extractor.py  # Webpage extractor endpoint
├── docker-compose.yaml     # Full-stack Docker orchestration
├── Makefile
├── docs/
│   └── ingredient-parser.ipynb
└── README.md
```

---

## 📦 Setup

### ⚙️ Requirements

- Python 3.12
- Poetry
- Docker (for containerized setup)
- LLM API Key (Google Gemini)


### 🔧 Local Development

1. **Install dependencies**

```bash
cd api
poetry install
```

2. **Start the development server**

```bash
sudo make dev
```

3. Open your browser at: [http://localhost:8000/docs](http://localhost:8000/docs) for the interactive API docs.


---
Absolutely! Here's a clean and professional **API endpoint table** you can drop into your `README.md` to document the `/ingredient_extractor` route:

---

### 🧪 API Endpoints

| Endpoint                  | Method | Description                                              | Query Params       | Response Type |
|---------------------------|--------|----------------------------------------------------------|--------------------|----------------|
| `/ingredient_extractor`   | GET    | Classifies a web page and extracts structured content.   | `url` (required): URL of the web page | JSON            |

---

### 📥 Example Request

```bash
curl "http://localhost:8000/ingredient_extractor?url=https://example.com/recipe/chocolate-cake"
```

---

### 📤 Example Response

#### For Recipes:

```json
{
  "type": "recipe",
  "data": {
    "title": "Chocolate Cake",
    "ingredients": [
      {
        "name": "cocoa powder",
        "quantity": "1/2 cup",
        "category": "baking"
      }
    ],
    "steps": [
      {
        "order": 1,
        "instruction": "Preheat the oven to 350°F."
      }
    ]
    // ... more fields like prep_time, nutrition, etc.
  }
}
```

#### For Products:

```json
{
  "type": "product",
  "data": {
    "products": [
      {
        "name": "KitchenAid Stand Mixer",
        "category": "appliance",
        "quantity": 1,
        "price": 299.99
      }
    ]
  }
}
```

#### For Other (unclassified):

```json
{
  "type": "other",
  "data": {}
}
```

---


## 🧱 LLM Integration

This project uses:

- `structured_predict` for classification
- `LLMTextCompletionProgram` for recipe/product extraction
- Prompts are modular and live in `src/agents/prompts.py`

---

## ✨ Future Ideas

- [ ] Support multi-recipe pages
- [ ] Add PDF parsing support
- [ ] Use vector memory for reclassification
- [ ] Add confidence scores
