from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext
from evemovies.stages.stage import BaseStage


class MainStage(BaseStage):
    def __init__(self):
        super().__init__("main_stage")

        self.keyboard_listeners = [
            {"keyboard": "main_keyboard", "term": "search", "handler": self._goto_search},
            {"keyboard": "main_keyboard", "term": "settings", "handler": self._goto_settings},
            {"keyboard": "main_keyboard", "term": "movies", "handler": self._goto_movies}
        ]

    async def _goto_search(self, update: Update, context: CallbackContext.DEFAULT_TYPE):
        user_locales = BaseStage.get_user_locales(context)
        back_keyboard = BaseStage.get_back_keyboard(context)

        await update.message.reply_text(user_locales["stages"]["search"]["welcome_to_search"],
                                        reply_markup=ReplyKeyboardMarkup(back_keyboard))

        return BaseStage.stages["search_stage"]

    async def _goto_settings(self, update: Update, context: CallbackContext.DEFAULT_TYPE):
        user_locales = BaseStage.get_user_locales(context)
        back_keyboard = BaseStage.get_back_keyboard(context)

        await update.message.reply_text(user_locales["stages"]["settings"]["what_to_change"],
                                        reply_markup=ReplyKeyboardMarkup(back_keyboard))

        return BaseStage.stages["settings_stage"]

    async def _goto_movies(self, update: Update, context: CallbackContext.DEFAULT_TYPE):
        user_locales = BaseStage.get_user_locales(context)
        back_keyboard = BaseStage.get_back_keyboard(context)

        await update.message.reply_text(user_locales["stages"]["movies"]["list_of_movies"],
                                        reply_markup=ReplyKeyboardMarkup(back_keyboard))

        return BaseStage.stages["movies_stage"]
