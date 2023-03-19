from PyQt5 import QtCore
from wifi import connect, check_avalible


class WifiSendHandler(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    def __init__(self, myWin, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.myWin = myWin

    def run(self):
        if self.myWin.cur_connection != '':
            self.conn = connect(self.myWin.host, self.myWin.port)
            if self.conn != None:
                pack = f'[send] {self.myWin.cur_connection} {self.myWin.data_to_send}'
                print([pack])
                self.conn.send(pack.encode())

                self.mysignal.emit('Ok')
            else:
                self.mysignal.emit('Refused')
        else:
            self.mysignal.emit('No conn')
