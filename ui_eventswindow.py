# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Events.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_EventsWindow(object):
    def setupUi(self, EventsWindow):
        if not EventsWindow.objectName():
            EventsWindow.setObjectName(u"EventsWindow")
        EventsWindow.resize(709, 729)
        self.centralwidget = QWidget(EventsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.FastPositionsLabel = QLabel(self.centralwidget)
        self.FastPositionsLabel.setObjectName(u"FastPositionsLabel")
        self.FastPositionsLabel.setGeometry(QRect(30, 20, 211, 19))
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 290, 356, 80))
        self.positionsButtonsLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.positionsButtonsLayout.setObjectName(u"positionsButtonsLayout")
        self.positionsButtonsLayout.setContentsMargins(0, 0, 0, 0)
        self.getPositions = QPushButton(self.horizontalLayoutWidget)
        self.getPositions.setObjectName(u"getPositions")

        self.positionsButtonsLayout.addWidget(self.getPositions)

        self.finalizePositions = QPushButton(self.horizontalLayoutWidget)
        self.finalizePositions.setObjectName(u"finalizePositions")

        self.positionsButtonsLayout.addWidget(self.finalizePositions)

        self.resetPositions = QPushButton(self.horizontalLayoutWidget)
        self.resetPositions.setObjectName(u"resetPositions")

        self.positionsButtonsLayout.addWidget(self.resetPositions)

        self.SlowPositionsLabel = QLabel(self.centralwidget)
        self.SlowPositionsLabel.setObjectName(u"SlowPositionsLabel")
        self.SlowPositionsLabel.setGeometry(QRect(390, 20, 111, 19))
        self.presetsBox = QGroupBox(self.centralwidget)
        self.presetsBox.setObjectName(u"presetsBox")
        self.presetsBox.setGeometry(QRect(30, 400, 491, 131))
        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(30, 50, 616, 194))
        self.positionListsLayout = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.positionListsLayout.setObjectName(u"positionListsLayout")
        self.positionListsLayout.setContentsMargins(0, 0, 0, 0)
        self.fastPositions = QListWidget(self.horizontalLayoutWidget_2)
        self.fastPositions.setObjectName(u"fastPositions")

        self.positionListsLayout.addWidget(self.fastPositions)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.sendToSlow = QPushButton(self.horizontalLayoutWidget_2)
        self.sendToSlow.setObjectName(u"sendToSlow")

        self.verticalLayout.addWidget(self.sendToSlow)

        self.sendToFast = QPushButton(self.horizontalLayoutWidget_2)
        self.sendToFast.setObjectName(u"sendToFast")

        self.verticalLayout.addWidget(self.sendToFast)


        self.positionListsLayout.addLayout(self.verticalLayout)

        self.slowPositions = QListWidget(self.horizontalLayoutWidget_2)
        self.slowPositions.setObjectName(u"slowPositions")

        self.positionListsLayout.addWidget(self.slowPositions)

        EventsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(EventsWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 709, 21))
        EventsWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(EventsWindow)
        self.statusbar.setObjectName(u"statusbar")
        EventsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(EventsWindow)

        QMetaObject.connectSlotsByName(EventsWindow)
    # setupUi

    def retranslateUi(self, EventsWindow):
        EventsWindow.setWindowTitle(QCoreApplication.translate("EventsWindow", u"MainWindow", None))
        self.FastPositionsLabel.setText(QCoreApplication.translate("EventsWindow", u"Fast Positions", None))
        self.getPositions.setText(QCoreApplication.translate("EventsWindow", u"Get Positions", None))
        self.finalizePositions.setText(QCoreApplication.translate("EventsWindow", u"Finalize Positions", None))
        self.resetPositions.setText(QCoreApplication.translate("EventsWindow", u"Reset Positions", None))
        self.SlowPositionsLabel.setText(QCoreApplication.translate("EventsWindow", u"Slow Positions", None))
        self.presetsBox.setTitle(QCoreApplication.translate("EventsWindow", u"Presets and Channels", None))
        self.sendToSlow.setText(QCoreApplication.translate("EventsWindow", u">", None))
        self.sendToFast.setText(QCoreApplication.translate("EventsWindow", u"<", None))
    # retranslateUi

