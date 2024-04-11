"""
## menu_router.py

This file contains `handlers` for "Main menu"

Also used a `FSM` for few handlers.
"""

from aiogram import F, types
from aiogram.fsm.context import FSMContext

from .routers import menu_router
from .fsm import MainMenu

from .Constant import text_messages as msg
from .Constant import custom_markups as cm


@menu_router.callback_query(F.data == "guest_callback")
async def start_menu(callback: types.CallbackQuery) -> None:
    message = callback.message

    await message.answer(  # type: ignore
        text="*Main Menu*", reply_markup=cm.menu_markups.get("main_menu")
    )
