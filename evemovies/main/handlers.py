from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import filters, CallbackContext, MessageHandler
from evemovies.helpers import stages
from evemovies.locales.locale import locales, get_user_locales
from evemovies.helpers.shared_keyboards import get_back_keyboard


async def _handle_main_any_text(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    print("wrong text, suggest to choose action from the keyboard")


async def _handle_main_goto_search(update: Update, context: CallbackContext.DEFAULT_TYPE) -> int:
    user_locales = get_user_locales(context)
    back_keyboard = get_back_keyboard(context)

    await update.message.reply_text(user_locales["stages"]["search"]["welcome_to_search"],
                                    reply_markup=ReplyKeyboardMarkup(back_keyboard))

    return stages.STAGE_SEARCH


async def _handle_main_goto_settings(update: Update, context: CallbackContext.DEFAULT_TYPE) -> int:
    user_locales = get_user_locales(context)
    back_keyboard = get_back_keyboard(context)

    await update.message.reply_text(user_locales["settings"]["what_to_change"],
                                    reply_markup=ReplyKeyboardMarkup(back_keyboard))

    return stages.STAGE_SETTINGS


_en_translation_base_path = locales["en"]["keyboards"]["main_keyboard"]
_ru_translation_base_path = locales["ru"]["keyboards"]["main_keyboard"]

main_handlers = [
    MessageHandler(filters.Regex(f"^({_en_translation_base_path['search']})$"), _handle_main_goto_search),
    MessageHandler(filters.Regex(f"^({_en_translation_base_path['search']})$"), _handle_main_goto_search),
    MessageHandler(filters.Regex(f"^({_ru_translation_base_path['settings']})$"), _handle_main_goto_settings),
    MessageHandler(filters.Regex(f"^({_ru_translation_base_path['settings']})$"), _handle_main_goto_settings),
    MessageHandler(filters.TEXT, _handle_main_any_text)
]
