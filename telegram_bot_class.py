import logging
import os
from typing import Final

from telegram import Update
from telegram.ext import ContextTypes, Application, CommandHandler, MessageHandler, filters

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
    return processed

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text: str = update.message.text
    # response: str = handle_response(text)
    await update.message.reply_text("")

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.log(f"Update {update} caused error {context.error}")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.run_polling(poll_interval=5)


if __name__ == '__main__':
    main()