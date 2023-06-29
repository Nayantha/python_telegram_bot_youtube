import os
from typing import Final

from telegram import Update

BOT_TOKEN: Final = os.getenv("BOT_TOKEN")
BOT_USERNAME: Final = os.getenv("BOT_USERNAME")

async def start_command(update: Update,):
    ...