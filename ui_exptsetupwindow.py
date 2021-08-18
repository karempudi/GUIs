# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setupWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_SetupWindow(object):
    def setupUi(self, SetupWindow):
        if not SetupWindow.objectName():
            SetupWindow.setObjectName(u"SetupWindow")
        SetupWindow.resize(615, 814)
        self.centralwidget = QWidget(SetupWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.exptSetupBox = QGroupBox(self.centralwidget)
        self.exptSetupBox.setObjectName(u"exptSetupBox")
        self.exptSetupBox.setGeometry(QRect(30, 10, 541, 231))
        self.horizontalLayoutWidget_3 = QWidget(self.exptSetupBox)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 20, 431, 41))
        self.exptNoLayout = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.exptNoLayout.setObjectName(u"exptNoLayout")
        self.exptNoLayout.setContentsMargins(0, 0, 0, 0)
        self.exptNoLabel = QLabel(self.horizontalLayoutWidget_3)
        self.exptNoLabel.setObjectName(u"exptNoLabel")

        self.exptNoLayout.addWidget(self.exptNoLabel)

        self.exptNoText = QLineEdit(self.horizontalLayoutWidget_3)
        self.exptNoText.setObjectName(u"exptNoText")

        self.exptNoLayout.addWidget(self.exptNoText)

        self.horizontalLayoutWidget_4 = QWidget(self.exptSetupBox)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(10, 60, 431, 41))
        self.positionsInputLayout = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.positionsInputLayout.setObjectName(u"positionsInputLayout")
        self.positionsInputLayout.setContentsMargins(0, 0, 0, 0)
        self.positionsInputLabel = QLabel(self.horizontalLayoutWidget_4)
        self.positionsInputLabel.setObjectName(u"positionsInputLabel")

        self.positionsInputLayout.addWidget(self.positionsInputLabel)

        self.fromFile = QRadioButton(self.horizontalLayoutWidget_4)
        self.fromFile.setObjectName(u"fromFile")

        self.positionsInputLayout.addWidget(self.fromFile)

        self.fromMicroManager = QRadioButton(self.horizontalLayoutWidget_4)
        self.fromMicroManager.setObjectName(u"fromMicroManager")

        self.positionsInputLayout.addWidget(self.fromMicroManager)

        self.horizontalLayoutWidget_5 = QWidget(self.exptSetupBox)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(10, 100, 431, 41))
        self.fileSelectionLayout = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.fileSelectionLayout.setObjectName(u"fileSelectionLayout")
        self.fileSelectionLayout.setContentsMargins(0, 0, 0, 0)
        self.fileSelectionLabel = QLabel(self.horizontalLayoutWidget_5)
        self.fileSelectionLabel.setObjectName(u"fileSelectionLabel")

        self.fileSelectionLayout.addWidget(self.fileSelectionLabel)

        self.fileSelectionButton = QPushButton(self.horizontalLayoutWidget_5)
        self.fileSelectionButton.setObjectName(u"fileSelectionButton")

        self.fileSelectionLayout.addWidget(self.fileSelectionButton)

        self.horizontalLayoutWidget_6 = QWidget(self.exptSetupBox)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 150, 431, 41))
        self.eventsCreationLayout = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.eventsCreationLayout.setObjectName(u"eventsCreationLayout")
        self.eventsCreationLayout.setContentsMargins(0, 0, 0, 0)
        self.eventsCreationLabel = QLabel(self.horizontalLayoutWidget_6)
        self.eventsCreationLabel.setObjectName(u"eventsCreationLabel")

        self.eventsCreationLayout.addWidget(self.eventsCreationLabel)

        self.eventsCreationButton = QPushButton(self.horizontalLayoutWidget_6)
        self.eventsCreationButton.setObjectName(u"eventsCreationButton")

        self.eventsCreationLayout.addWidget(self.eventsCreationButton)

        self.analysisSetupBox = QGroupBox(self.centralwidget)
        self.analysisSetupBox.setObjectName(u"analysisSetupBox")
        self.analysisSetupBox.setGeometry(QRect(30, 260, 541, 441))
        self.horizontalLayoutWidget = QWidget(self.analysisSetupBox)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 40, 431, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboBox = QComboBox(self.horizontalLayoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)

        self.databaseTablesBox = QGroupBox(self.analysisSetupBox)
        self.databaseTablesBox.setObjectName(u"databaseTablesBox")
        self.databaseTablesBox.setGeometry(QRect(20, 230, 501, 101))
        self.acquiredCheck = QCheckBox(self.databaseTablesBox)
        self.acquiredCheck.setObjectName(u"acquiredCheck")
        self.acquiredCheck.setGeometry(QRect(10, 30, 131, 23))
        self.segCellsChannelsCheck = QCheckBox(self.databaseTablesBox)
        self.segCellsChannelsCheck.setObjectName(u"segCellsChannelsCheck")
        self.segCellsChannelsCheck.setGeometry(QRect(160, 30, 251, 23))
        self.deadAliveCheck = QCheckBox(self.databaseTablesBox)
        self.deadAliveCheck.setObjectName(u"deadAliveCheck")
        self.deadAliveCheck.setGeometry(QRect(10, 60, 91, 23))
        self.growthRatesCheck = QCheckBox(self.databaseTablesBox)
        self.growthRatesCheck.setObjectName(u"growthRatesCheck")
        self.growthRatesCheck.setGeometry(QRect(120, 60, 131, 23))
        self.horizontalLayoutWidget_7 = QWidget(self.analysisSetupBox)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(20, 80, 431, 31))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.horizontalLayoutWidget_7)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_7.addWidget(self.checkBox)

        self.horizontalLayoutWidget_8 = QWidget(self.analysisSetupBox)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(20, 120, 431, 31))
        self.horizontalLayout_8 = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.checkBox_6 = QCheckBox(self.horizontalLayoutWidget_8)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.horizontalLayout_8.addWidget(self.checkBox_6)

        self.checkBox_7 = QCheckBox(self.horizontalLayoutWidget_8)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.horizontalLayout_8.addWidget(self.checkBox_7)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(350, 710, 221, 51))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        SetupWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(SetupWindow)
        self.statusbar.setObjectName(u"statusbar")
        SetupWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(SetupWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 615, 21))
        SetupWindow.setMenuBar(self.menubar)

        self.retranslateUi(SetupWindow)

        QMetaObject.connectSlotsByName(SetupWindow)
    # setupUi

    def retranslateUi(self, SetupWindow):
        SetupWindow.setWindowTitle(QCoreApplication.translate("SetupWindow", u"SetupWindow", None))
        self.exptSetupBox.setTitle(QCoreApplication.translate("SetupWindow", u"Experiment Setup", None))
        self.exptNoLabel.setText(QCoreApplication.translate("SetupWindow", u"Experiment No:", None))
        self.exptNoText.setText(QCoreApplication.translate("SetupWindow", u"EXP-21-BP000", None))
        self.positionsInputLabel.setText(QCoreApplication.translate("SetupWindow", u"Positions:", None))
        self.fromFile.setText(QCoreApplication.translate("SetupWindow", u"File", None))
        self.fromMicroManager.setText(QCoreApplication.translate("SetupWindow", u"Micromanager", None))
        self.fileSelectionLabel.setText(QCoreApplication.translate("SetupWindow", u"If File Select File:", None))
        self.fileSelectionButton.setText(QCoreApplication.translate("SetupWindow", u"Select File", None))
        self.eventsCreationLabel.setText(QCoreApplication.translate("SetupWindow", u"Events Creation:", None))
        self.eventsCreationButton.setText(QCoreApplication.translate("SetupWindow", u"Create Events", None))
        self.analysisSetupBox.setTitle(QCoreApplication.translate("SetupWindow", u"Analysis Setup", None))
        self.label.setText(QCoreApplication.translate("SetupWindow", u"Cell Segmentation: ", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("SetupWindow", u"Normal U-net", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("SetupWindow", u"Small U-net", None))

        self.databaseTablesBox.setTitle(QCoreApplication.translate("SetupWindow", u"Database Tables", None))
        self.acquiredCheck.setText(QCoreApplication.translate("SetupWindow", u"Acquired", None))
        self.segCellsChannelsCheck.setText(QCoreApplication.translate("SetupWindow", u"Seg Cells and Channel Detection", None))
        self.deadAliveCheck.setText(QCoreApplication.translate("SetupWindow", u"DeadAlive", None))
        self.growthRatesCheck.setText(QCoreApplication.translate("SetupWindow", u"GrowthRates", None))
        self.checkBox.setText(QCoreApplication.translate("SetupWindow", u"Channel Segmentation", None))
        self.checkBox_6.setText(QCoreApplication.translate("SetupWindow", u"DeadAlive", None))
        self.checkBox_7.setText(QCoreApplication.translate("SetupWindow", u"Growth Rates", None))
        self.pushButton_3.setText(QCoreApplication.translate("SetupWindow", u"Save", None))
        self.pushButton_2.setText(QCoreApplication.translate("SetupWindow", u"Close", None))
    # retranslateUi

