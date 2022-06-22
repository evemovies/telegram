import logging
from dotenv import dotenv_values
from telegram.ext import ApplicationBuilder, ConversationHandler, CommandHandler

from evemovies.stages.stage import BaseStage
from evemovies.stages.main.main_stage import MainStage
from evemovies.stages.start.start_stage import StartStage
from evemovies.stages.search.search_stage import SearchStage
from evemovies.stages.movies.movies_stage import MoviesStage
from evemovies.stages.settings.settings_stage import SettingsStage

from evemovies.helpers.expose_user_middleware import expose_user_handler
from evemovies.helpers.general_commands import handle_saveme

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

if __name__ == "__main__":
    application = ApplicationBuilder().token(dotenv_values()["TELEGRAM_TOKEN"]).build()

    all_stages = {
        "main_stage": MainStage(),
        "start_stage": StartStage(),
        "search_stage": SearchStage(),
        "movies_stage": MoviesStage(),
        "settings_stage": SettingsStage(),
    }

    conversation_states = {}

    for stage_name, stage_index in BaseStage.stages.items():
        conversation_states[stage_index] = \
            all_stages[stage_name].get_handlers() + all_stages[stage_name].get_inline_handlers()

    conversation = ConversationHandler(
        per_user=True,
        entry_points=all_stages["start_stage"].get_handlers(),
        states=conversation_states,
        fallbacks=[CommandHandler("saveme", handle_saveme)],
    )

    # TODO: add /saveme command
    application.add_handler(expose_user_handler, 0)
    application.add_handler(conversation, 1)
    application.run_polling()
