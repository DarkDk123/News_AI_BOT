# -------------Imports--------------------------------------
import google.generativeai as genai
import google.ai.generativelanguage as glm

# from dotenv import load_dotenv  # To load .evn file
import os

# ---------------Other_Imports----------------------------------
from google.generativeai import types

# Generation Configuration for Gemini-Pro
generation_config = types.GenerationConfig(
    temperature=0.9,
    top_k=1,
    top_p=1,
    # max_output_tokens=200
)


class GeminiAI:
    def __init__(self, model: str = "gemini-pro") -> None:
        # Configure the model
        genai.configure(
            api_key=os.getenv(key="GEMINI_KEY"),
        )

        # Model creation
        self.__model = genai.GenerativeModel(
            model_name=model, generation_config=generation_config
        )
        self.chat: genai.ChatSession = None  # type: ignore

    async def generate_text_async(
        self, input_: str, tools: list[glm.Tool]
    ) -> types.AsyncGenerateContentResponse:
        """Generates `Function call` asynchronously independently of Chat Session.

        Args:
            `input_:` The input text to generate a response for.
            `tools`: List of available `function definitions`
        Returns:
            The Generated `Function Call` or sometimes `text` as Response object
        """

        async_response: types.AsyncGenerateContentResponse = (
            await self.__model.generate_content_async(contents=input_, tools=tools)
        )
        return async_response

    def create_new_chat(self) -> genai.ChatSession:
        """Creating new `chatSession` for each user."""
        return self.__model.start_chat()

    async def generate_text_async_chat(
        self, input_: str, chat: genai.ChatSession, tools: list[glm.Tool]
    ) -> types.AsyncGenerateContentResponse:
        """Generates `Function call` asynchronously using a chat instance.

        Args:
            `input_:` The input text to generate a response for.
            `chat`: Chat Session instance unique to each user.
            `tools`: List of available `function definitions`
        Returns:
            The Generated `Function Call` or sometimes `text`
        """

        async_response: types.AsyncGenerateContentResponse = (
            await chat.send_message_async(content=input_, tools=tools)
        )

        return async_response


# Gemini client Object
AI = GeminiAI()
