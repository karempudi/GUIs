# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewSetup.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_viewWindow(object):
    def setupUi(self, viewWindow):
        if not viewWindow.objectName():
            viewWindow.setObjectName(u"viewWindow")
        viewWindow.resize(296, 263)
        self.centralwidget = QWidget(viewWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.viewBoxText = QTextEdit(self.centralwidget)
        self.viewBoxText.setObjectName(u"viewBoxText")
        self.viewBoxText.setGeometry(QRect(20, 10, 251, 161))
        self.closeButton = QPushButton(self.centralwidget)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setGeometry(QRect(180, 180, 75, 23))
        viewWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(viewWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 296, 21))
        viewWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(viewWindow)
        self.statusbar.setObjectName(u"statusbar")
        viewWindow.setStatusBar(self.statusbar)

        self.retranslateUi(viewWindow)

        QMetaObject.connectSlotsByName(viewWindow)
    # setupUi

    def retranslateUi(self, viewWindow):
        viewWindow.setWindowTitle(QCoreApplication.translate("viewWindow", u"MainWindow", None))
        self.closeButton.setText(QCoreApplication.translate("viewWindow", u"close", None))
    # retranslateUi

