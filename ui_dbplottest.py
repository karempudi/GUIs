# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dbPlotTest.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from pyqtgraph import ImageView


class Ui_dbPlotWindow(object):
    def setupUi(self, dbPlotWindow):
        if not dbPlotWindow.objectName():
            dbPlotWindow.setObjectName(u"dbPlotWindow")
        dbPlotWindow.resize(458, 437)
        self.centralwidget = QWidget(dbPlotWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.plot = ImageView(self.centralwidget)
        self.plot.setObjectName(u"plot")
        self.plot.setGeometry(QRect(40, 80, 281, 231))
        self.startWriteButton = QPushButton(self.centralwidget)
        self.startWriteButton.setObjectName(u"startWriteButton")
        self.startWriteButton.setGeometry(QRect(40, 30, 75, 23))
        self.startPlotButton = QPushButton(self.centralwidget)
        self.startPlotButton.setObjectName(u"startPlotButton")
        self.startPlotButton.setGeometry(QRect(160, 30, 75, 23))
        dbPlotWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(dbPlotWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 458, 21))
        dbPlotWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(dbPlotWindow)
        self.statusbar.setObjectName(u"statusbar")
        dbPlotWindow.setStatusBar(self.statusbar)

        self.retranslateUi(dbPlotWindow)

        QMetaObject.connectSlotsByName(dbPlotWindow)
    # setupUi

    def retranslateUi(self, dbPlotWindow):
        dbPlotWindow.setWindowTitle(QCoreApplication.translate("dbPlotWindow", u"MainWindow", None))
        self.startWriteButton.setText(QCoreApplication.translate("dbPlotWindow", u"Start db write", None))
        self.startPlotButton.setText(QCoreApplication.translate("dbPlotWindow", u"Start Plotting", None))
    # retranslateUi

