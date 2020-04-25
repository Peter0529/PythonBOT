# -*- coding: utf-8 -*-

# BOT Main Window


from PyQt5 import QtWidgets, QtGui

from mydesign import Ui_MainWindow

from settings.main_settings import *
from settings.bot_settings import *
from mainthread import MainThread

import sys

class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
    
        super(mywindow, self).__init__()

        # Init Main GUI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Load BOT Settings
        self.loadSettings()

        # Set Start Button OnClick Event Function
        self.ui.btStart.clicked.connect(self.onStart)

        # Set Stop Button OnClick Event Function
        self.ui.btStop.clicked.connect(self.onStop)

        # Set Start Menu OnClick Event Function
        self.ui.menuStart.triggered.connect(self.onStart)

        # Set Stop Menu OnClick Event Function
        self.ui.menuStop.triggered.connect(self.onStop)

        # Set Save Settings Menu OnClick Event Function
        self.ui.menuSaveSettings.triggered.connect(self.saveSettings)

        # Set EXIT Menu OnClick Event Function
        self.ui.menuEXIT.triggered.connect(self.onEXIT)
    
    # Load BOT Settings(from bot_settings.py) and Set Values
    def loadSettings(self):
        
        self.ui.inputChromePath.setText(PORTABLE_CHROME_PATH)
        self.ui.inputMaxThread.setValue(MAX_ACTIVE_THREAD)
        self.ui.inputErrorLimit.setValue(ERROR_LIMIT_PER_THREAD)
        self.ui.inputTimeOut.setValue(TIMEOUT)
        self.ui.inputCampNote.setText(CAMPAIGN_NOTE)
        self.ui.inputProxyNote.setText(PROXY_NOTE)
        self.ui.inputMaxMixed.setValue(MAX_MIXED)
        self.ui.inputMaxPlays.setValue(MAX_PLAYS)

    # Save Current Settings(to bot_settings.py)
    def saveSettings(self):

        self.getCurrentSettings()
        with open("settings/bot_settings.py","w+") as f:
            f.writelines(["\nMAX_ACTIVE_THREAD=" + str(MAX_ACTIVE_THREAD)
                        ,"\nERROR_LIMIT_PER_THREAD=" + str(ERROR_LIMIT_PER_THREAD)
                        ,"\nTIMEOUT=" + str(TIMEOUT)
                        ,"\nMAX_PLAYS=" + str(MAX_PLAYS)
                        ,"\nMAX_MIXED=" + str(MAX_MIXED)
                        ,"\nPROXY_NOTE=\"" + PROXY_NOTE + "\""
                        ,"\nCAMPAIGN_NOTE=\"" + CAMPAIGN_NOTE +"\""])

    # Get Values of Current Settings
    def getCurrentSettings(self):
        global MAX_ACTIVE_THREAD,ERROR_LIMIT_PER_THREAD,TIMEOUT,PROXY_NOTE,CAMPAIGN_NOTE,MAX_MIXED,MAX_PLAYS

        MAX_ACTIVE_THREAD       = self.ui.inputMaxThread.value()
        ERROR_LIMIT_PER_THREAD  = self.ui.inputErrorLimit.value()
        TIMEOUT                 = self.ui.inputTimeOut.value()
        PROXY_NOTE              = self.ui.inputProxyNote.text()
        CAMPAIGN_NOTE           = self.ui.inputCampNote.text()
        MAX_MIXED               = self.ui.inputMaxMixed.value()
        MAX_PLAYS               = self.ui.inputMaxPlays.value()

    # Start Bot
    def onStart(self):
        self.getCurrentSettings()

        settings = {
            'MAX_ACTIVE_THREAD'             : MAX_ACTIVE_THREAD,
            'ERROR_LIMIT_PER_THREAD'        : ERROR_LIMIT_PER_THREAD,
            'TIMEOUT'                       : TIMEOUT,
            'PROXY_NOTE'                    : PROXY_NOTE,
            'CAMPAIGN_NOTE'                 : CAMPAIGN_NOTE,
            'MAX_MIXED'                     : MAX_MIXED,
            'MAX_PLAYS'                     : MAX_PLAYS
        }

        self.mainthread = MainThread(settings)
        self.mainthread.start()
    
    # Stop Bot
    def onStop(self):
        self.mainthread.stop()
    
    # Exit Application
    def onEXIT(self):
        sys.exit(1)


app = QtWidgets.QApplication([])

application = mywindow()

application.show()

sys.exit(app.exec())