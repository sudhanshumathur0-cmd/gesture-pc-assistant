import time

from services import (
    open_browser,
    close_browser,
    take_screenshot,
    volume_mute,
    volume_up,
    volume_down,
    play_pause_music
)

from logger import save_log


class ActionController:

    def __init__(self):
        self.last_action_time = 0
        self.cooldown = 2

    def execute(self, gesture):

        current_time = time.time()

        if current_time - self.last_action_time < self.cooldown:
            return

        if gesture == "OPEN_PALM":
            open_browser()
            save_log("Browser Opened")

        elif gesture == "CLOSE_BROWSER":
            close_browser()
            save_log("Browser Closed")

        elif gesture == "VICTORY":
            take_screenshot()
            save_log("Screenshot Taken")

        elif gesture == "FIST":
            volume_mute()
            save_log("Volume Muted")

        elif gesture == "THUMBS_UP":
            play_pause_music()
            save_log("Music Play/Pause")

        elif gesture == "VOLUME_UP":
            volume_up()
            save_log("Volume Up")

        elif gesture == "VOLUME_DOWN":
            volume_down()
            save_log("Volume Down")

        self.last_action_time = current_time