import asyncio
import os
from typing import List
from PySide2.QtCore import QUrl
from PySide2.QtGui import QDropEvent, QDragEnterEvent
from PySide2.QtWidgets import QMainWindow
from app.form import Ui_Form


class CodeCalculator:
    source: str
    paths: List[str]

    def __init__(self, source: str):
        self.source = source
        self.paths = []

    async def count(self) -> int:
        self.generate_path_map()

        result = await self.calculate()

        return result

    def generate_path_map(self):
        directory_items = (os.path.join(self.source, x) for x in os.listdir(self.source) if not x.startswith('.'))

        for item in directory_items:
            if os.path.isfile(item):
                self.paths.append(item)
                continue

            for root, subdirectories, files in os.walk(item):
                self.paths.extend([os.path.join(root, x) for x in files if not x.startswith('.')])

    async def calculate(self) -> int:
        count = 0

        for file_path in self.paths:
            await asyncio.sleep(0)

            with open(file_path, 'rt') as file:
                try:
                    count += len(file.readlines())
                except UnicodeDecodeError:
                    continue

        return count


class MainWindow(Ui_Form, QMainWindow):
    directory_path: str = None
    _is_calculating: bool

    def __init__(self):
        super().__init__()

        self.setFixedSize(self.size())
        self.setupUi(self)
        self.init_handlers()

    @property
    def is_calculating(self):
        return self._is_calculating

    @is_calculating.setter
    def is_calculating(self, value):
        self._is_calculating = value
        self.setAcceptDrops(not value)
        self.calculate_button.setEnabled(not value)

        if value:
            self.drop_label.setText("Calculating ...")

    def init_handlers(self):
        self.calculate_button.clicked.connect(self.on_calculate)

    def on_calculate(self):
        if self.directory_path is not None:
            self.is_calculating = True
            asyncio.create_task(self.calculate())

    async def calculate(self):
        calculator = CodeCalculator(self.directory_path)
        lines_of_code = await calculator.count()
        self.after_calculate(lines_of_code)

    def after_calculate(self, result: int):
        self.drop_label.setText(f"Lines of code: {result:0,d}")
        self.is_calculating = False

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        uri: QUrl = event.mimeData().urls()[0]
        self.update_selected_path(uri)

    def update_selected_path(self, uri: QUrl):
        path = uri.toLocalFile()

        if not os.path.isdir(path):
            self.drop_label.setText("Drop directory instead of files")
            return

        self.directory_path = path

        max_label_length = 40

        if len(path) > max_label_length:
            path = path[:max_label_length] + '...'

        self.drop_label.setText(path)
        self.calculate_button.setEnabled(True)
        self.drop_label.setToolTip(self.directory_path)
