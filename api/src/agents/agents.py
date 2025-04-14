from llama_index.core.program import LLMTextCompletionProgram
from src.agents.schema import (
    ExtractRecipe,
    ExtractProductList,
    ExtractIngredients,
)
from src.agents.prompts import (
    RECIPE_RPOMPT,
    PRODUCT_PROMPT,
    OTHER_CONTENT_PROMPT,

)
from src.agents.llm import llm_gemini


recipe_extractor = LLMTextCompletionProgram.from_defaults(
    output_cls=ExtractRecipe,
    prompt_template_str=RECIPE_RPOMPT,
    llm=llm_gemini,
  )

product_extractor = LLMTextCompletionProgram.from_defaults(
    output_cls=ExtractProductList,
    prompt_template_str=PRODUCT_PROMPT,
    llm=llm_gemini,
)

ingredient_info_extractor = LLMTextCompletionProgram.from_defaults(
    output_cls=ExtractIngredients,
    prompt_template_str=OTHER_CONTENT_PROMPT,
    llm=llm_gemini,
)
