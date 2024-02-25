from datetime import date
import platform


class Settings:
    APP_NAME = "ToDo"

    # builder_settings
    VERSION = 'v0.0.1'

    GEOMETRY = f"{1200}x{800}"

    STORAGE_PATH = 'storage.json'

    COLOR_SIDEBAR_BG = ('#ebebeb', '#303030')
    COLOR_SIDEBAR_BTN = "transparent"
    COLOR_SIDEBAR_BTN_HOVER = ("#d2d2d2", "#464646")
    COLOR_SIDEBAR_BTN_TEXT = ("gray10", "gray90")
    COLOR_SIDEBAR_BTN_ACTIVE = ("#d9d9d9", "#3f3f3f")

    COLOR_WINDOW_BG = ("#fafafa", "gray88")

    COLOR_BIG_LABEL_BG = COLOR_SIDEBAR_BG