"""
## menu_router.py

This file contains `handlers` for "Main menu"

Also used a `FSM` for few handlers.
"""

from aiogram import F, types, Bot
from aiogram.fsm.context import FSMContext

from .routers import menu_router
from .fsm import MainMenu

from .Constant import text_messages as msg
from .Constant import custom_markups as cm
from config.settings import ADMIN_USER


@menu_router.callback_query(F.data == "menu_callback")
async def start_menu(callback: types.CallbackQuery, bot: Bot) -> None:
    message = callback.message

    if isinstance(message, types.Message):
        if "TeleNews Bot" in message.text:  # type: ignore
            await message.answer(
                text="*Main Menu*", reply_markup=cm.menu_markups.get("main_menu")
            )
        else:
            await message.edit_text("*Main Menu*")
            await message.edit_reply_markup(
                reply_markup=cm.menu_markups.get("main_menu")
            )


@menu_router.callback_query(F.data == "sel_topics_callback")
async def sel_topics_callback(callback: types.CallbackQuery) -> None:
    message = callback.message

    if isinstance(message, types.Message):
        await message.edit_text("*Select Topics*")
        await message.edit_reply_markup(
            text="Select One Topic!", reply_markup=cm.menu_markups.get("sel_topics")
        )


@menu_router.callback_query(F.data == "sel_custom_news_topics")
async def sel_custom_news_topics_callback(
    callback: types.CallbackQuery, state: FSMContext
) -> None:
    await state.set_state(MainMenu.sel_custom_news_topics)

    editable_message = await callback.message.answer(  # type: ignore
        text="Now, Please Enter your favourite topics Separated by *coma (,)*"
    )

    await callback.message.delete()  # type: ignore
    await state.update_data(
        # For navigation main_message should be edited only
        main_message_id=editable_message.message_id
    )


@menu_router.message(MainMenu.sel_custom_news_topics)
async def select_news_topics(
    message: types.Message, state: FSMContext, bot: Bot
) -> None:
    try:
        data = await state.get_data()
        # Get message to edit
        main_message = await bot.edit_message_text(
            "Just Wait🌚",
            message_id=data.get("main_message_id"),
            chat_id=message.chat.id,
        )
        topics = list(map(lambda x: x.casefold().strip(), message.text.split(",")))  # type: ignore
        if not topics:
            await main_message.edit_text(  # type: ignore
                "Please enter valid topic string \ni.e. AI, Data, Something"
            )
        # TODO: Logical Error, allow isalpha to have white spaces also
        elif not all(map(str.isalpha, topics)):
            await main_message.edit_text(  # type: ignore
                "Topics should be alphabet only!\n Separated by ','"
            )

        else:
            tempDict: dict = data.get("tempDict", {})
            tempDict.update(topics=topics)
            await state.update_data(tempDict=tempDict)

            callback = types.CallbackQuery(
                id="done",
                from_user=message.from_user,  # type: ignore
                chat_instance=message.chat.type,
                message=main_message,  # type: ignore
                data="sel_country_callback",
            )

            # await message.delete()
            await state.set_state(None)
            await sel_country_callback(callback, state)

    except Exception as e:
        await message.answer(
            f"Something Went Wrong!!\nContact admin ({ADMIN_USER}) with Screenshot"
        )

    else:
        await message.delete()


@menu_router.callback_query(F.data == "sel_country_callback")
@menu_router.callback_query(F.data.startswith("topic:"))
async def sel_country_callback(
    callback: types.CallbackQuery, state: FSMContext
) -> None:
    message = callback.message

    if isinstance(message, types.Message):
        if callback.data.startswith("topic:"):  # type:ignore
            topic = callback.data.removeprefix("topic:").casefold()  # type: ignore
            await state.update_data(tempDict={"topics": topic})

        await message.edit_text(text="Select Country")
        await message.edit_reply_markup(reply_markup=cm.menu_markups.get("sel_country"))


