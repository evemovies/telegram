from typing import List
from telegram import KeyboardButton
from telegram.ext import CallbackContext
from evemovies.locales.locale import get_user_locales


def get_main_keyboard(ctx: CallbackContext.DEFAULT_TYPE) -> List[List[KeyboardButton]]:
    user_locales = get_user_locales(ctx)
    base_translation_path = user_locales["keyboards"]["main_keyboard"]

    return [
        [KeyboardButton(base_translation_path["search"]), KeyboardButton(base_translation_path["movies"])],
        [KeyboardButton(base_translation_path["settings"]), KeyboardButton(base_translation_path["about"])],
        [KeyboardButton(base_translation_path["support"]), KeyboardButton(base_translation_path["contact"])]
    ]


def get_back_keyboard(ctx: CallbackContext.DEFAULT_TYPE) -> List[List[KeyboardButton]]:
    user_locales = get_user_locales(ctx)
    base_translation_path = user_locales["keyboards"]["back_keyboard"]

    return [
        [KeyboardButton(base_translation_path["back"])]
    ]
