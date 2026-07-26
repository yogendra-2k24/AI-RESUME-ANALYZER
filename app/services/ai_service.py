from prompts.resume_prompt import RESUME_PROMPT
from provider.llm_provider import generate
from app.schemas.resume_analysis import ResumeAnalysis

def analyze_text(text: str) -> ResumeAnalysis:

    final_prompt = f"""
        {RESUME_PROMPT}

        Resume:

        {text}
    """

    analysis = generate(final_prompt)

    return analysis