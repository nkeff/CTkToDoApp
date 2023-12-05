import os
import platform
import shutil
import sys
from subprocess import Popen

from core.settings import Settings

try:
    import PyInstaller
except ImportError:
    PyInstaller = None
    raise SystemExit("Error: PyInstaller package missing. "
                     "To install type: pip install --upgrade pyinstaller")

def message(msg: list) -> str:
    linelen = 50
    tmp = '+' + '=' * linelen + '\n'
    for i in msg:
        tmp += '| ' + i + '\n'
    tmp += '+' + '=' * linelen
    print(tmp)
    return tmp


class BUILDER:
    def __init__(self):

        self.DIST_DIR = "dist/"
        self.BUILD_DIR = "build/"
        self.CMD = f"pyinstaller app.spec"

        self.APP_NAME = Settings.get_exe_file_name()

    def __delete_build_dir(self):
        if os.path.exists(self.BUILD_DIR):
            shutil.rmtree(self.BUILD_DIR)

    def __delete_dist_dir(self):
        if os.path.exists(self.DIST_DIR):
            shutil.rmtree(self.DIST_DIR)

    def __rename_bin_file(self):
        filename = 'app' if platform.system() == "Linux" else 'app.exe'
        shutil.move(
            os.path.join(self.DIST_DIR, filename),
            os.path.join(self.DIST_DIR, self.APP_NAME)
        )

    def run(self):
        self.__delete_dist_dir()
        self.__delete_build_dir()

        sub = Popen(self.CMD.split(' '))
        sub.communicate()
        rcode = sub.returncode
        if rcode != 0:
            print("Error: PyInstaller failed, code=%s" % rcode)
            self.__delete_dist_dir()
            self.__delete_build_dir()
            sys.exit(1)

        self.__delete_build_dir()
        self.__rename_bin_file()

        # Done
        message(['Сборка завершена!', 'Исполняемый файл находится в директории dist', self.APP_NAME])


if __name__ == "__main__":
    builder = BUILDER()
    builder.run()
