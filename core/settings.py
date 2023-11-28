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
