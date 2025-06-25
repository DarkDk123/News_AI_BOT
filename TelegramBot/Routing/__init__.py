"""
## Routing

This Module handles the entire routing of the Bot!
"""

# Importing register_routers
# In context of all defined router handlers

import sys

# Append path to allow importing NewsFetchClasses.
sys.path.append("./")

from dotenv import load_dotenv

# Load .env file first!
load_dotenv()

from .routers import register_routers
from .command_handlers import *  # or specific functions/classes
from .registration_handlers import *
from .menu_handlers import *

__all__ = [
    "register_routers",
]
