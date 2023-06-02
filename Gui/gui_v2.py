# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_v2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(667, 499)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background: rgba(255, 255, 255, 10);\n"
"color: rgb(190, 252, 255)")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabWidget::pane {\n"
"    background: transparent;\n"
"    border:0;\n"
"} \n"
"\n"
"QTabBar::tab {\n"
"  width: 100px;\n"
"  height: 20px;\n"
"  background: none; \n"
"  border-radius: 3px; \n"
"  border-bottom-left-radius: 0px;\n"
"  border-bottom-right-radius: 0px;\n"
"  color: rgb(190, 252, 255);\n"
"} \n"
"\n"
"QTabBar::tab:selected { \n"
"  background: rgba(0, 0, 0, 210);\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.widget = QtWidgets.QWidget(self.tab_2)
        self.widget.setStyleSheet("background: transparent;\n"
"color: rgb(190, 252, 255);")
        self.widget.setObjectName("widget")
        self.progressBar_2 = QtWidgets.QProgressBar(self.widget)
        self.progressBar_2.setGeometry(QtCore.QRect(200, 10, 181, 31))
        self.progressBar_2.setStyleSheet("QProgressBar{\n"
"    border: 1px solid black;\n"
"    padding: 1px;\n"
"    border-radius: 7px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk {\n"
"    \n"
"    background-color: rgb(83, 207, 151);\n"
"    border: 1px solid black;\n"
"    border-radius: 7px;\n"
"}")
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.gridLayout_11.addWidget(self.widget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setEnabled(True)
        self.frame.setStyleSheet("background: transparent;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMinimumSize(QtCore.QSize(180, 200))
        self.frame_3.setStyleSheet("background: transparent;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_10 = QtWidgets.QFrame(self.frame_3)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.frame_10)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(190, 252, 255);")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_5 = QtWidgets.QLabel(self.frame_10)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(190, 252, 255);")
        self.label_5.setScaledContents(False)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.gridLayout_3.addWidget(self.frame_10, 0, 0, 1, 2)
        self.verticalSlider = QtWidgets.QSlider(self.frame_3)
        self.verticalSlider.setStyleSheet("QSlider::handle:vertical {\n"
"    background: rgb(135, 191, 107);\n"
"}")
        self.verticalSlider.setMaximum(99)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.gridLayout_3.addWidget(self.verticalSlider, 1, 0, 1, 1)
        self.verticalSlider_2 = QtWidgets.QSlider(self.frame_3)
        self.verticalSlider_2.setStyleSheet("QSlider::handle:vertical {\n"
"    background: rgb(135, 191, 107);\n"
"}")
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.gridLayout_3.addWidget(self.verticalSlider_2, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(190, 252, 255);")
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(190, 252, 255);")
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 2, 1, 1, 1)
        self.gridLayout_6.addWidget(self.frame_3, 0, 0, 1, 1)
        self.frame_12 = QtWidgets.QFrame(self.frame)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.frame_12)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("color: rgb(190, 252, 255);")
        self.checkBox.setIconSize(QtCore.QSize(64, 64))
        self.checkBox.setCheckable(True)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.frame_12)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(190, 252, 255);")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.gridLayout_6.addWidget(self.frame_12, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.Statistic = QtWidgets.QWidget()
        self.Statistic.setStyleSheet("")
        self.Statistic.setObjectName("Statistic")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.Statistic)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frame_15 = QtWidgets.QFrame(self.Statistic)
        self.frame_15.setMinimumSize(QtCore.QSize(230, 70))
        self.frame_15.setStyleSheet("background: transparent;\n"
"color: rgb(190, 252, 255);")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_15)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_8 = QtWidgets.QLabel(self.frame_15)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(190, 252, 255);\n"
"")
        self.label_8.setObjectName("label_8")
        self.gridLayout_9.addWidget(self.label_8, 0, 0, 1, 1)
        self.frame_16 = QtWidgets.QFrame(self.frame_15)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.label_11 = QtWidgets.QLabel(self.frame_16)
        self.label_11.setGeometry(QtCore.QRect(77, 128, 16, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame_16)
        self.label_12.setGeometry(QtCore.QRect(76, -3, 16, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_10 = QtWidgets.QLabel(self.frame_16)
        self.label_10.setGeometry(QtCore.QRect(140, 62, 16, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.frame_13 = QtWidgets.QFrame(self.frame_16)
        self.frame_13.setGeometry(QtCore.QRect(20, 10, 122, 122))
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_13)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.frame_18 = QtWidgets.QFrame(self.frame_13)
        self.frame_18.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy)
        self.frame_18.setMinimumSize(QtCore.QSize(30, 30))
        self.frame_18.setStyleSheet("QFrame{\n"
"    border: 1px solid black;\n"
"    background-color: rgb(79, 79, 79);\n"
"}")
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.gridLayout_10.addWidget(self.frame_18, 0, 1, 1, 1)
        self.frame_20 = QtWidgets.QFrame(self.frame_13)
        self.frame_20.setEnabled(False)
        self.frame_20.setMinimumSize(QtCore.QSize(30, 30))
        self.frame_20.setStyleSheet("QFrame{\n"
"    border: 1px solid black;\n"
"    background-color: rgb(109, 109, 109);\n"
"}")
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.gridLayout_10.addWidget(self.frame_20, 1, 0, 1, 1)
        self.frame_19 = QtWidgets.QFrame(self.frame_13)
        self.frame_19.setEnabled(False)
        self.frame_19.setMinimumSize(QtCore.QSize(30, 30))
        self.frame_19.setStyleSheet("QFrame{\n"
"    border: 1px solid black;\n"
"    background-color: rgb(89, 89, 89);\n"
"}")
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.gridLayout_10.addWidget(self.frame_19, 1, 2, 1, 1)
        self.frame_21 = QtWidgets.QFrame(self.frame_13)
        self.frame_21.setEnabled(False)
        self.frame_21.setMinimumSize(QtCore.QSize(30, 30))
        self.frame_21.setStyleSheet("QFrame{\n"
"    border: 1px solid black;\n"
"    background-color: rgb(59, 59, 59);\n"
"}")
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.gridLayout_10.addWidget(self.frame_21, 2, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.frame_16)
        self.label_13.setGeometry(QtCore.QRect(7, 60, 16, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_9.addWidget(self.frame_16, 0, 1, 1, 1)
        self.gridLayout_8.addWidget(self.frame_15, 0, 0, 1, 1)
        self.frame_14 = QtWidgets.QFrame(self.Statistic)
        self.frame_14.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_14.setStyleSheet("background: transparent;")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_14)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background: rgba(255, 255, 255, 20);\n"
"color: rgb(190, 252, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_14)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(190, 252, 255);\n"
"background: rgba(255, 255, 255, 20);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.gridLayout_8.addWidget(self.frame_14, 1, 0, 1, 1)
        self.tabWidget.addTab(self.Statistic, "")
        self.gridLayout.addWidget(self.tabWidget, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background: transparent;\n"
"color: rgb(190, 252, 255);")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 1, 1, 1)
        self.frame_11 = QtWidgets.QFrame(self.centralwidget)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_11)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_9 = QtWidgets.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background: transparent;\n"
"color: rgb(190, 252, 255);")
        self.label_9.setObjectName("label_9")
        self.gridLayout_7.addWidget(self.label_9, 1, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background: transparent;\n"
"color: rgb(190, 252, 255);")
        self.label_14.setObjectName("label_14")
        self.gridLayout_7.addWidget(self.label_14, 2, 0, 1, 1)
        self.listWidget_2 = QtWidgets.QListWidget(self.frame_11)
        self.listWidget_2.setMinimumSize(QtCore.QSize(200, 120))
        self.listWidget_2.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setStyleSheet("background: rgba(255, 255, 255, 30);\n"
"border-color: rgb(190, 252, 255);\n"
"color: rgb(190, 252, 255);")
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout_7.addWidget(self.listWidget_2, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(197, 229, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem3, 4, 0, 2, 1)
        self.gridLayout.addWidget(self.frame_11, 0, 0, 3, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(130, 120))
        self.frame_2.setStyleSheet("background: transparent;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setMinimumSize(QtCore.QSize(230, 70))
        self.frame_4.setStyleSheet("background: transparent;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background: transparent;\n"
"color: rgb(190, 252, 255);")
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setStyleSheet("background: transparent;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setEnabled(False)
        self.frame_6.setMinimumSize(QtCore.QSize(30, 0))
        self.frame_6.setStyleSheet("QFrame{\n"
"    border: 3px;\n"
"    border-color:  rgb(50, 50, 50);\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_2.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setEnabled(False)
        self.frame_7.setMinimumSize(QtCore.QSize(30, 0))
        self.frame_7.setStyleSheet("QFrame{\n"
"        border: 3px;\n"
"    border-color:  rgb(50, 50, 50);\n"
"    background-color: rgb(79, 79, 79);\n"
"}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_2.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_5)
        self.frame_8.setEnabled(False)
        self.frame_8.setMinimumSize(QtCore.QSize(30, 0))
        self.frame_8.setStyleSheet("QFrame{\n"
"        border: 3px;\n"
"    border-color:  rgb(50, 50, 50);\n"
"    background-color: rgb(89, 89, 89);\n"
"}")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_2.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.frame_5)
        self.frame_9.setEnabled(False)
        self.frame_9.setMinimumSize(QtCore.QSize(30, 0))
        self.frame_9.setStyleSheet("QFrame{\n"
"        border: 3px;\n"
"    border-color:  rgb(50, 50, 50);\n"
"    background-color: rgb(109, 109, 109);\n"
"}")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_2.addWidget(self.frame_9)
        self.gridLayout_4.addWidget(self.frame_5, 0, 1, 1, 1)
        self.gridLayout_5.addWidget(self.frame_4, 0, 0, 1, 3)
        self.progressBar = QtWidgets.QProgressBar(self.frame_2)
        self.progressBar.setMaximumSize(QtCore.QSize(200, 16777215))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    border: 1px solid white;\n"
"    padding: 1px;\n"
"    border-radius: 7px;\n"
"    text-align: center;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"QProgressBar::chunk {\n"
"    \n"
"    background-color: rgb(130, 202, 205);\n"
"    border: 1px rgb(220, 252, 255);;\n"
"    border-radius: 7px;\n"
"}")
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 100)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_5.addWidget(self.progressBar, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("background: transparent;\n"
"color: rgb(190, 252, 255);")
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 1, 0, 1, 2)
        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setAutoFillBackground(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 667, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.actionNetScan = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.actionNetScan.setFont(font)
        self.actionNetScan.setObjectName("actionNetScan")
        self.actionCOMScan = QtWidgets.QAction(MainWindow)
        self.actionCOMScan.setObjectName("actionCOMScan")
        self.actionDirretcConnection = QtWidgets.QAction(MainWindow)
        self.actionDirretcConnection.setObjectName("actionDirretcConnection")
        self.actionReser_Settings = QtWidgets.QAction(MainWindow)
        self.actionReser_Settings.setObjectName("actionReser_Settings")
        self.toolBar.addAction(self.actionNetScan)
        self.toolBar.addAction(self.actionDirretcConnection)
        self.toolBar.addAction(self.actionReser_Settings)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Delivery"))
        self.label_6.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "Speed"))
        self.label_3.setText(_translate("MainWindow", "Step"))
        self.checkBox.setText(_translate("MainWindow", "Test Mode"))
        self.pushButton.setText(_translate("MainWindow", "Apply"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Monitor"))
        self.label_8.setText(_translate("MainWindow", "Sensors: "))
        self.label_11.setText(_translate("MainWindow", "0"))
        self.label_12.setText(_translate("MainWindow", "0"))
        self.label_10.setText(_translate("MainWindow", "0"))
        self.label_13.setText(_translate("MainWindow", "0"))
        self.pushButton_3.setText(_translate("MainWindow", "Set as white"))
        self.pushButton_2.setText(_translate("MainWindow", "Set as black"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Statistic), _translate("MainWindow", "Сalibration"))
        self.label_7.setText(_translate("MainWindow", "Current mode:"))
        self.label_9.setText(_translate("MainWindow", "Current connection: "))
        self.label_14.setText(_translate("MainWindow", "IP:"))
        self.listWidget_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>Devices</p><p><br/></p></body></html>"))
        self.listWidget_2.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Devices</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Sensors: "))
        self.label.setText(_translate("MainWindow", " Battery:"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.menu.setTitle(_translate("MainWindow", "Robot Controller"))
        self.actionNetScan.setText(_translate("MainWindow", "Avalible robots"))
        self.actionNetScan.setShortcut(_translate("MainWindow", "Shift+S"))
        self.actionCOMScan.setText(_translate("MainWindow", "COM Scan"))
        self.actionCOMScan.setShortcut(_translate("MainWindow", "Shift+C"))
        self.actionDirretcConnection.setText(_translate("MainWindow", "Dirretc connection"))
        self.actionDirretcConnection.setShortcut(_translate("MainWindow", "Shift+D"))
        self.actionReser_Settings.setText(_translate("MainWindow", "Reser Settings"))