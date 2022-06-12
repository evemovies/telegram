from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext
from evemovies.stages.stage import BaseStage


class SearchStage(BaseStage):
    def __init__(self):
        super().__init__("search_stage")

        self.keyboard_listeners = [
            {"keyboard": "back_keyboard", "term": "back", "handler": self._go_back},
        ]
        self.text_listeners = [
            {"handler": self._search_movie}
        ]

    async def _search_movie(self, update: Update, context: CallbackContext.DEFAULT_TYPE):
        back_keyboard = BaseStage.get_back_keyboard(context)

        movies = self.requests.get("/api/v1/movies/search-movie?language=en&title=last%20duel&year=2021").json()

        print(movies)

        await update.message.reply_text(f"Searching for a movie {update.message.text}",
                                        reply_markup=ReplyKeyboardMarkup(back_keyboard))
