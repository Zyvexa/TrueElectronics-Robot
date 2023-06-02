from PyQt5 import QtCore, QtWidgets
from wifi import connect, parse_server, check_avalible
from time import sleep


class WifiDataHandler(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(list)
    check_signal = QtCore.pyqtSignal(list)

    def __init__(self, myWin, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.isRun = True
        self.myWin = myWin

    def run(self):
        self.prew_conn = self.myWin.cur_connection  # предыдущее
        self.prew_host = (self.myWin.host, self.myWin.port)
        while self.isRun:
            self.conn = connect(self.myWin.host, self.myWin.port)  # подключаемся
            if self.prew_conn != self.myWin.cur_connection \
                    and (self.myWin.host, self.myWin.port) != self.prew_host:  # если подключение изменилось

                if self.conn != None:
                    self.conn.close()  # отключаемся от потока
                break
            if self.prew_conn == self.myWin.cur_connection \
                    and (self.myWin.host, self.myWin.port) == self.prew_host:  # если ничего не менялось

                out = parse_server(self.conn, self.myWin.cur_connection)  # получаем данные
                self.mysignal.emit(out)
                sleep(0.2)
        else:
            self.conn.close()
