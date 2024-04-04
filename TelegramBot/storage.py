"""
## storage.py

This file contains `storage` data,
and we're using `Redis` Storage for this project.
"""

from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder

from redis.asyncio import Redis
from config import settings

storage = RedisStorage(
    redis=Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        password=settings.REDIS_PASSWORD,
    ),
    key_builder=DefaultKeyBuilder(with_bot_id=True),
)
