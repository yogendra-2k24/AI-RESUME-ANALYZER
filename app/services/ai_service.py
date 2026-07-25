from prompts.resume_prompt import RESUME_PROMPT
from provider.llm_provider import generate

def analyze_text(text: str):

    final_prompt = f"""
        {RESUME_PROMPT}

        Resume:

        {text}
    """

    response = generate(final_prompt)

    return response