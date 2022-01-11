# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Виталий\Desktop\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from mplwidget import MplWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 800))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.realtimeTab = QtWidgets.QWidget()
        self.realtimeTab.setObjectName("realtimeTab")
        self.pushButton = QtWidgets.QPushButton(self.realtimeTab)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 141, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.realtimeTab)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 50, 141, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.realtimeTab, "")
        self.AvahTab = QtWidgets.QWidget()
        self.AvahTab.setObjectName("AvahTab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.AvahTab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_ReverseBranch = QtWidgets.QGroupBox(self.AvahTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_ReverseBranch.sizePolicy().hasHeightForWidth())
        self.groupBox_ReverseBranch.setSizePolicy(sizePolicy)
        self.groupBox_ReverseBranch.setMinimumSize(QtCore.QSize(221, 130))
        self.groupBox_ReverseBranch.setMaximumSize(QtCore.QSize(221, 130))
        self.groupBox_ReverseBranch.setObjectName("groupBox_ReverseBranch")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_ReverseBranch)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.LabelRevBrBegin = QtWidgets.QLabel(self.groupBox_ReverseBranch)
        self.LabelRevBrBegin.setObjectName("LabelRevBrBegin")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.LabelRevBrBegin)
        self.RevBrBegin = QtWidgets.QSpinBox(self.groupBox_ReverseBranch)
        self.RevBrBegin.setMaximum(4095)
        self.RevBrBegin.setObjectName("RevBrBegin")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.RevBrBegin)
        self.LabelRevBrEnd = QtWidgets.QLabel(self.groupBox_ReverseBranch)
        self.LabelRevBrEnd.setObjectName("LabelRevBrEnd")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.LabelRevBrEnd)
        self.RevBrEnd = QtWidgets.QSpinBox(self.groupBox_ReverseBranch)
        self.RevBrEnd.setMaximum(4095)
        self.RevBrEnd.setObjectName("RevBrEnd")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.RevBrEnd)
        self.LabelRevBrStep = QtWidgets.QLabel(self.groupBox_ReverseBranch)
        self.LabelRevBrStep.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.LabelRevBrStep.setObjectName("LabelRevBrStep")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.LabelRevBrStep)
        self.RevBrStep = QtWidgets.QSpinBox(self.groupBox_ReverseBranch)
        self.RevBrStep.setMaximum(4095)
        self.RevBrStep.setObjectName("RevBrStep")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.RevBrStep)
        self.verticalLayout.addLayout(self.formLayout)
        self.gridLayout_2.addWidget(self.groupBox_ReverseBranch, 1, 0, 1, 1)
        self.groupBox_ForvardBranch = QtWidgets.QGroupBox(self.AvahTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_ForvardBranch.sizePolicy().hasHeightForWidth())
        self.groupBox_ForvardBranch.setSizePolicy(sizePolicy)
        self.groupBox_ForvardBranch.setMinimumSize(QtCore.QSize(221, 130))
        self.groupBox_ForvardBranch.setMaximumSize(QtCore.QSize(221, 130))
        self.groupBox_ForvardBranch.setObjectName("groupBox_ForvardBranch")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_ForvardBranch)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setObjectName("formLayout_2")
        self.LabelFrvdBrBegin = QtWidgets.QLabel(self.groupBox_ForvardBranch)
        self.LabelFrvdBrBegin.setObjectName("LabelFrvdBrBegin")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.LabelFrvdBrBegin)
        self.FrvdBrBegin = QtWidgets.QSpinBox(self.groupBox_ForvardBranch)
        self.FrvdBrBegin.setMaximum(4095)
        self.FrvdBrBegin.setObjectName("FrvdBrBegin")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.FrvdBrBegin)
        self.LabelFrvdBrEnd = QtWidgets.QLabel(self.groupBox_ForvardBranch)
        self.LabelFrvdBrEnd.setObjectName("LabelFrvdBrEnd")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.LabelFrvdBrEnd)
        self.FrvdBrEnd = QtWidgets.QSpinBox(self.groupBox_ForvardBranch)
        self.FrvdBrEnd.setMaximum(4095)
        self.FrvdBrEnd.setObjectName("FrvdBrEnd")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.FrvdBrEnd)
        self.LabelFrvdBrStep = QtWidgets.QLabel(self.groupBox_ForvardBranch)
        self.LabelFrvdBrStep.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.LabelFrvdBrStep.setObjectName("LabelFrvdBrStep")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.LabelFrvdBrStep)
        self.FrvdBrStep = QtWidgets.QSpinBox(self.groupBox_ForvardBranch)
        self.FrvdBrStep.setMaximum(4095)
        self.FrvdBrStep.setObjectName("FrvdBrStep")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.FrvdBrStep)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.gridLayout_2.addWidget(self.groupBox_ForvardBranch, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 5, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.saveGraphButton = QtWidgets.QPushButton(self.AvahTab)
        self.saveGraphButton.setMinimumSize(QtCore.QSize(120, 0))
        self.saveGraphButton.setMaximumSize(QtCore.QSize(120, 16777215))
        self.saveGraphButton.setObjectName("saveGraphButton")
        self.horizontalLayout_6.addWidget(self.saveGraphButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 4, 0, 1, 1)
        self.plotWidget = MplWidget(self.AvahTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotWidget.sizePolicy().hasHeightForWidth())
        self.plotWidget.setSizePolicy(sizePolicy)
        self.plotWidget.setObjectName("plotWidget")
        self.gridLayout_2.addWidget(self.plotWidget, 0, 1, 6, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.execButton = QtWidgets.QPushButton(self.AvahTab)
        self.execButton.setMinimumSize(QtCore.QSize(120, 0))
        self.execButton.setMaximumSize(QtCore.QSize(120, 16777215))
        self.execButton.setObjectName("execButton")
        self.horizontalLayout_7.addWidget(self.execButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 3, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.AvahTab)
        self.groupBox.setMinimumSize(QtCore.QSize(221, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(221, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 26))
        self.label.setMaximumSize(QtCore.QSize(16777215, 26))
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.dutName = QtWidgets.QLineEdit(self.groupBox)
        self.dutName.setMaximumSize(QtCore.QSize(16777215, 32))
        self.dutName.setText("")
        self.dutName.setObjectName("dutName")
        self.verticalLayout_3.addWidget(self.dutName)
        self.verticalLayout_7.addLayout(self.verticalLayout_3)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_3.setObjectName("formLayout_3")
        self.LabelIllumination = QtWidgets.QLabel(self.groupBox)
        self.LabelIllumination.setObjectName("LabelIllumination")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.LabelIllumination)
        self.illumination = QtWidgets.QLineEdit(self.groupBox)
        self.illumination.setObjectName("illumination")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.illumination)
        self.LabelTemperature = QtWidgets.QLabel(self.groupBox)
        self.LabelTemperature.setObjectName("LabelTemperature")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.LabelTemperature)
        self.temperature = QtWidgets.QLineEdit(self.groupBox)
        self.temperature.setObjectName("temperature")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.temperature)
        self.verticalLayout_7.addLayout(self.formLayout_3)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setMinimumSize(QtCore.QSize(0, 28))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 28))
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.comment = QtWidgets.QPlainTextEdit(self.groupBox)
        self.comment.setPlainText("")
        self.comment.setObjectName("comment")
        self.verticalLayout_6.addWidget(self.comment)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.gridLayout_2.addWidget(self.groupBox, 2, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        self.tabWidget.addTab(self.AvahTab, "")
        self.ArchiveTab = QtWidgets.QWidget()
        self.ArchiveTab.setObjectName("ArchiveTab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.ArchiveTab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 4, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_4 = QtWidgets.QGroupBox(self.ArchiveTab)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_4.addWidget(self.groupBox_4)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 0, 1, 5, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.removeDataFile = QtWidgets.QPushButton(self.ArchiveTab)
        self.removeDataFile.setMaximumSize(QtCore.QSize(120, 16777215))
        self.removeDataFile.setObjectName("removeDataFile")
        self.horizontalLayout_3.addWidget(self.removeDataFile)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.ArchiveTab)
        self.groupBox_2.setMinimumSize(QtCore.QSize(250, 0))
        self.groupBox_2.setMaximumSize(QtCore.QSize(221, 16777215))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(0, 26))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 26))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_9.addWidget(self.label_2)
        self.dutNameValue = QtWidgets.QLabel(self.groupBox_2)
        self.dutNameValue.setText("")
        self.dutNameValue.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.dutNameValue.setObjectName("dutNameValue")
        self.verticalLayout_9.addWidget(self.dutNameValue)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setMinimumSize(QtCore.QSize(0, 26))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 26))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.dateValue = QtWidgets.QLabel(self.groupBox_2)
        self.dateValue.setText("")
        self.dateValue.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.dateValue.setObjectName("dateValue")
        self.horizontalLayout_8.addWidget(self.dateValue)
        self.verticalLayout_9.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setMinimumSize(QtCore.QSize(0, 26))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 26))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_9.addWidget(self.label_8)
        self.timeValue = QtWidgets.QLabel(self.groupBox_2)
        self.timeValue.setText("")
        self.timeValue.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.timeValue.setObjectName("timeValue")
        self.horizontalLayout_9.addWidget(self.timeValue)
        self.verticalLayout_9.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setMinimumSize(QtCore.QSize(0, 26))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 26))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.illuminationValue = QtWidgets.QLabel(self.groupBox_2)
        self.illuminationValue.setText("")
        self.illuminationValue.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.illuminationValue.setObjectName("illuminationValue")
        self.horizontalLayout_5.addWidget(self.illuminationValue)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setMinimumSize(QtCore.QSize(0, 26))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 26))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.temperatureValue = QtWidgets.QLabel(self.groupBox_2)
        self.temperatureValue.setText("")
        self.temperatureValue.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.temperatureValue.setObjectName("temperatureValue")
        self.horizontalLayout_4.addWidget(self.temperatureValue)
        self.verticalLayout_9.addLayout(self.horizontalLayout_4)
        self.verticalLayout_8.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setMinimumSize(QtCore.QSize(0, 28))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 28))
        self.label_5.setObjectName("label_5")
        self.verticalLayout_10.addWidget(self.label_5)
        self.comment_2 = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.comment_2.setReadOnly(True)
        self.comment_2.setPlainText("")
        self.comment_2.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.comment_2.setObjectName("comment_2")
        self.verticalLayout_10.addWidget(self.comment_2)
        self.verticalLayout_8.addLayout(self.verticalLayout_10)
        self.gridLayout_3.addWidget(self.groupBox_2, 2, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.ArchiveTab)
        self.groupBox_3.setMinimumSize(QtCore.QSize(250, 0))
        self.groupBox_3.setMaximumSize(QtCore.QSize(250, 16777215))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.listOfFiles = QtWidgets.QListWidget(self.groupBox_3)
        self.listOfFiles.setMinimumSize(QtCore.QSize(226, 0))
        self.listOfFiles.setMaximumSize(QtCore.QSize(226, 400))
        self.listOfFiles.setObjectName("listOfFiles")
        self.verticalLayout_12.addWidget(self.listOfFiles)
        self.gridLayout_3.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_3)
        self.tabWidget.addTab(self.ArchiveTab, "")
        self.AnalyseTab = QtWidgets.QWidget()
        self.AnalyseTab.setObjectName("AnalyseTab")
        self.tabWidget.addTab(self.AnalyseTab, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_uart_settings = QtWidgets.QAction(MainWindow)
        self.action_uart_settings.setObjectName("action_uart_settings")
        self.action_device_settings = QtWidgets.QAction(MainWindow)
        self.action_device_settings.setObjectName("action_device_settings")
        self.action_connect = QtWidgets.QAction(MainWindow)
        self.action_connect.setCheckable(False)
        self.action_connect.setObjectName("action_connect")
        self.action_open = QtWidgets.QAction(MainWindow)
        self.action_open.setObjectName("action_open")
        self.action_save = QtWidgets.QAction(MainWindow)
        self.action_save.setObjectName("action_save")
        self.action_exit = QtWidgets.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.menu.addAction(self.action_open)
        self.menu.addAction(self.action_save)
        self.menu.addSeparator()
        self.menu.addAction(self.action_exit)
        self.menu_2.addAction(self.action_uart_settings)
        self.menu_2.addAction(self.action_connect)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action_device_settings)
        self.menu_3.addAction(self.action_about)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.RevBrStep)
        MainWindow.setTabOrder(self.RevBrStep, self.RevBrEnd)
        MainWindow.setTabOrder(self.RevBrEnd, self.RevBrBegin)
        MainWindow.setTabOrder(self.RevBrBegin, self.execButton)
        MainWindow.setTabOrder(self.execButton, self.FrvdBrBegin)
        MainWindow.setTabOrder(self.FrvdBrBegin, self.FrvdBrEnd)
        MainWindow.setTabOrder(self.FrvdBrEnd, self.FrvdBrStep)
        MainWindow.setTabOrder(self.FrvdBrStep, self.dutName)
        MainWindow.setTabOrder(self.dutName, self.illumination)
        MainWindow.setTabOrder(self.illumination, self.temperature)
        MainWindow.setTabOrder(self.temperature, self.comment)
        MainWindow.setTabOrder(self.comment, self.saveGraphButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IVC_Tracer_v2_GUI"))
        self.pushButton.setText(_translate("MainWindow", "Настройки порта"))
        self.pushButton_2.setText(_translate("MainWindow", "Подключиться"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.realtimeTab), _translate("MainWindow", "Realtime"))
        self.groupBox_ReverseBranch.setTitle(_translate("MainWindow", "Обратная ветвь"))
        self.LabelRevBrBegin.setText(_translate("MainWindow", "Начало:"))
        self.LabelRevBrEnd.setText(_translate("MainWindow", "Конец:"))
        self.LabelRevBrStep.setText(_translate("MainWindow", "Шаг:"))
        self.groupBox_ForvardBranch.setTitle(_translate("MainWindow", "Прямая ветвь"))
        self.LabelFrvdBrBegin.setText(_translate("MainWindow", "Начало:"))
        self.LabelFrvdBrEnd.setText(_translate("MainWindow", "Конец:"))
        self.LabelFrvdBrStep.setText(_translate("MainWindow", "Шаг:"))
        self.saveGraphButton.setText(_translate("MainWindow", "Сохранить"))
        self.execButton.setText(_translate("MainWindow", "Выполнить"))
        self.groupBox.setTitle(_translate("MainWindow", "Информация"))
        self.label.setText(_translate("MainWindow", "Название:"))
        self.LabelIllumination.setText(_translate("MainWindow", "Освещенность:"))
        self.LabelTemperature.setText(_translate("MainWindow", "Температура:"))
        self.label_4.setText(_translate("MainWindow", "Комментарий:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AvahTab), _translate("MainWindow", "АВАХ"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Результат"))
        self.removeDataFile.setText(_translate("MainWindow", "Удалить"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Информация"))
        self.label_2.setText(_translate("MainWindow", "Название:"))
        self.label_7.setText(_translate("MainWindow", "Дата:"))
        self.label_8.setText(_translate("MainWindow", "Время:"))
        self.label_6.setText(_translate("MainWindow", "Освещенность:"))
        self.label_3.setText(_translate("MainWindow", "Температура:"))
        self.label_5.setText(_translate("MainWindow", "Комментарий:"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Выберите файл данных"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ArchiveTab), _translate("MainWindow", "Архив"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AnalyseTab), _translate("MainWindow", "Анализ"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Настройки"))
        self.menu_3.setTitle(_translate("MainWindow", "Справка"))
        self.action_uart_settings.setText(_translate("MainWindow", "Настройки соединения"))
        self.action_device_settings.setText(_translate("MainWindow", "Настройки прибора"))
        self.action_connect.setText(_translate("MainWindow", "Подключиться к прибору"))
        self.action_open.setText(_translate("MainWindow", "Открыть"))
        self.action_open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_save.setText(_translate("MainWindow", "Сохранить"))
        self.action_exit.setText(_translate("MainWindow", "Выход"))
        self.action_about.setText(_translate("MainWindow", "О программе"))
