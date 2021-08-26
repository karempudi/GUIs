# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from pyqtgraph import ImageView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(980, 837)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Setup = QGroupBox(self.centralwidget)
        self.Setup.setObjectName(u"Setup")
        self.Setup.setGeometry(QRect(10, 20, 201, 151))
        self.setupButton = QPushButton(self.Setup)
        self.setupButton.setObjectName(u"setupButton")
        self.setupButton.setGeometry(QRect(10, 30, 88, 27))
        self.viewButton = QPushButton(self.Setup)
        self.viewButton.setObjectName(u"viewButton")
        self.viewButton.setGeometry(QRect(10, 70, 88, 27))
        self.viewerBox = QGroupBox(self.centralwidget)
        self.viewerBox.setObjectName(u"viewerBox")
        self.viewerBox.setGeometry(QRect(20, 430, 621, 311))
        self.runStatus = QGroupBox(self.centralwidget)
        self.runStatus.setObjectName(u"runStatus")
        self.runStatus.setGeometry(QRect(20, 180, 861, 241))
        self.imgArrivalPlot = ImageView(self.runStatus)
        self.imgArrivalPlot.setObjectName(u"imgArrivalPlot")
        self.imgArrivalPlot.setGeometry(QRect(20, 30, 181, 181))
        self.imgSegPlot = QGraphicsView(self.runStatus)
        self.imgSegPlot.setObjectName(u"imgSegPlot")
        self.imgSegPlot.setGeometry(QRect(230, 30, 181, 181))
        self.deadAlivePlot = QGraphicsView(self.runStatus)
        self.deadAlivePlot.setObjectName(u"deadAlivePlot")
        self.deadAlivePlot.setGeometry(QRect(440, 30, 181, 181))
        self.growthRatePlot = QGraphicsView(self.runStatus)
        self.growthRatePlot.setObjectName(u"growthRatePlot")
        self.growthRatePlot.setGeometry(QRect(650, 30, 181, 181))
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(230, 20, 481, 151))
        self.stopExptButton = QPushButton(self.groupBox_3)
        self.stopExptButton.setObjectName(u"stopExptButton")
        self.stopExptButton.setGeometry(QRect(20, 70, 88, 27))
        self.pushButton_3 = QPushButton(self.groupBox_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(20, 30, 88, 27))
        self.startAnalysisButton = QPushButton(self.groupBox_3)
        self.startAnalysisButton.setObjectName(u"startAnalysisButton")
        self.startAnalysisButton.setGeometry(QRect(130, 30, 121, 27))
        self.pushButton_5 = QPushButton(self.groupBox_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(130, 70, 121, 27))
        self.createDbButton = QPushButton(self.groupBox_3)
        self.createDbButton.setObjectName(u"createDbButton")
        self.createDbButton.setGeometry(QRect(260, 30, 121, 27))
        self.pushButton_8 = QPushButton(self.groupBox_3)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(20, 110, 111, 23))
        self.pushButton_9 = QPushButton(self.groupBox_3)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(140, 110, 121, 23))
        self.createTablesButton = QPushButton(self.groupBox_3)
        self.createTablesButton.setObjectName(u"createTablesButton")
        self.createTablesButton.setGeometry(QRect(260, 80, 111, 21))
        self.statisticsBox = QGroupBox(self.centralwidget)
        self.statisticsBox.setObjectName(u"statisticsBox")
        self.statisticsBox.setGeometry(QRect(650, 430, 231, 311))
        self.deadAliveStatsButton = QPushButton(self.statisticsBox)
        self.deadAliveStatsButton.setObjectName(u"deadAliveStatsButton")
        self.deadAliveStatsButton.setGeometry(QRect(50, 30, 88, 27))
        self.fillRateButton = QPushButton(self.statisticsBox)
        self.fillRateButton.setObjectName(u"fillRateButton")
        self.fillRateButton.setGeometry(QRect(50, 70, 88, 27))
        self.resetButton = QPushButton(self.centralwidget)
        self.resetButton.setObjectName(u"resetButton")
        self.resetButton.setGeometry(QRect(670, 760, 75, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 980, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuExit = QMenu(self.menubar)
        self.menuExit.setObjectName(u"menuExit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Setup.setTitle(QCoreApplication.translate("MainWindow", u"Setup", None))
        self.setupButton.setText(QCoreApplication.translate("MainWindow", u"Setup", None))
        self.viewButton.setText(QCoreApplication.translate("MainWindow", u"View ", None))
        self.viewerBox.setTitle(QCoreApplication.translate("MainWindow", u"Viewer", None))
        self.runStatus.setTitle(QCoreApplication.translate("MainWindow", u"Experiment Status", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Controls", None))
        self.stopExptButton.setText(QCoreApplication.translate("MainWindow", u"Stop Expt", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Start Expt", None))
        self.startAnalysisButton.setText(QCoreApplication.translate("MainWindow", u"Start Analysis", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Stop Analysis", None))
        self.createDbButton.setText(QCoreApplication.translate("MainWindow", u"Create database", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Move To Position No", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Tweeze Position", None))
        self.createTablesButton.setText(QCoreApplication.translate("MainWindow", u"Create tables", None))
        self.statisticsBox.setTitle(QCoreApplication.translate("MainWindow", u"Statistics", None))
        self.deadAliveStatsButton.setText(QCoreApplication.translate("MainWindow", u"DeadAlive", None))
        self.fillRateButton.setText(QCoreApplication.translate("MainWindow", u"Fill Rate", None))
        self.resetButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuExit.setTitle(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

