from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext
from evemovies.stages.stage import BaseStage


class StartStage(BaseStage):
    def __init__(self):
        super().__init__("start_stage")

        self.command_listeners = [
            {"command": "start", "handler": self._create_user}
        ]
        self.text_listeners = [
            {"handler": self._handle_any_text}
        ]

    async def _create_user(self, update: Update, context: CallbackContext.DEFAULT_TYPE):
        main_keyboard = BaseStage.get_main_keyboard(context)

        await update.message.reply_text("Checking if need to create a new user",
                                        reply_markup=ReplyKeyboardMarkup(main_keyboard))

        return BaseStage.stages["main_stage"]

    async def _handle_any_text(self, update: Update, context: CallbackContext.DEFAULT_TYPE):
        main_keyboard = BaseStage.get_main_keyboard(context)

        await update.message.reply_text("Starting conversation after restart",
                                        reply_markup=ReplyKeyboardMarkup(main_keyboard))

        return BaseStage.stages["main_stage"]
