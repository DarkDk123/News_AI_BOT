"""
## command_handlers.py

This file Routes all the commands gives to BOT
using `command_router` from `routers.py`.
"""

from aiogram import filters, types, Bot, F
from aiogram.fsm.context import FSMContext

from .Constant import text_messages as msg  # Constant message texts
from .Constant import custom_markups as cm  # Custom Markups
from .routers import command_router

import sys

sys.path.append("../")
from NewsFetchClasses.Fetch_news import newsAPI


# Start/Restart the Conversation
@command_router.message(filters.Command("start", "restart", ignore_case=True))
async def start(message: types.Message) -> None:
    await message.answer(
        msg.welcome_message(username=message.from_user.first_name),  # type: ignore
        reply_markup=cm.register_or_guest,
    )


# Help command : shows list of commands
@command_router.message(filters.Command("help", ignore_case=True))
async def help_(message: types.Message) -> None:
    await message.answer(msg.help_message())


# Destroys User Data if registered.
@command_router.message(filters.Command("destroy", ignore_case=True))
async def destroy(message: types.Message, state: FSMContext) -> None:
    if not (await state.get_data()).get("is_registered"):
        await message.answer("You are not registered yet!!")

    else:
        await message.answer(
            f"""
            *{(await state.get_data())['name']}*, Do you really want to *destroy your Data*??
            You will need to re-register!
            """,
            reply_markup=cm.destroy_data_or_not,
        )


# destroy_data callback
@command_router.callback_query(F.data == "destroy_yes")
async def destroy_yes(callback: types.CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    await callback.message.answer(  # type: ignore
        f"🚮 Deleted: {data.get('name')} from {data.get('country')} 🙋‍♂️",
    )

    await state.clear()


# destroy_no (cancel) callback
@command_router.callback_query(F.data == "destroy_no")
async def destroy_no(message: types.Message, state: FSMContext) -> None:
    await message.answer("🫂 You Are Safe!!")


# Get list of available News Sources.
@command_router.message(filters.Command("sources", ignore_case=True))
async def news_sources(message: types.Message, state: FSMContext) -> None:
    data = await state.get_data()
    response = newsAPI.get_sources(
        language="en",
        country=msg.countries.get(data.get("country"), "in"),  # type: ignore
    )

    response2 = newsAPI.get_sources(language="en")

    sources = [
        source["name"]
        for source in response.get("sources", []) + response2.get("sources", [])
    ][:10]

    await message.answer(msg.sources(sources))


# Options to support this project.
@command_router.message(filters.Command("support", ignore_case=True))
async def support(message: types.Message) -> None:
    await message.answer(text=msg.support(), reply_markup=cm.support)


# Get the User's saved details.
@command_router.message(filters.Command("mydetails", ignore_case=True))
async def mydetails(message: types.Message, state: FSMContext) -> None:
    try:
        if (await state.get_data()).get("is_registered"):
            await message.answer(msg.details_message(await state.get_data()))
        else:
            await message.answer("You are not registered yet! 😓")
    except Exception as e:
        print(e)


# Invoke Registration Process | Or Register the User
@command_router.message(filters.Command("register", ignore_case=True))
@command_router.callback_query(F.data == "register_callback")
async def register_callback(
    message: types.Message | types.CallbackQuery, state: FSMContext
) -> None:
    full_name = message.from_user.full_name  # type: ignore
    message = message if isinstance(message, types.Message) else message.message  # type: ignore

    if (await state.get_data()).get("is_registered"):
        await message.answer("You are already registered")
        await mydetails(message, state)
        await message.answer(
            text="Want to re-register?",
            reply_markup=cm.registration_markups.get("re-register"),
        )
    else:
        await message.answer(
            text=msg.reg_init(full_name),  # type: ignore
            reply_markup=cm.registration_markups["correct_name_or_not"],
        )


@command_router.callback_query(F.data == "re-register_callback")
async def re_register_callback(
    callback: types.CallbackQuery, state: FSMContext
) -> None:
    await state.clear()
    await register_callback(callback, state)
