import json
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
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
        self.inline_button_listeners = [self._handle_inline_option]

    async def _handle_inline_option(self, update: Update, context: CallbackContext.DEFAULT_TYPE):
        query = update.callback_query
        formatted_query_data = json.loads(query.data)

        actions_map = {
            "movie": self._select_movie,
            "add": self._add_selected_movie,
            "back": self._unselect_movie
        }

        await actions_map[formatted_query_data["a"]](context, query)

        await query.answer()

    async def _select_movie(self, context: CallbackContext.DEFAULT_TYPE, query: CallbackQuery):
        formatted_query_data = json.loads(query.data)

        movie_selected_keyboard = [
            [
                InlineKeyboardButton("Back", callback_data=json.dumps({"a": "back", "p": None})),
                InlineKeyboardButton("Add", callback_data=json.dumps({"a": "add", "p": formatted_query_data["p"]})),
            ]
        ]
        await query.edit_message_text("chosen", reply_markup=InlineKeyboardMarkup(movie_selected_keyboard))

        await query.answer()

    async def _add_selected_movie(self, context: CallbackContext.DEFAULT_TYPE, query: CallbackQuery):
        movies = context.user_data["current_movies"]
        formatted_query_data = json.loads(query.data)

        print("Adding movie for a user", movies[formatted_query_data["p"]])

        await query.answer()

    async def _unselect_movie(self, context: CallbackContext.DEFAULT_TYPE, query: CallbackQuery):
        movies = context.user_data["current_movies"]

        movie_buttons = []
        for movie in movies.values():
            movie_buttons.append([InlineKeyboardButton(f"{movie['title']} {movie['year']}",
                                                       callback_data=json.dumps({"a": "movie", "p": movie['id']}))])

        await query.edit_message_text("Results", reply_markup=InlineKeyboardMarkup(movie_buttons))
        await query.answer()

    async def _search_movie(self, update: Update, context: CallbackContext.DEFAULT_TYPE):
        movies_response = self.requests.get(
            "/api/v1/movies/search-movie?language=en&title=last%20duel&year=2021").json()
        movies = movies_response["data"]["foundMovies"]

        BaseStage.save_movies_to_user_data(context, movies)

        movie_buttons = []
        for movie in movies:
            movie_buttons.append([InlineKeyboardButton(f"{movie['title']} {movie['year']}",
                                                       callback_data=json.dumps({"a": "movie", "p": movie['id']}))])

        await update.message.reply_text(f"Searching for a movie {update.message.text}",
                                        reply_markup=InlineKeyboardMarkup(movie_buttons))
