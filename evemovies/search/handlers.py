from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import filters, CallbackContext, MessageHandler
from evemovies.helpers import stages
from evemovies.helpers.shared_keyboards import get_main_keyboard, get_back_keyboard
from evemovies.locales.locale import locales


async def _handle_search_movie_search(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    print(f"handling movie search {update.message.text}")
    print("should reply with back keyboard")
    back_keyboard = get_back_keyboard(context)

    await update.message.reply_text(f"Searching for a movie {update.message.text}",
                                    reply_markup=ReplyKeyboardMarkup(back_keyboard))


async def _handle_search_leave(update: Update, context: CallbackContext.DEFAULT_TYPE) -> int:
    main_keyboard = get_main_keyboard(context)

    await update.message.reply_text("Returning to the main stage", reply_markup=ReplyKeyboardMarkup(main_keyboard))

    return stages.STAGE_MAIN


_en_translation_base_path = locales["en"]["keyboards"]["back_keyboard"]
_ru_translation_base_path = locales["ru"]["keyboards"]["back_keyboard"]

search_handlers = [
    MessageHandler(filters.Regex(f"^({_en_translation_base_path['back']})$"), _handle_search_leave),
    MessageHandler(filters.Regex(f"^({_ru_translation_base_path['back']})$"), _handle_search_leave),
    MessageHandler(filters.TEXT, _handle_search_movie_search),
]
