import asyncio
import logging
import sys
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.utils import markdown
from aiogram import exceptions as aio_exceptions

sys.path.append("../")
from GenAI.Gemini import GeminiAI

# Bot token can be obtained via https://t.me/BotFather
load_dotenv()
TOKEN: str = os.getenv("TELEGRAM_BOT_TOKEN")

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


# Gemini Setup
AI = GeminiAI()


@dp.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(text=f"Hello, {markdown.hbold(message.from_user.full_name)}!")


@dp.message()
async def AI_response(message: types.Message) -> None:
    """
    Responds to a message with an AI-generated text.

    Args:
        message: The message to respond to.
    """

    try:
        # Send a copy of the received message
        await message.answer(
            text=await AI.generate_text_async_chat(input_=message.text),
            parse_mode="markdown",
        )
    except ValueError:
        # If AI returned None!
        await message.answer(text="Please try again with other input!")
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer(text="Nice try!")
    except aio_exceptions.TelegramBadRequest:
        await message.answer(text="Try Again!!")


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main=main())