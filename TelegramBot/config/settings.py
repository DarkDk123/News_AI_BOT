"""
## settings.py

This file contains all the necessary `settings`
required by the `BOT` and project in general.
"""

import os


# Redis Settings

REDIS_HOST: str = os.environ["REDIS_HOST"]
REDIS_PORT: int = int(os.environ["REDIS_PORT"])
REDIS_PASSWORD: str = os.environ["REDIS_PASSWORD"]

LINKEDIN_URL = "https://www.linkedin.com/in/dipeshrathore1"
GITHUB_URL = "https://github.com/DarkDk123/News_AI_BOT"
