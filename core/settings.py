from datetime import date
import distro
import platform


class Settings:
    APP_NAME = "ToDo"

    # builder_settings
    VERSION = 'v0.0.1'
    ICON_NAME = "favicon.ico"
    DATA_DIR = 'data/'

    GEOMETRY = f"{1000}x{600}"

    STORAGE_PATH = 'storage.json'

    COLOR_SIDEBAR_BG = ('#ebebeb', '#303030')
    COLOR_SIDEBAR_BTN = "transparent"
    COLOR_SIDEBAR_BTN_HOVER = ("#d2d2d2", "#464646")
    COLOR_SIDEBAR_BTN_TEXT = ("gray10", "gray90")
    COLOR_SIDEBAR_BTN_ACTIVE = ("#d9d9d9", "#3f3f3f")

    COLOR_WINDOW_BG = ("#fafafa", "gray10")

    COLOR_BIG_LABEL_BG = COLOR_SIDEBAR_BG

    @staticmethod
    def get_base_config():
        pass

    @staticmethod
    def get_exe_file_name():
        """ Создаем имя для исполняемого файла (в зависимости от ОС) """
        name = ''
        if platform.system() == "Windows":
            name = f'{Settings.APP_NAME}_{Settings.VERSION}_{date.today().strftime("%Y.%m.%d")}.exe'
        elif platform.system() == "Linux":
            name = f'{Settings.APP_NAME}_{Settings.VERSION}_{date.today().strftime("%Y.%m.%d")}_{distro.id()}'
        return name
