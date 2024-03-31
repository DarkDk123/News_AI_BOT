"""
## main.py

It's the Entry point of the "Telegram BOT"
"""

# ______________Helping_Imports___________
import asyncio, logging
import sys

from aiogram import Dispatcher, types

from bot_instance import BOT
from Routing import register_routers

# Main Bot Logger
logger = logging.getLogger("Main_BOT_Logger")


# Dispather Object - Root Router
DP = Dispatcher()
register_routers(DP)  # Registering required Routers


async def main() -> None:
    await DP.start_polling(BOT)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())

    except KeyboardInterrupt:
        logger.info("Interrupted By User!! ⚠️")

    except Exception as e:
        logger.error(f"{e}")
        raise e
    finally:
        logger.info("🤖 BOT Stopped!! ✅")