@menu_router.callback_query(F.data.startswith("country:"))
async def country_callback(callback: types.CallbackQuery, state: FSMContext) -> None:
    message = callback.message

    if isinstance(message, types.Message):
        country = callback.data.removeprefix("country:")  # type: ignore
        tempDict = (await state.get_data()).get("tempDict", {})
        tempDict.update(country=country)

        await state.update_data(tempDict=tempDict)  # Update in Redis database

        callback = types.CallbackQuery(
            id="done",
            from_user=callback.from_user,  # type: ignore
            chat_instance=message.chat.type,
            message=message,
            data="show_news",
        )

        # await show_news(callback, state)
        await message.answer(text="Showing news...")
        await message.delete()


@menu_router.callback_query(F.data == "sel_country_man")
async def sel_custom_country_callback(
    callback: types.CallbackQuery, state: FSMContext
) -> None:
    await state.set_state(MainMenu.sel_country_manually)

    editable_message = await callback.message.answer(  # type: ignore
        text=msg.sel_countries()
    )

    await callback.message.delete()  # type: ignore
    await state.update_data(
        # For navigation main_message should be edited only
        main_message_id=editable_message.message_id
    )


@menu_router.message(MainMenu.sel_country_manually)
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
        # TODO: Please filter valid countries and get total number of countries! Find 1 to x?
        if (not country_id) or 0 > country_id or country_id > 10:
            try:
                await main_message.edit_text(  # type: ignore
                    text="*Please, Enter valid Choice*\n" + msg.sel_countries()
                )
            except Exception as e:
                await message.answer(str(e))

        else:
            tempDict: dict = data.get("tempDict", {})
            tempDict.update(country=msg._get_country(country_id))
            await state.update_data(tempDict=tempDict)

            callback = types.CallbackQuery(
                id="done",
                from_user=message.from_user,  # type: ignore
                chat_instance=message.chat.type,
                message=main_message,  # type: ignore
                data="sel_country_callback",
            )
            await state.set_state(None)

            # await show_news(callback, state)
            await message.answer(text="Showing news...")

    except Exception as e:
        await message.answer(
            f"Something Went Wrong!!\nContact admin ({ADMIN_USER}) with Screenshot"
        )

    else:
        await message.delete()


@menu_router.callback_query(F.data == "show_results_head")
async def show_results_head(callback: types.CallbackQuery) -> None:
    message = callback.message

    if isinstance(message, types.Message):
        callback = types.CallbackQuery(
            id="done",
            from_user=message.from_user,  # type: ignore
            chat_instance=message.chat.type,
            message=message,  # type: ignore
            data="sel_country_callback",
        )

        # await show_news(callback, state)
        await message.answer(text="Showing Headlines")


@menu_router.callback_query(F.data == "NLP_callback")
async def nlp_callback(
    callback: types.CallbackQuery, state: FSMContext, bot: Bot
) -> None:
    message = callback.message

    await state.set_state(MainMenu.get_custom_prompt)
    if isinstance(message, types.Message):
        # Get message to edit
        await message.edit_text(text="Just Wait🌚")

        await state.update_data(main_message=message.message_id)

        await message.edit_text(text="Please Enter prompt : ")  # type:ignore


@menu_router.message(MainMenu.get_custom_prompt)
async def nlp_custom_prompt(
    message: types.Message, state: FSMContext, bot: Bot
) -> None:
    if message.text:
        data = await state.get_data()
        tempDict: dict = data.get("tempDict", {})

        # Method to extract topics, country and source from given prompt
        topics, country, source = _extract_features(message.text).values()
        tempDict.update(topics=topics, country=country, source=source)
        await state.update_data(tempDict=tempDict)

        main_message = await bot.edit_message_text(
            text="Just Wait🌚",
            chat_id=message.chat.id,
            message_id=(await state.get_data()).get("main_message", message.message_id),
        )

        callback = types.CallbackQuery(
            id="done",
            from_user=message.from_user,  # type: ignore
            chat_instance=message.chat.type,
            message=main_message,  # type: ignore
            data="sel_country_callback",
        )
        await state.set_state(None)
        await message.delete()
        # await show_news(callback, state)
        await main_message.edit_text(text="Showing news...") # type: ignore
    else:
        await message.answer(text="Provide a valid prompt!!")


def _extract_features(prompt: str):
    topics = []
    country = ""
    source = ""
    # Logic for extracting features from prompt

    return {"topics": topics, "country": country, "source": source}
