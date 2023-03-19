from PyQt5 import QtCore
from wifi import connect, check_avalible


class WifiScanHandler(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(list)

    def __init__(self, myWin, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.myWin = myWin

    def run(self):
        print(1)
        conn = connect(self.myWin.host, self.myWin.port)
        print(2)
        if conn != None:  # TODO: сделать проверку на то что out != None
            out = check_avalible(conn)
            if out != None:
                print('1', out)
                self.mysignal.emit(out)
                conn.close()
            else:
                self.mysignal.emit([None])
        else:
            self.mysignal.emit([None])



