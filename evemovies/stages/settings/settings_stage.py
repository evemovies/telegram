from evemovies.stages.stage import BaseStage


class SettingsStage(BaseStage):
    def __init__(self):
        super().__init__("settings_stage")

        self.keyboard_listeners = [
            {"keyboard": "back_keyboard", "term": "back", "handler": self._go_back},
        ]
