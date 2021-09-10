# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testProcess.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_testProcess(object):
    def setupUi(self, testProcess):
        if not testProcess.objectName():
            testProcess.setObjectName(u"testProcess")
        testProcess.resize(323, 313)
        self.centralwidget = QWidget(testProcess)
        self.centralwidget.setObjectName(u"centralwidget")
        self.processButton = QPushButton(self.centralwidget)
        self.processButton.setObjectName(u"processButton")
        self.processButton.setGeometry(QRect(20, 10, 291, 31))
        self.text = QPlainTextEdit(self.centralwidget)
        self.text.setObjectName(u"text")
        self.text.setGeometry(QRect(20, 50, 291, 211))
        self.text.setReadOnly(True)
        testProcess.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(testProcess)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 323, 21))
        testProcess.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(testProcess)
        self.statusbar.setObjectName(u"statusbar")
        testProcess.setStatusBar(self.statusbar)

        self.retranslateUi(testProcess)

        QMetaObject.connectSlotsByName(testProcess)
    # setupUi

    def retranslateUi(self, testProcess):
        testProcess.setWindowTitle(QCoreApplication.translate("testProcess", u"MainWindow", None))
        self.processButton.setText(QCoreApplication.translate("testProcess", u"Start process1", None))
    # retranslateUi

