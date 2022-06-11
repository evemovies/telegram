import json
from pathlib import Path
from typing import Dict, Any
from telegram.ext import CallbackContext

en_file = Path(__file__).with_name("en.json")
ru_file = Path(__file__).with_name("ru.json")

with en_file.open("r") as en_raw, ru_file.open("r") as ru_raw:
    en = json.load(en_raw)
    ru = json.load(ru_raw)

    locales = {
        "en": en,
        "ru": ru
    }


def get_user_locales(ctx: CallbackContext.DEFAULT_TYPE) -> Dict[str, Any]:
    language = ctx.user_data["user"]["language"]

    return locales[language]
