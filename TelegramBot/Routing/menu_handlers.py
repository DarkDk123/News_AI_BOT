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
from config.settings import ADMIN_USER, BOT_USER

import time as t
import re
from NewsFetchClasses.Fetch_news import newsAPI, get_sources_by_country
from newsapi.newsapi_exception import NewsAPIException
from .NLP_processor import extract_features


@menu_router.callback_query(F.data == "menu_callback")
async def start_menu(callback: types.CallbackQuery) -> None:
    message = callback.message

    if isinstance(message, types.Message):
        if message.from_user.username == BOT_USER[1:]:  # type: ignore
            await message.edit_text(
                text="<b>Main Menu</b>", reply_markup=cm.menu_markups.get("main_menu")
            )
        else:
            await message.answer(
                text="<b>Main Menu</b>", reply_markup=cm.menu_markups.get("main_menu")
            )


@menu_router.callback_query(F.data == "quick_updates")
async def quick_update(callback: types.CallbackQuery, state: FSMContext) -> None:
    message = callback.message
    data = await state.get_data()

    if isinstance(message, types.Message):
        if not data.get("is_registered"):
            new_msg = await message.answer(msg.no_quick())
            t.sleep(3)
            await new_msg.delete()
        else:
            callback = types.CallbackQuery(
                id="done",
                from_user=callback.from_user,  # type: ignore
                chat_instance=message.chat.type,
                message=message,  # type: ignore
                data="show_personalized_news",
            )

            await show_news(callback, state)


@menu_router.callback_query(F.data == "sel_topics_callback")
async def sel_topics_callback(callback: types.CallbackQuery) -> None:
    message = callback.message

    if isinstance(message, types.Message):
        await message.edit_text(
            "<b>Select Topics 🤳</b>", reply_markup=cm.menu_markups.get("sel_topics")
        )


