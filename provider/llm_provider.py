import json
import os

from google import genai
from dotenv import load_dotenv
from pydantic import ValidationError

from app.schemas.resume_analysis import ResumeAnalysis

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(
    api_key=api_key
)

def generate(final_prompt: str) -> ResumeAnalysis:


    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=final_prompt,
    config={
        "response_mime_type": "application/json"
    }
    )

    json_text = response.text

    data = json.loads(json_text)

    analysis = ResumeAnalysis(**data)

    return analysis