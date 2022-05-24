from telegram import Update
from telegram.ext import filters, CallbackContext, MessageHandler
from evemovies.helpers import stages


async def _handle_movies_any_text(update: Update, context: CallbackContext.DEFAULT_TYPE):
    print('handling default text')
    print('should reply with back keyboard')


async def _handle_movies_leave(update: Update, context: CallbackContext.DEFAULT_TYPE):
    print('leaving movies stage')
    print('should reply with main keyboard')
    return stages.STAGE_MAIN


movies_handlers = [
    MessageHandler(filters.Regex('^(cancel)$'), _handle_movies_leave),
    MessageHandler(filters.TEXT, _handle_movies_any_text),
]