@menu_router.callback_query(F.data == "sel_custom_news_topics")
async def sel_custom_news_topics_callback(
    callback: types.CallbackQuery, state: FSMContext
) -> None:
    await state.set_state(MainMenu.sel_custom_news_topics)

    editable_message = await callback.message.answer(  # type: ignore
        text="Now, Please Enter your favourite topics Separated by <b><code>coma (,)</code></b>"
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
        topics = list(
            map(
                lambda x: x.casefold().strip() if len(x) > 3 else x.upper().strip(),
                message.text.split(","),
            )
        )  # type: ignore
        if not topics:
            await main_message.edit_text(  # type: ignore
                "💀 Please enter valid topic string \ni.e. <code>AI, Data, Something</code>"
            )
        elif not all(map(lambda x: re.match(re.compile(r"^[a-zA-Z\s]*$"), x), topics)):
            await main_message.edit_text(  # type: ignore
                "Topics should be alphabet only!\n Separated by <code>','</code>"
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
            await state.set_state(MainMenu.get_custom_prompt)
            await sel_country_callback(callback, state)

    except Exception as _:
        await message.answer(
            f"💔Something Went Wrong!!\nPlease Contact admin ({ADMIN_USER}) with Screenshots."
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
            topic = (
                topic.casefold().strip()
                if len(topic := callback.data.removeprefix("topic:")) > 3
                else topic.upper().strip()
            )  # type: ignore
            await state.update_data(tempDict={"topics": [topic]})

        await message.edit_text(
            text="<b>Select Country</b>",
            reply_markup=cm.menu_markups.get("sel_country"),
        )


@menu_router.callback_query(F.data.startswith("country:"))
async def country_callback(callback: types.CallbackQuery, state: FSMContext) -> None:
    message = callback.message

    if isinstance(message, types.Message):
        country = callback.data.removeprefix("country:")  # type: ignore
        tempDict = (await state.get_data()).get("tempDict", {})
        tempDict.update(country=country if country != "None" else None)

        await state.update_data(tempDict=tempDict)  # Update in Redis database

        callback = types.CallbackQuery(
            id="done",
            from_user=callback.from_user,  # type: ignore
            chat_instance=message.chat.type,
            message=message,
            data="show_news",
        )

        await show_news(callback, state)


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

        if (not country_id) or 1 > country_id or country_id > 17:
            try:
                await main_message.edit_text(  # type: ignore
                    text="<b>Please, Enter valid Choice</b>\n" + msg.sel_countries()
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
                data="show_news",
            )
            await state.set_state(MainMenu.get_custom_prompt)

            await show_news(callback, state)

    except Exception as _:
        await message.answer(
            f"💔Something Went Wrong!!\nPlease Contact admin ({ADMIN_USER}) with Screenshots."
        )

    else:
        await message.delete()


@menu_router.callback_query(F.data == "show_results_head")
async def show_results_head(callback: types.CallbackQuery, state: FSMContext) -> None:
    message = callback.message

    if isinstance(message, types.Message):
        callback = types.CallbackQuery(
            id="done",
            from_user=message.from_user,  # type: ignore
            chat_instance=message.chat.type,
            message=message,  # type: ignore
            data="show_news_headlines",
        )

        await show_news_headlines(callback, state)


@menu_router.callback_query(F.data == "NLP_callback")
async def nlp_callback(
    callback: types.CallbackQuery, state: FSMContext, bot: Bot
) -> None:
    message = callback.message

    await state.set_state(MainMenu.get_custom_prompt)
    if isinstance(message, types.Message):
        # Get message to edit
        await message.edit_text(text="Just Wait🌚")

        await state.update_data(main_message_id=message.message_id)

        await message.edit_text(text="Please Enter prompt : ")  # type:ignore


@menu_router.message(MainMenu.get_custom_prompt)
async def nlp_custom_prompt(
    message: types.Message, state: FSMContext, bot: Bot
) -> None:
    if message.text and not message.text.startswith("/"):
        data = await state.get_data()
        tempDict: dict = data.get("tempDict", {})

        # Method to extract topics, country and language from given prompt
        features = await extract_features(msg.query_template(message.text))

        if isinstance(features, str):
            await message.answer(features, parse_mode="Markdown")
            return None  # Keep user on the same state.
        else:
            tempDict.update(**features)
            await state.update_data(tempDict=tempDict)

        callback = types.CallbackQuery(
            id="done",
            from_user=message.from_user,  # type: ignore
            chat_instance=message.chat.type,
            message=message,
            data="show_news",
        )
        # await state.set_state() # Keep state to Custom Prompt
        await message.delete()
        await show_news(callback, state)
    else:
        await handle_rubbish(message)


@menu_router.callback_query(F.data == "show_news")
@menu_router.callback_query(F.data == "show_personalized_news")
async def show_news(callback: types.CallbackQuery, state: FSMContext) -> None:
    message = callback.message
    data = await state.get_data()

    # Logic for Personalized Vs Temporary News
    tempDict = (
        data
        if (callback.data == "show_personalized_news")
        else data.get("tempDict", {})
    )

    try:
        topics = " OR ".join(tempDict.get("topics", ["tech", "python"]))
        sources = get_sources_by_country(
            msg.countries.get(tempDict.get("country"))  # type: ignore
        )
        language = tempDict.get("language", None)  # Get language if provided

        response = newsAPI.get_everything(
            q=topics,
            sources=sources,
            sort_by="relevancy",
            page_size=3,
            language=language,
            qintitle=topics,
        )

    except NewsAPIException as e:
        if e.get_code() == "rateLimited":
            await message.answer(msg.api_rate_limited())  # type: ignore
        else:
            await message.answer("🙁 Unknown API Error!!⚠️")  # type: ignore

    else:
        if isinstance(message, types.Message):
            if response["status"] == "ok":
                if not response["articles"]:
                    message = await message.answer("📪No Articles Found!⚠️")
                    t.sleep(2)
                    await message.delete()
                else:
                    await message.answer(
                        f"<blockquote>🔍 Here are News Articles about {', '.join(topics.split(' OR '))} 📰</blockquote>"
                    )
                    for idx, article in zip(
                        msg.emoji_indexes,
                        response["articles"],
                    ):
                        if article["title"] in ("[Removed]", None):
                            continue
                        await message.answer(
                            msg.article_to_str(article=article, index=idx),
                            reply_markup=cm.get_response_markup(article["url"]),
                        )

            elif response["status"] == "error":
                await message.answer(response["message"])

            else:
                await message.answer(str(response))


@menu_router.callback_query(F.data == "show_news_headlines")
async def show_news_headlines(callback: types.CallbackQuery, state) -> None:
    message = callback.message

    try:
        response = newsAPI.get_top_headlines(page_size=3)

    except NewsAPIException as e:
        if e.get_code() == "rateLimited":
            await message.answer(msg.api_rate_limited())  # type: ignore
        else:
            await message.answer("🙁 Unknown API Error!!⚠️")  # type: ignore

    else:
        if isinstance(message, types.Message):
            if response["status"] == "ok":
                if not response["articles"]:
                    message = await message.answer("📪No Articles Found!⚠️")
                    t.sleep(2)
                    await message.delete()
                else:
                    await message.answer(
                        "<blockquote>🔍 Here are Top News Headlines 📰</blockquote>"
                    )
                    for idx, article in zip(msg.emoji_indexes, response["articles"]):
                        if article["title"] in ("[Removed]", None):
                            continue
                        await message.answer(
                            msg.article_to_str(article=article, index=idx),
                            reply_markup=cm.get_response_markup(article["url"]),
                        )
            elif response["status"] == "error":
                await message.edit_text(response["message"])

            else:
                await message.edit_text(str(response))


@menu_router.callback_query(F.data == "delete_article")
async def delete_article(callback: types.CallbackQuery) -> None:
    message = callback.message

    if isinstance(message, types.Message):
        await message.delete()


@menu_router.message()
async def handle_rubbish(message: types.Message) -> None:
    if message.text:
        print(message.text)
        b_message = await message.answer("❌ Invalid Message or Command!! 😵")
    elif message.photo:
        b_message = await message.answer("👌Beautiful Photo!!, but of no use!😁")
    elif message.audio or message.voice:
        b_message = await message.answer("😅 I'm Deaf,🧏 Just listen👂 news from me!")  # type: ignore
    else:
        b_message = await message.answer("❌ It's Invalid, please try valid command!🙏")
    t.sleep(1.5)  # Wait & delete!

    await message.delete()
    await b_message.delete()
