from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext

from evemovies.stages.stage import BaseStage


async def handle_saveme(update: Update, context: CallbackContext.DEFAULT_TYPE):
    main_keyboard = BaseStage.get_main_keyboard(context)

    await update.message.reply_text("Something went wrong, try again", reply_markup=ReplyKeyboardMarkup(main_keyboard))

    return 0
