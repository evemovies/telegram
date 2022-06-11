from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import filters, CallbackContext, MessageHandler, CommandHandler
from evemovies.helpers.shared_keyboards import get_main_keyboard
from evemovies.helpers import stages


async def _handle_start_any_text(update: Update, context: CallbackContext.DEFAULT_TYPE) -> int:
    main_keyboard = get_main_keyboard(context)

    await update.message.reply_text("Starting conversation after restart",
                                    reply_markup=ReplyKeyboardMarkup(main_keyboard))
    return stages.STAGE_MAIN


async def _handle_start_with_command(update: Update, context: CallbackContext.DEFAULT_TYPE) -> int:
    main_keyboard = get_main_keyboard(context)

    await update.message.reply_text("Handling start command", reply_markup=ReplyKeyboardMarkup(main_keyboard))

    return stages.STAGE_MAIN


start_handlers = [
    CommandHandler("start", _handle_start_with_command),
    MessageHandler(filters.TEXT, _handle_start_any_text),
]
