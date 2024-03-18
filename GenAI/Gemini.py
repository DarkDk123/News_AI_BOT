# -------------Imports--------------------------------------
import google.generativeai as genai
from dotenv import load_dotenv  # To load .evn file
import os

# ---------------Other_Imports----------------------------------
from google.generativeai import types


# Load the API Keys from .env file
load_dotenv()

# Generation Configuration for Gemini-Pro
generation_config:dict[str, int|float] = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    # "max_output_tokens": 200,
}


class GeminiAI:
    def __init__(self, model: str = "gemini-pro") -> None:
        # Configure the model
        genai.configure(
            api_key=os.getenv(key="GEMINI_KEY"),
        )

        # Model creation
        self.model = genai.GenerativeModel(model_name=model, generation_config=generation_config)
        self.chat : genai.ChatSession = None

    async def generate_text_async(
        self,
        input_: str,
    ) -> str:
        async_response: types.AsyncGenerateContentResponse = await self.model.generate_content_async(contents=input_)
        return async_response.text

    def _create_chat(self) -> None:
        self.chat = self.model.start_chat()

    async def generate_text_async_chat(self, input_: str) -> str:
        """Generates text asynchronously using a chat instance.

        If a chat instance does not exist, a new one is created.

        Args:
            `input_:` The input text to generate a response for.

        Returns:
            The generated text.
        """

        if not self.chat:
            self._create_chat()

        async_response: types.AsyncGenerateContentResponse = (
            await self.chat.send_message_async(content=input_)
        )

        return async_response.text
