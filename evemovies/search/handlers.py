from telegram import Update
from telegram.ext import filters, CallbackContext, MessageHandler
from evemovies.helpers import stages


async def _handle_search_movie_search(update: Update, context: CallbackContext.DEFAULT_TYPE):
    print(f'handling movie search {update.message.text}')
    print('should reply with back keyboard')


async def _handle_search_leave(update: Update, context: CallbackContext.DEFAULT_TYPE):
    print('leaving search stage')
    print('should reply with main keyboard')
    return stages.STAGE_MAIN


search_handlers = [
    MessageHandler(filters.Regex('^(cancel)$'), _handle_search_leave),
    MessageHandler(filters.TEXT, _handle_search_movie_search),
]
