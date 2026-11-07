import json
import os

FILE_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "devices.json"
)


# - - - Loading Devices
def load_devices():
    if not os.path.exists(FILE_PATH):
        return {}

    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, dict):
            return {}

        return data

    except (json.JSONDecodeError, OSError):
        return {}


# - - - Saving Devices
def save_devices(devices):
    try:
        os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)

        temp_path = FILE_PATH + ".tmp"

        with open(temp_path, "w", encoding="utf-8") as file:
            json.dump(
                devices,
                file,
                indent=4,
                ensure_ascii=False
            )

        os.replace(temp_path, FILE_PATH)
        return True

    except (OSError, TypeError):
        return False
