from telegram import Update
from telegram.ext import filters, CallbackContext, MessageHandler, CommandHandler
from evemovies.helpers import stages


async def _handle_start_any_text(update: Update, context: CallbackContext.DEFAULT_TYPE) -> int:
    print('starting conversation after restart')
    return stages.STAGE_MAIN


async def _handle_start_with_command(update: Update, context: CallbackContext.DEFAULT_TYPE) -> int:
    print('user registration in progress')
    return stages.STAGE_MAIN


start_handlers = [
    CommandHandler('start', _handle_start_with_command),
    MessageHandler(filters.TEXT, _handle_start_any_text),
]
