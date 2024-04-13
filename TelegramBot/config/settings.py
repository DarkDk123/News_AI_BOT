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

# Socials
LINKEDIN_URL = os.environ["LINKEDIN_URL"]
GITHUB_URL = os.environ["GITHUB_URL"]

ADMIN_USER = os.environ["ADMIN_USER"]
