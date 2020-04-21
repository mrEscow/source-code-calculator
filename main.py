import asyncio
from asyncio import AbstractEventLoop
from PySide2.QtWidgets import QApplication
from asyncqt import QEventLoop
from app.calculator import MainWindow

if __name__ == '__main__':
    app = QApplication()
    event_loop: AbstractEventLoop = QEventLoop()

    asyncio.set_event_loop(event_loop)

    form = MainWindow()
    form.show()

    event_loop.run_forever()
