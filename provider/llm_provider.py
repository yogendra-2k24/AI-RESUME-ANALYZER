import json
import os

from openai import OpenAI
from dotenv import load_dotenv
from pydantic import ValidationError

from app.schemas.resume_analysis import ResumeAnalysis

load_dotenv()

api_key = os.getenv("OPEN_API_KEY")

client = OpenAI(
    api_key=api_key
)

def generate(final_prompt: str) -> ResumeAnalysis:

    try:

        response = client.responses.create(
            model="gpt-5.5",
            input=final_prompt
        )

        json_text = response.output_text

        data = json.loads(json_text)

        analysis = ResumeAnalysis(**data)

        return analysis

    except json.JSONDecodeError:
        raise

    except ValidationError:
        raise

    except Exception:
        raise