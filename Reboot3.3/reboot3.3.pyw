import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QSystemTrayIcon, QStyle, QMenu, QAction, qApp
from ui import Ui_MainWindow
import time
import os
import keyboard
import configparser

config = configparser.ConfigParser()
config.read("settings.ini")


class Reboot(QtWidgets.QMainWindow):

    def __init__(self):
        super(Reboot, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.style().standardIcon(QStyle.SP_MessageBoxWarning))
        show_action = QAction("Показать", self)
        quit_action = QAction("Выход", self)
        hide_action = QAction("Скрыть", self)
        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        quit_action.triggered.connect(qApp.quit)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

    def init_UI(self):
        self.setWindowTitle("Reboot 7 sec")
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_MessageBoxWarning))
        self.ui.pushButton.clicked.connect(self.bp)
        self.ui.pushButton.clicked.connect(self.hide)

    def bp(self):
        pass_user = config.get("Settings", "pass_user")
        key_1 = config.get("Settings", "Key1")
        key_2 = config.get("Settings", "Key2")
        self.ui.lineEdit_2.setText('ON')
        keyboard.add_hotkey("F12", lambda: self.lan())
        keyboard.add_hotkey("F11", lambda: (keyboard.write(pass_user), keyboard.send('enter')))
        keyboard.add_hotkey(key_1, lambda: (keyboard.send('alt+F4'), time.sleep(0.2), keyboard.send('escape')))
        keyboard.add_hotkey(key_2, lambda: (keyboard.write("/fb")))

    def lan(self):
        os.system('ipconfig/release *Ethernet*')
        time.sleep(7)
        os.system('ipconfig /renew  *Ethernet* ')


app = QtWidgets.QApplication([])
application = Reboot()
application.show()
sys.exit(app.exec_())
