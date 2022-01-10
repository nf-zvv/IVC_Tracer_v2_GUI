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
        self.groupBox_2 = QtWidgets.QGroupBox(self.AvahTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(221, 171))
        self.groupBox_2.setMaximumSize(QtCore.QSize(221, 171))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 25, 51, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(30, 75, 41, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(40, 125, 31, 16))
        self.label_6.setObjectName("label_6")
        self.reverseBranchStart = QtWidgets.QSpinBox(self.groupBox_2)
        self.reverseBranchStart.setGeometry(QtCore.QRect(80, 20, 113, 28))
        self.reverseBranchStart.setMaximum(4095)
        self.reverseBranchStart.setObjectName("reverseBranchStart")
        self.reverseBranchEnd = QtWidgets.QSpinBox(self.groupBox_2)
        self.reverseBranchEnd.setGeometry(QtCore.QRect(80, 70, 113, 28))
        self.reverseBranchEnd.setMaximum(4095)
        self.reverseBranchEnd.setObjectName("reverseBranchEnd")
        self.reverseBranchStep = QtWidgets.QSpinBox(self.groupBox_2)
        self.reverseBranchStep.setGeometry(QtCore.QRect(80, 120, 113, 28))
        self.reverseBranchStep.setMaximum(4095)
        self.reverseBranchStep.setObjectName("reverseBranchStep")
        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.AvahTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(221, 171))
        self.groupBox.setMaximumSize(QtCore.QSize(221, 171))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 25, 51, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 75, 41, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(40, 125, 31, 16))
        self.label_3.setObjectName("label_3")
        self.forvardBranchStart = QtWidgets.QSpinBox(self.groupBox)
        self.forvardBranchStart.setGeometry(QtCore.QRect(80, 20, 113, 28))
        self.forvardBranchStart.setMaximum(4095)
        self.forvardBranchStart.setObjectName("forvardBranchStart")
        self.forvardBranchEnd = QtWidgets.QSpinBox(self.groupBox)
        self.forvardBranchEnd.setGeometry(QtCore.QRect(80, 70, 113, 28))
        self.forvardBranchEnd.setMaximum(4095)
        self.forvardBranchEnd.setObjectName("forvardBranchEnd")
        self.forvardBranchStep = QtWidgets.QSpinBox(self.groupBox)
        self.forvardBranchStep.setGeometry(QtCore.QRect(80, 120, 113, 28))
        self.forvardBranchStep.setMaximum(4095)
        self.forvardBranchStep.setObjectName("forvardBranchStep")
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.execButton = QtWidgets.QPushButton(self.AvahTab)
        self.execButton.setMinimumSize(QtCore.QSize(120, 0))
        self.execButton.setMaximumSize(QtCore.QSize(120, 16777215))
        self.execButton.setObjectName("execButton")
        self.horizontalLayout_7.addWidget(self.execButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 2, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.saveGraphButton = QtWidgets.QPushButton(self.AvahTab)
        self.saveGraphButton.setMinimumSize(QtCore.QSize(120, 0))
        self.saveGraphButton.setMaximumSize(QtCore.QSize(120, 16777215))
        self.saveGraphButton.setObjectName("saveGraphButton")
        self.horizontalLayout_6.addWidget(self.saveGraphButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 4, 0, 1, 1)
        self.plotWidget = MplWidget(self.AvahTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotWidget.sizePolicy().hasHeightForWidth())
        self.plotWidget.setSizePolicy(sizePolicy)
        self.plotWidget.setObjectName("plotWidget")
        self.gridLayout_2.addWidget(self.plotWidget, 0, 1, 5, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        self.tabWidget.addTab(self.AvahTab, "")
        self.ArchiveTab = QtWidgets.QWidget()
        self.ArchiveTab.setObjectName("ArchiveTab")
        self.tabWidget.addTab(self.ArchiveTab, "")
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
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Настройки порта"))
        self.pushButton_2.setText(_translate("MainWindow", "Подключиться"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.realtimeTab), _translate("MainWindow", "Realtime"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Обратная ветвь"))
        self.label_4.setText(_translate("MainWindow", "Начало:"))
        self.label_5.setText(_translate("MainWindow", "Конец:"))
        self.label_6.setText(_translate("MainWindow", "Шаг:"))
        self.groupBox.setTitle(_translate("MainWindow", "Прямая ветвь"))
        self.label.setText(_translate("MainWindow", "Начало:"))
        self.label_2.setText(_translate("MainWindow", "Конец:"))
        self.label_3.setText(_translate("MainWindow", "Шаг:"))
        self.execButton.setText(_translate("MainWindow", "Выполнить"))
        self.saveGraphButton.setText(_translate("MainWindow", "Сохранить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AvahTab), _translate("MainWindow", "АВАХ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ArchiveTab), _translate("MainWindow", "Архив"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Настройки"))
        self.menu_3.setTitle(_translate("MainWindow", "Справка"))
        self.action_uart_settings.setText(_translate("MainWindow", "Настройки соединения"))
        self.action_device_settings.setText(_translate("MainWindow", "Настройки прибора"))
        self.action_connect.setText(_translate("MainWindow", "Подключиться к прибору"))
        self.action_open.setText(_translate("MainWindow", "Открыть"))
        self.action_save.setText(_translate("MainWindow", "Сохранить"))
        self.action_exit.setText(_translate("MainWindow", "Выход"))
        self.action_about.setText(_translate("MainWindow", "О программе"))