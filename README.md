<div align="center">

  # <span align="center"> Telegram - News AI Bot</span>
  <img src="./images/Bot_Profile.jpeg" alt="Bot Profile" width="30%">

</div>

<br>

---
<h1 align="center">

[TeleNewsPy🕊️](https://web.telegram.org/k/#@TeleNewsPy_Bot)

[![TeleNewsPy Status](https://cronitor.io/badges/WwEpyi/production/_tkad06ybaR-xchTipqEpYL9_10.svg)](https://news-ai-bot.onrender.com)

![GitHub stars](https://img.shields.io/github/stars/DarkDk123/News_AI_BOT?style=plastic&label=Stars&color=blue&labelColor=grey&logo=github)
[![license](https://img.shields.io/github/license/DarkDk123/News_AI_BOT?color=blue&label=License&style=plastic)](https://github.com/DarkDk123/News_AI_BOT/blob/main/LICENSE)
[![developer](https://img.shields.io/static/v1?label=Author&message=DarkDk123&color=blue&style=plastic)](https://github.com/DarkDk123)
</h1>



## Description

The **Telegram News AI Bot** is an intelligent bot that fetches and delivers the latest news to users on Telegram.
It leverages [Gemini AI](https://ai.google.dev/gemini-api) to process **NLP queries** and
provide interactive news updates based on user queries (topics & keywords). This project is built using
[AIOgram](https://github.com/aiogram/aiogram), [FastAPI](https://github.com/tiangolo/fastapi) and other python libraries!

It uses [NewsAPI](https://newsapi.org) to fetch recent news data!


<div align="center">
   
### BOT GIFs

<img src=./images/demo.gif height=400></img>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img src=./images/demo2.gif height=400></img>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img src=./images/demo3.gif height=400></img>
</div>

## Features

- Recent news articles
- NLP Prompt with AI
- Quick & Personalized Updates
- Concise, readable chunks of news
- Easy Interface with Telegram

## Usage

There are two ways to use the Telegram News AI Bot:

1. **Live Deployed Bot**:
   - Interact with the live bot on Telegram: [TeleNewsPy🕊️](https://web.telegram.org/k/#@TeleNewsPy_Bot)
   - Simply start the bot and follow the prompts to receive news updates.

2. **Local Installation**:
   - Follow the installation instructions below to set up and run the bot on your local machine.


## Setup

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Installation

#### 1. Clone the repository:
    
   ```sh
   git clone https://github.com/DarkDk123/News_AI_BOT.git
   cd News_AI_BOT
   ```

#### 2. Install the required dependencies:
    
   ```sh
   pip install -r "requirements.txt"
   ```

#### 3. Set up environment variables:
   > Create a `.env` file in the root directory and add the necessary environment variables. Refer to the [`env_example`](https://github.com/DarkDk123/News_AI_BOT/blob/main/env_example) file for guidance.

### Running the Bot

#### 1. Run the `main.py` file from root directory:
    
   ```sh
   python "TelegramBot/main.py" # Command should be the same!
   ```

Once the server is running, the bot will deliver articles to the configured Telegram chat.
You can interact with the bot using the Telegram app to make NLP queries and receive
interactive news updates based on your queries.

## Contributing

We welcome contributions from the community! To contribute:

1. [Fork](https://github.com/DarkDk123/News_AI_BOT/fork) this repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes.
5. Push to the branch.
6. Open a pull request.

For any questions or feedback, please open an issue on GitHub or contact the [project maintainers](https://github.com/DarkDk123/News_AI_BOT/contributors).

## License

This project is licensed under the ***GPL 3.0*** License. See the [`LICENSE`](https://github.com/DarkDk123/News_AI_BOT/blob/main/LICENSE) file for more details.