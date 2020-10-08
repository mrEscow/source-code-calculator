import asyncio
from asyncio import AbstractEventLoop

from asyncqt import QEventLoop
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication

from calculator.window import MainWindow

try:
    # noinspection PyUnresolvedReferences
    from PySide2.QtWinExtras import QtWin

    QtWin.setCurrentProcessExplicitAppUserModelID("com.manchenkov.source_calc")
except ImportError:
    pass


def run_app():
    app = QApplication()
    app.setWindowIcon(QIcon('icon.ico'))

    event_loop: AbstractEventLoop = QEventLoop()
    asyncio.set_event_loop(event_loop)

    form = MainWindow()
    form.show()

    event_loop.run_forever()


if __name__ == '__main__':
    run_app()
