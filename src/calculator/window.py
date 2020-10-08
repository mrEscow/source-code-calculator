import asyncio
import os

from PySide2.QtCore import (QMetaObject, QRect, QSize, Qt, QUrl)
from PySide2.QtGui import (QDragEnterEvent, QDropEvent, QFont)
from PySide2.QtWidgets import *

from calculator.service import CodeCalculator


class MainWindow(QMainWindow):
    font: QFont
    container: QWidget
    drop_label: QLabel
    calculate_button: QPushButton
    status_bar: QStatusBar
    directory_path: str = None
    _is_calculating: bool

    def __init__(self):
        super().__init__()

        self.font = QFont()
        self.font.setPointSize(25)
        self.font.setKerning(True)
        self.font.setStyleStrategy(QFont.PreferAntialias)

        self.setMinimumSize(QSize(560, 260))
        self.setMaximumSize(QSize(560, 260))
        self.setAcceptDrops(True)
        self.setWindowTitle(u"Source Code Calculator")
        self.setFixedSize(self.size())

        self.setup_interface()
        self.init_handlers()

    def setup_interface(self):
        if not self.objectName():
            self.setObjectName(u"Form")

        self.setup_container()
        self.setup_calculate_button()
        self.setup_drop_label()
        self.setup_status_bar()

        QMetaObject.connectSlotsByName(self)

    def setup_container(self):
        self.container = QWidget(self)
        self.container.setObjectName(u"container")
        self.setCentralWidget(self.container)

    def setup_status_bar(self):
        self.status_bar = QStatusBar(self)
        self.status_bar.setObjectName(u"status_bar")
        self.setStatusBar(self.status_bar)

    def setup_drop_label(self):
        self.drop_label = QLabel(self.container)
        self.drop_label.setObjectName(u"drop_label")
        self.drop_label.setEnabled(True)
        self.drop_label.setGeometry(QRect(10, 10, 541, 171))
        self.drop_label.setFont(self.font)
        self.drop_label.setAutoFillBackground(False)
        self.drop_label.setFrameShape(QFrame.StyledPanel)
        self.drop_label.setText(u"Drop Your folder here")
        self.drop_label.setTextFormat(Qt.PlainText)
        self.drop_label.setAlignment(Qt.AlignCenter)

    def setup_calculate_button(self):
        self.calculate_button = QPushButton(self.container, text="Calculate")
        self.calculate_button.setObjectName(u"calculate_button")
        self.calculate_button.setEnabled(False)
        self.calculate_button.setGeometry(QRect(220, 190, 112, 32))
        self.calculate_button.setFocusPolicy(Qt.NoFocus)

    def init_handlers(self):
        self.calculate_button.clicked.connect(self.on_calculate)

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
