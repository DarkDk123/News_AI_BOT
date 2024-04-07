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
from .fsm import Registration


@rr.callback_query(F.data == "correct_name_yes")
async def correct_name(callback: types.CallbackQuery, state: FSMContext) -> None:
    await state.update_data(name=callback.from_user.full_name)  # type: ignore

    await callback.message.answer(msg.locations(), reply_markup=cm.registration_markups["location_prompt"]) # type: ignore
    await state.set_state(Registration.location_prompt)


@rr.callback_query(F.data == "correct_name_no")
async def correct_name_(callback: types.CallbackQuery, state: FSMContext) -> None:
    await callback.message.answer("Well, then what should we call you??")  # type: ignore
    await state.set_state(Registration.name)


@rr.message(Registration.name)
async def name(message: types.Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    await message.reply(
        text=msg.locations(),
        reply_markup=cm.registration_markups["location_prompt"],
    )


@rr.message(Registration.location_prompt)
async def location_prompt(message: types.Message, state: FSMContext) -> None:
    await state.update_data(country=message.text)
    await message.reply("Now, Please Enter your favourite topics,\nSeparated by *coma (,)*")
    await state.set_state(Registration.sel_news_topics)


@rr.message(Registration.sel_news_topics)
async def select_news_topics(message: types.Message, state: FSMContext) -> None:
    try:
        topics = message.text.split(',') #type: ignore
        if (not topics):
            message.answer("Please enter valid topic string \ni.e. AI, Data, Something")
        else:
            await state.update_data(topics=topics, is_registered=True)
            await message.answer("*Registration Complete!!*✅")
            
            # Now we have to start main menu
    except:
        message.answer("Something Went Wrong, try Again!!")
    
