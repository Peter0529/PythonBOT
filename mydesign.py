# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1063, 752)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(820, 40, 221, 101))
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 20, 191, 72))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.inputCampNote = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.inputCampNote.setFont(font)
        self.inputCampNote.setObjectName("inputCampNote")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.inputCampNote)
        self.inputProxyNote = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.inputProxyNote.setFont(font)
        self.inputProxyNote.setObjectName("inputProxyNote")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.inputProxyNote)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(50, 50, 769, 170))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setHorizontalSpacing(5)
        self.formLayout_2.setVerticalSpacing(30)
        self.formLayout_2.setObjectName("formLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(30)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.inputMaxThread = QtWidgets.QSpinBox(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.inputMaxThread.setFont(font)
        self.inputMaxThread.setMaximum(999)
        self.inputMaxThread.setObjectName("inputMaxThread")
        self.gridLayout.addWidget(self.inputMaxThread, 1, 2, 1, 1)
        self.inputTimeOut = QtWidgets.QSpinBox(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.inputTimeOut.setFont(font)
        self.inputTimeOut.setMaximum(999)
        self.inputTimeOut.setObjectName("inputTimeOut")
        self.gridLayout.addWidget(self.inputTimeOut, 1, 6, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 1, 9, 1, 1)
        self.inputMaxMixed = QtWidgets.QSpinBox(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.inputMaxMixed.setFont(font) 
        self.inputMaxMixed.setMaximum(999)
        self.inputMaxMixed.setObjectName("inputMaxMixed")
        self.gridLayout.addWidget(self.inputMaxMixed, 1, 10, 1, 1)
        self.inputMaxPlays = QtWidgets.QSpinBox(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.inputMaxPlays.setFont(font)
        self.inputMaxPlays.setMaximum(999)
        self.inputMaxPlays.setObjectName("inputMaxPlays")
        self.gridLayout.addWidget(self.inputMaxPlays, 1, 8, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 7, 1, 1)
        self.inputErrorLimit = QtWidgets.QSpinBox(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.inputErrorLimit.setFont(font)
        self.inputErrorLimit.setMaximum(999)
        self.inputErrorLimit.setObjectName("inputErrorLimit")
        self.gridLayout.addWidget(self.inputErrorLimit, 1, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 5, 1, 1)
        self.chkShowStatusBar = QtWidgets.QCheckBox(self.formLayoutWidget_2)
        self.chkShowStatusBar.setObjectName("chkShowStatusBar")
        self.gridLayout.addWidget(self.chkShowStatusBar, 1, 11, 1, 1)
        self.inputChromePath = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.inputChromePath.setFont(font)
        self.inputChromePath.setTabletTracking(False)
        self.inputChromePath.setReadOnly(True)
        self.inputChromePath.setObjectName("inputChromePath")
        self.gridLayout.addWidget(self.inputChromePath, 0, 2, 1, 10)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.SpanningRole, self.gridLayout)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 150, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.outLogs = QtWidgets.QTextEdit(self.centralwidget)
        self.outLogs.setGeometry(QtCore.QRect(50, 200, 751, 461))
        self.outLogs.setReadOnly(True)
        self.outLogs.setObjectName("outLogs")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(830, 210, 211, 441))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 20, 0, 0)
        self.formLayout_3.setHorizontalSpacing(6)
        self.formLayout_3.setVerticalSpacing(40)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.dLabel = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.dLabel.setObjectName("dLabel")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.dLabel)
        self.outPlayedCount = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.outPlayedCount.setFont(font)
        self.outPlayedCount.setReadOnly(True)
        self.outPlayedCount.setObjectName("outPlayedCount")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.outPlayedCount)
        self.outCurrentThreadCount = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.outCurrentThreadCount.setFont(font)
        self.outCurrentThreadCount.setReadOnly(True)
        self.outCurrentThreadCount.setObjectName("outCurrentThreadCount")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.outCurrentThreadCount)
        self.followedCountLabel = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.followedCountLabel.setObjectName("followedCountLabel")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.followedCountLabel)
        self.outFollowedCount = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.outFollowedCount.setFont(font)
        self.outFollowedCount.setReadOnly(True)
        self.outFollowedCount.setObjectName("outFollowedCount")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.outFollowedCount)
        self.highlightedCountLabel = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.highlightedCountLabel.setObjectName("highlightedCountLabel")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.highlightedCountLabel)
        self.outHighlightedCount = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.outHighlightedCount.setFont(font)
        self.outHighlightedCount.setReadOnly(True)
        self.outHighlightedCount.setObjectName("outHighlightedCount")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.outHighlightedCount)
        self.reupedCountLabel = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.reupedCountLabel.setObjectName("reupedCountLabel")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.reupedCountLabel)
        self.outReupedCount = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.outReupedCount.setFont(font)
        self.outReupedCount.setReadOnly(True)
        self.outReupedCount.setObjectName("outReupedCount")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.outReupedCount)
        self.favoritedCountLabel = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.favoritedCountLabel.setObjectName("favoritedCountLabel")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.favoritedCountLabel)
        self.outFavoritedCount = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.outFavoritedCount.setFont(font)
        self.outFavoritedCount.setReadOnly(True)
        self.outFavoritedCount.setObjectName("outFavoritedCount")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.outFavoritedCount)
        self.errorCountLabel = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.errorCountLabel.setObjectName("errorCountLabel")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.errorCountLabel)
        self.outErrorCount = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.outErrorCount.setFont(font)
        self.outErrorCount.setReadOnly(True)
        self.outErrorCount.setClearButtonEnabled(False)
        self.outErrorCount.setObjectName("outErrorCount")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.outErrorCount)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(820, 190, 231, 471))
        self.groupBox_2.setObjectName("groupBox_2")
        self.btStart = QtWidgets.QPushButton(self.centralwidget)
        self.btStart.setGeometry(QtCore.QRect(310, 680, 75, 23))
        self.btStart.setCheckable(False)
        self.btStart.setChecked(False)
        self.btStart.setAutoRepeat(False)
        self.btStart.setAutoDefault(False)
        self.btStart.setDefault(False)
        self.btStart.setFlat(False)
        self.btStart.setObjectName("btStart")
        self.btStop = QtWidgets.QPushButton(self.centralwidget)
        self.btStop.setGeometry(QtCore.QRect(460, 680, 75, 23))
        self.btStop.setObjectName("btStop")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 140, 1031, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.label.raise_()
        self.formLayoutWidget_2.raise_()
        self.label_8.raise_()
        self.outLogs.raise_()
        self.formLayoutWidget_3.raise_()
        self.btStart.raise_()
        self.btStop.raise_()
        self.line.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1063, 21))
        self.menubar.setObjectName("menubar")
        self.menuAction = QtWidgets.QMenu(self.menubar)
        self.menuAction.setObjectName("menuAction")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuStart = QtWidgets.QAction(MainWindow)
        self.menuStart.setObjectName("menuStart")
        self.menuStop = QtWidgets.QAction(MainWindow)
        self.menuStop.setObjectName("menuStop")
        self.menuEXIT = QtWidgets.QAction(MainWindow)
        self.menuEXIT.setObjectName("menuEXIT")
        self.menuSaveSettings = QtWidgets.QAction(MainWindow)
        self.menuSaveSettings.setObjectName("menuSaveSettings")
        self.menuAction.addSeparator()
        self.menuAction.addAction(self.menuStart)
        self.menuAction.addAction(self.menuStop)
        self.menuAction.addSeparator()
        self.menuAction.addAction(self.menuSaveSettings)
        self.menuAction.addSeparator()
        self.menuAction.addAction(self.menuEXIT)
        self.menubar.addAction(self.menuAction.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.inputProxyNote, self.inputChromePath)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Audiomack BOT"))
        self.label.setText(_translate("MainWindow", "Settings:"))
        self.groupBox.setTitle(_translate("MainWindow", "NOTE"))
        self.label_5.setText(_translate("MainWindow", "Proxy NOTE"))
        self.label_6.setText(_translate("MainWindow", "Campaign NOTE"))
        self.label_3.setText(_translate("MainWindow", "Max Active Thread"))
        self.label_11.setText(_translate("MainWindow", "Max Mixed "))
        self.label_4.setText(_translate("MainWindow", "Error Limit"))
        self.label_10.setText(_translate("MainWindow", "Max Plays"))
        self.label_2.setText(_translate("MainWindow", "Portable Chrome Path"))
        self.label_7.setText(_translate("MainWindow", "TimeOut"))
        self.chkShowStatusBar.setText(_translate("MainWindow", "Show StatusBar"))
        self.label_8.setText(_translate("MainWindow", "Logs:"))
        self.outLogs.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "Current Thread Count"))
        self.dLabel.setText(_translate("MainWindow", "Played Count"))
        self.followedCountLabel.setText(_translate("MainWindow", "Followed Count"))
        self.highlightedCountLabel.setText(_translate("MainWindow", "Highlighted Count"))
        self.reupedCountLabel.setText(_translate("MainWindow", "Reuped Count"))
        self.favoritedCountLabel.setText(_translate("MainWindow", "Favorited Count"))
        self.errorCountLabel.setText(_translate("MainWindow", "Error Count"))
        self.groupBox_2.setTitle(_translate("MainWindow", "COUNT"))
        self.btStart.setText(_translate("MainWindow", "Start"))
        self.btStop.setText(_translate("MainWindow", "Stop"))
        self.menuAction.setTitle(_translate("MainWindow", "Action"))
        self.menuStart.setText(_translate("MainWindow", "Start"))
        self.menuStop.setText(_translate("MainWindow", "Stop"))
        self.menuEXIT.setText(_translate("MainWindow", "EXIT"))
        self.menuSaveSettings.setText(_translate("MainWindow", "Save Current Settings"))
