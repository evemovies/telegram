from telegram import Update
from telegram.ext import filters, CallbackContext, MessageHandler
from evemovies.helpers import stages


async def _handle_main_any_text(update: Update, context: CallbackContext.DEFAULT_TYPE):
    print('wrong text, suggest to choose action from the keyboard')


async def _handle_main_goto_search(update: Update, context: CallbackContext.DEFAULT_TYPE):
    print('going to search')
    return stages.STAGE_SEARCH


async def _handle_main_goto_settings(update: Update, context: CallbackContext.DEFAULT_TYPE):
    print('going to settings')
    return stages.STAGE_SETTINGS


main_handlers = [
    MessageHandler(filters.Regex('^(search)$'), _handle_main_goto_search),
    MessageHandler(filters.Regex('^(settings)$'), _handle_main_goto_settings),
    MessageHandler(filters.TEXT, _handle_main_any_text)
]
