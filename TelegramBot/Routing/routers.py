"""
## routers.py

This file will contain all the `routers` to be included
"""

from aiogram import Dispatcher, Router

# Router to Route all the Commands
command_router = Router(name="Command Router")

# Router for Registration Handlers
registration_router = Router(name="Registration Router")


def register_routers(DP: Dispatcher) -> None:
    """Registers all the Routers to the Dispatcher Object

    Args:
      DP: Root Dispatcher Object

    Returns:
      None
    """

    DP.include_routers(command_router, registration_router)
