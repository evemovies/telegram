import logging
from dotenv import dotenv_values
from telegram.ext import ApplicationBuilder, ConversationHandler
from evemovies.start.handlers import start_handlers
from evemovies.main.handlers import main_handlers
from evemovies.search.handlers import search_handlers
from evemovies.movies.handlers import movies_handlers
from evemovies.settings.handlers import settings_handlers
from evemovies.helpers.stages import stages as stages_map
from evemovies.helpers.expose_user_middleware import expose_user_handler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    application = ApplicationBuilder().token(dotenv_values()['TELEGRAM_TOKEN']).build()

    conversation = ConversationHandler(
        per_user=True,

        entry_points=start_handlers,
        states={
            stages_map['STAGE_MAIN']: main_handlers,
            stages_map['STAGE_SEARCH']: search_handlers,
            stages_map['STAGE_MOVIES']: movies_handlers,
            stages_map['STAGE_SETTINGS']: settings_handlers
        },
        fallbacks=[],
    )

    application.add_handler(expose_user_handler, 0)
    application.add_handler(conversation, 1)
    application.run_polling()
