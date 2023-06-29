import os
from typing import Final

from telegram import Update
from telegram.ext import ContextTypes

BOT_TOKEN: Final = os.getenv("BOT_TOKEN")
BOT_USERNAME: Final = os.getenv("BOT_USERNAME")

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome!...")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("youtube downloader")

# Handle Responses
def handle_response(text: str) -> str:
    processed : str = text.lower()
    # CODE
    return "test"

