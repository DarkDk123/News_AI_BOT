"""
## registration_handlers.py

This file contains all `handlers` relating to `registration`.
It uses a `FSM` to transition between different states.
"""

from aiogram import filters, types, Bot, F
from aiogram.fsm.context import FSMContext

from .Constant import text_messages as msg
from .Constant import custom_markups as cm

from .routers import registration_router as rr
from .fsm import Registration, MainMenu
from .menu_handlers import start_menu

from config.settings import ADMIN_USER
import re


@rr.callback_query(F.data == "correct_name_yes")
async def correct_name(callback: types.CallbackQuery, state: FSMContext) -> None:
    await state.update_data(name=callback.from_user.full_name)  # type: ignore

    await callback.message.answer(msg.locations(), reply_markup=cm.registration_markups["location_prompt"])  # type: ignore
    await state.set_state(Registration.location_prompt)


@rr.callback_query(F.data == "correct_name_no")
async def correct_name_(callback: types.CallbackQuery, state: FSMContext) -> None:
    await callback.message.answer("🧐 Well, then what should we call you??")  # type: ignore
    await state.set_state(Registration.name)


@rr.message(Registration.name)
async def name(message: types.Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    await state.set_state(Registration.location_prompt)
    await message.reply(
        text=msg.locations(),
        reply_markup=cm.registration_markups["location_prompt"],
    )


@rr.message(Registration.location_prompt)
@rr.callback_query(F.data.startswith("r_country:"))
async def country_callback(callback: types.CallbackQuery, state: FSMContext) -> None:
    message = callback.message

    if isinstance(message, types.Message):
        country = callback.data.removeprefix("r_country:")  # type: ignore
        await state.update_data(country=country.title() if country != "None" else None)

        await message.reply(
            text="Now, Please Enter your favourite topics Separated by <b>coma (,)</b>",
        )

        await state.set_state(Registration.sel_news_topics)


@rr.message(Registration.location_prompt)
@rr.callback_query(F.data == "r_country_man")
async def r_country_man(callback: types.CallbackQuery, state: FSMContext) -> None:
    await state.set_state(Registration.sel_countries_manually)

    editable_message = await callback.message.answer(  # type: ignore
        text=msg.sel_countries()
    )

    await callback.message.delete()  # type: ignore
    await state.update_data(
        # For navigation main_message should be edited only
        main_message_id=editable_message.message_id
    )


@rr.message(Registration.sel_countries_manually)
async def select_country(message: types.Message, state: FSMContext, bot: Bot) -> None:
    try:
        data = await state.get_data()
        # Get message to edit
        main_message = await bot.edit_message_text(
            "Just Wait🌚",
            message_id=data.get("main_message_id"),
            chat_id=message.chat.id,
        )
        country_id = int(message.text) if message.text.isnumeric() else None  # type: ignore

        if (not country_id) or 1 > country_id or country_id > 17:
            try:
                await main_message.edit_text(  # type: ignore
                    text="<b>Please, Enter valid Choice</b>\n" + msg.sel_countries()
                )
            except Exception as e:
                await message.answer(str(e))

        else:
            await state.update_data(country=msg._get_country(country_id))

            await message.answer(
                text="Now, Please Enter your favourite topics Separated by <b><code>coma (,)</code></b>",
            )

            await state.set_state(Registration.sel_news_topics)

    except Exception as e:
        await message.answer(
            f"💔Something Went Wrong!!\nPlease Contact admin ({ADMIN_USER}) with Screenshots."
        )

    else:
        await message.delete()


@rr.message(Registration.sel_news_topics)
async def select_news_topics(message: types.Message, state: FSMContext) -> None:
    try:
        topics = list(map(lambda x: x.casefold().strip() if len(x) > 3 else x.upper().strip(), message.text.split(",")))  # type: ignore
        if not topics:
            await message.answer(
                "💀 Please enter valid topic string \ni.e. <code>AI, Data, Something</code>"
            )
        elif not all(map(lambda x: re.match(re.compile(r"^[a-zA-Z\s]*$"), x), topics)):
            print(topics)
            await message.answer(
                "Topics should be alphabet only!\n Separated by <code>','</code>"
            )

        else:
            await state.update_data(topics=topics, is_registered=True)
            await state.set_state(MainMenu.get_custom_prompt)
            await message.answer("<b>Registration Complete!!✅</b>")

            # Now we have to start main menu
            callback = types.CallbackQuery(
                data="menu_callback",
                id="unique_",
                chat_instance=message.chat.type,
                from_user=message.from_user,  # type: ignore
                message=message,
            )

            await start_menu(callback)

    except:
        await message.delete()
        message = await message.answer("Something Went Wrong, try Again!!")

    finally:
        await message.delete()
