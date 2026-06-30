from datetime import datetime
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "activity.log")


def save_log(action):

    os.makedirs(LOG_DIR, exist_ok=True)

    with open(
        LOG_FILE,
        "a",
        encoding="utf-8"
    ) as file:

        file.write(
            f"{datetime.now()} - {action}\n"
        )