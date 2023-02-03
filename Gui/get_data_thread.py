from PyQt5 import QtCore, QtWidgets
from _serial_ports import parse_serial, open_serial, close_serial
from time import sleep


class dataHandler(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(list)

    def __init__(self, myWin, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.isRun = True
        self.myWin = myWin

    def run(self):
        self.prew_con = self.myWin.cur_connection
        self.ser = open_serial(self.myWin.cur_connection)
        while self.isRun:
            if self.prew_con != self.myWin.cur_connection:
                close_serial(self.ser)
                break
            if self.prew_con == self.myWin.cur_connection:
                out = parse_serial(self.ser)
                print(out)
                self.mysignal.emit(out)
                sleep(0.2)
