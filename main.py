import asyncio
from asyncio import AbstractEventLoop
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication
from asyncqt import QEventLoop
from app.calculator import MainWindow

try:
    from PySide2.QtWinExtras import QtWin

    app_id = 'com.manchenkov.source_calc'
    QtWin.setCurrentProcessExplicitAppUserModelID(app_id)
except ImportError:
    pass

if __name__ == '__main__':
    app = QApplication()
    app.setWindowIcon(QIcon('icon.ico'))

    event_loop: AbstractEventLoop = QEventLoop()

    asyncio.set_event_loop(event_loop)

    form = MainWindow()
    form.show()

    event_loop.run_forever()
