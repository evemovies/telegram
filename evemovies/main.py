import os
import logging
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, ConversationHandler
from evemovies.start.handlers import start_handlers
from evemovies.main.handlers import main_handlers
from evemovies.search.handlers import search_handlers
from evemovies.movies.handlers import movies_handlers
from evemovies.settings.handlers import settings_handlers
from evemovies.helpers.stages import stages as stages_map

load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    application = ApplicationBuilder().token(os.getenv('TELEGRAM_TOKEN')).build()

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

    application.add_handler(conversation)
    application.run_polling()
