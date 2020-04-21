# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setMinimumSize(QSize(560, 260))
        Form.setMaximumSize(QSize(560, 260))
        Form.setAcceptDrops(True)
        Form.setWindowTitle(u"Source Code Calculator")
        self.centralwidget = QWidget(Form)
        self.centralwidget.setObjectName(u"centralwidget")
        self.calculate_button = QPushButton(self.centralwidget)
        self.calculate_button.setObjectName(u"calculate_button")
        self.calculate_button.setEnabled(False)
        self.calculate_button.setGeometry(QRect(220, 190, 112, 32))
        self.calculate_button.setFocusPolicy(Qt.NoFocus)
        self.calculate_button.setText(u"Calculate")
        self.drop_label = QLabel(self.centralwidget)
        self.drop_label.setObjectName(u"drop_label")
        self.drop_label.setEnabled(True)
        self.drop_label.setGeometry(QRect(10, 10, 541, 171))
        font = QFont()
        font.setPointSize(25)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.drop_label.setFont(font)
        self.drop_label.setAutoFillBackground(False)
        self.drop_label.setFrameShape(QFrame.StyledPanel)
        self.drop_label.setText(u"Drop Your folder here")
        self.drop_label.setTextFormat(Qt.PlainText)
        self.drop_label.setAlignment(Qt.AlignCenter)
        Form.setCentralWidget(self.centralwidget)
        self.status_bar = QStatusBar(Form)
        self.status_bar.setObjectName(u"status_bar")
        Form.setStatusBar(self.status_bar)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        pass
    # retranslateUi

