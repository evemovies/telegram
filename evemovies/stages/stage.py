from abc import ABC, abstractmethod
from typing import Dict, Any
from telegram import KeyboardButton, Update, ReplyKeyboardMarkup
from telegram.ext import filters, CallbackContext, MessageHandler, CommandHandler, CallbackQueryHandler

from evemovies.locales.locale import locales
from evemovies.helpers.requests_session import session


class BaseStage(ABC):
    stages = {}

    @abstractmethod
    def __init__(self, stage_name):
        self.requests = session
        self.keyboard_listeners = []
        self.command_listeners = []
        self.text_listeners = []
        self.inline_button_listeners = []
        self._add_stage(stage_name)

    @staticmethod
    def get_main_keyboard(context: CallbackContext.DEFAULT_TYPE):
        user_locales = BaseStage.get_user_locales(context)
        base_translation_path = user_locales["keyboards"]["main_keyboard"]

        return [
            [KeyboardButton(base_translation_path["search"]), KeyboardButton(base_translation_path["movies"])],
            [KeyboardButton(base_translation_path["settings"]), KeyboardButton(base_translation_path["about"])],
            [KeyboardButton(base_translation_path["support"]), KeyboardButton(base_translation_path["contact"])]
        ]

    @staticmethod
    def get_back_keyboard(context: CallbackContext.DEFAULT_TYPE):
        user_locales = BaseStage.get_user_locales(context)
        base_translation_path = user_locales["keyboards"]["back_keyboard"]

        return [
            [KeyboardButton(base_translation_path["back"])]
        ]

    @staticmethod
    def get_user_locales(context: CallbackContext.DEFAULT_TYPE):
        language = context.user_data["user"]["language"]

        return locales[language]

    @staticmethod
    def save_movies_to_user_data(context: CallbackContext.DEFAULT_TYPE, movies):
        movies_map = {}

        for movie in movies:
            movies_map[movie["id"]] = movie

        context.user_data["current_movies"] = movies_map

    def _add_stage(self, stage_name):
        stage_index = len(BaseStage.stages)
        BaseStage.stages[stage_name] = stage_index

    async def _go_back(self, update: Update, context: CallbackContext.DEFAULT_TYPE):
        main_keyboard = BaseStage.get_main_keyboard(context)

        await update.message.reply_text("Returning to the main stage", reply_markup=ReplyKeyboardMarkup(main_keyboard))

        return BaseStage.stages["main_stage"]

    def get_handlers(self):
        listeners = []

        for listener in self.keyboard_listeners:
            en_keyboard = locales["en"]["keyboards"][listener["keyboard"]]
            ru_keyboard = locales["ru"]["keyboards"][listener["keyboard"]]

            listeners.append(MessageHandler(filters.Regex(f"^({en_keyboard[listener['term']]})$"), listener["handler"]))
            listeners.append(MessageHandler(filters.Regex(f"^({ru_keyboard[listener['term']]})$"), listener["handler"]))

        for listener in self.command_listeners:
            listeners.append(CommandHandler(listener["command"], listener["handler"]))

        for listener in self.text_listeners:
            listeners.append(MessageHandler(filters.TEXT, listener["handler"]))

        return listeners

    def get_inline_handlers(self):
        inline_listeners = []

        for listener in self.inline_button_listeners:
            inline_listeners.append(CallbackQueryHandler(listener))

        return inline_listeners
