"""
## NLP_processor.py

Logic to decide required function `arguments` using Gemini

This file leverages `Function calling` feature of GeminiAPI
read more here : [Official article]("https://ai.google.dev/gemini-api/docs/function-calling/python"), [Tutorial]("https://ai.google.dev/gemini-api/tutorials/extract_structured_data")
"""

from GenAI.Gemini import AI

import google.ai.generativelanguage as glm

from .Constant.text_messages import countries, languages

# Function as JSON dictionary for Gemini `Tools`
func = {
    "function_declarations": [
        {
            "name": "get_everything",
            "description": "Search through millions of articles from over 30,000 large and small news sources and blogs. Refer to the official News API documentation for details on search syntax and examples.",
            "parameters": {
                "type_": "OBJECT",
                "properties": {
                    "q": {
                        "type_": "ARRAY",
                        "description": "Array of Keywords or phrases to search for in the article title and body. Abbreviations should be UpperCased!, single topic should also be in an Array",
                    },
                    # get_everything doesn't take "country", instead i'll use it to fetch "sources"
                    "country": {
                        "type_": "STRING",
                        "description": f"Country in Capital cased, must be one of '{list(countries.keys())}'. If unable to determine, default should be 'None'",
                    },
                    "language": {
                        "type_": "STRING",
                        "description": "The 2-letter ISO-639-1 code of the language you want to get headlines for.",
                    },
                },
                # "required": ["q"], # getting anything if want news from whole country!
            },
        }
    ]
}


async def extract_features(prompt: str) -> str | dict:
    """
    Extracts topics, country and language (if available) from the NLP prompt using `Gemini`
    """
    response = await AI.generate_text_async(prompt, tools=[glm.Tool(func)])
    try:
        fc = response.candidates[0].content.parts[0].function_call
        if not fc.args:
            raise Exception("Function call not returned by Gemini")
    except Exception as e:
        if response.candidates[0].finish_reason != 1:
            if response.candidates[0].finish_reason == 3:
                return "We can't have a conversation like that!🤫"
            else:
                return "I can't proceed with that request! 😓"

        elif response.text:
            return response.text
        else:
            return "Something bad happened!"

    topics = list(fc.args["q"] if "q" in fc.args else [])  # type: ignore
    country = (
        fc.args["country"]
        if "country" in fc.args and fc.args["country"] in countries
        else None
    )

    language = (
        fc.args["language"]
        if "language" in fc.args and fc.args["language"] in languages
        else "en"
    )

    print(topics, country, language)
    return {"topics": topics, "country": country, "language": language}
