import asyncio
import logging
import sys
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types, F, filters
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Filter, Command
from aiogram.utils import markdown
from aiogram import exceptions as aio_exceptions
from aiogram.client.default import DefaultBotProperties

sys.path.append("../")
from GenAI.Gemini import GeminiAI

# Bot token can be obtained via https://t.me/BotFather
load_dotenv()
TOKEN: str = str(os.getenv("TELEGRAM_BOT_TOKEN"))

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


# Gemini Setup
AI = GeminiAI()


@dp.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(
        text=f"Hello, {markdown.bold(message.from_user.full_name)}!",  # type: ignore
        parse_mode="Markdown"
    )


@dp.message(
    Command("create", "bnao"),
)
async def command_create_handler(message: types.Message) -> None:
    await message.reply(text="Created Something ✅")


@dp.message(Command("do"))
# @dp.message(lambda message: "dipesh" in message.text)
async def temp(message: types.Message) -> None:
    replay = await message.answer(
        "Hi there! What's your name?",
        reply_to_message_id=message.message_id,
        reply_markup=types.ForceReply(
            keyboard=[
                [types.KeyboardButton(text="Done")],
                [
                    types.KeyboardButton(text="Button 2"),
                    types.KeyboardButton(text="Button 3"),
                ],
            ],
        ),
    )


@dp.message(F.photo)
async def msg(message: types.Message):
    await message.reply("WOW!! SO ELEGENT!")


@dp.message()
@dp.edited_message()
async def AI_response(message: types.Message) -> None:
    """
    Responds to a message with an AI-generated text.

    Args:
        message: The message to respond to.
    """

    try:
        # Send a copy of the received message
        await message.answer(
            text=await AI.generate_text_async_chat(input_=message.text),  # type:ignore
            parse_mode="markdown",
        )
    except ValueError:
        # If AI returned None!
        await message.answer(text="Please try again with other input!", show_alert=True)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer(text="Nice try!", show_alert=True)
    except aio_exceptions.TelegramBadRequest:
        await message.answer(text="Bad Request 🥲\n Try Again!!")


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(token=TOKEN)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main=main())
