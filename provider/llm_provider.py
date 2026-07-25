from openai import OpenAI
from app.services.ai_service import analyze_text

client = OpenAI()

def generate(final_prompt: str):

    response = client.responses.create(
        model="gpt-5.5",
        input=final_prompt
    )

    return response.output_text