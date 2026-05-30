from openai import OpenAI
from app.config import OPENROUTER_API_KEY, LLM_MODEL_NAME

class AnswerGenerator:
    def __init__(self):
        # OpenRouter uses the exact same client syntax as OpenAI!
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=OPENROUTER_API_KEY,
        )

    def generate_answer(self, query: str, retrieved_passages: list) -> str:
        # 1. Combine the retrieved passages into a single context string
        context_blocks = []
        for i, passage in enumerate(retrieved_passages):
            # Including the Document ID helps the model cite its sources
            context_blocks.append(f"[Document {passage['document_id']}] {passage['text']}")
        
        context_text = "\n\n".join(context_blocks)

        # 2. Advanced Prompt Engineering (Based on RIRAG-2025 methodologies)
        system_prompt = (
            "You are an expert regulatory compliance assistant for the Abu Dhabi Global Market (ADGM). "
            "Your task is to synthesize a comprehensive, highly accurate answer to the user's question. "
            "CRITICAL RULES: "
            "1. You MUST base your answer EXCLUSIVELY on the provided Context Passages. "
            "2. DO NOT introduce any outside information or hallucinate rules. "
            "3. If the provided context does not contain the answer, explicitly state: 'The provided regulatory context does not contain enough information to answer this query.' "
            "4. Ensure all relevant regulatory obligations from the context are integrated without contradiction."
        )

        user_prompt = f"Context Passages:\n{context_text}\n\nQuestion:\n{query}"

        # 3. Call the OpenRouter API
        try:
            response = self.client.chat.completions.create(
                model=LLM_MODEL_NAME,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.1, # Low temperature ensures factual consistency over creativity
                max_tokens=500
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating answer: {str(e)}"