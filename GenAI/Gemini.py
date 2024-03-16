# -------------Imports--------------------------------------
import google.generativeai as genai
from dotenv import load_dotenv  # To load .evn file
import os

# ---------------Other_Imports----------------------------------
from google.generativeai.types import generation_types


# Load the API Keys from .env file
load_dotenv()

# Generation Configuration for Gemini-Pro
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 200,
}


class GeminiAI:
    def __init__(self, model: str = "gemini-pro") -> None:
        # Configure the model
        genai.configure(
            api_key=os.getenv("GEMINI_KEY"),
        )

        # Model creation
        self.model = genai.GenerativeModel(model, generation_config=generation_config)

    def generate_text(
        self,
        input_: str,
    ) -> generation_types.GenerateContentResponse:
        return self.model.generate_content(input_)

