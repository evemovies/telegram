import json
from pathlib import Path

en_file = Path(__file__).with_name("en.json")
ru_file = Path(__file__).with_name("ru.json")

with en_file.open("r") as en_raw, ru_file.open("r") as ru_raw:
    en = json.load(en_raw)
    ru = json.load(ru_raw)

    locales = {
        "en": en,
        "ru": ru
    }
