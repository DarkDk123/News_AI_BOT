"""
## fsm.py

This file contains all `Finite State Machines`
required in this project.

It contains the `StatesGroup` objects having certain `States`.
"""

from aiogram.fsm.state import State, StatesGroup


class Registration(StatesGroup):
    name = State(state="Username")
    location_prompt = State(state="Location Prompt")

    loc_not_passed = State(state="Location prompt not passed")
    sel_countries_manually = State(state="Select countries")

    sel_news_topics = State(state="Select News Topics")  # Not used now!


class MainMenu(StatesGroup):
    sel_custom_news_topics = State(state="Select News Topics")
    sel_country_manually = State(state="Select Country")
    get_custom_prompt = State(state="NLP Prompt")
