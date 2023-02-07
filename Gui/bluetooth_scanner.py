# not using now
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtBluetooth as QtBt
from time import sleep


class BLEHandler(QtCore.QThread):
    # mysignal = QtCore.pyqtSignal(set)
    proc_signal = QtCore.pyqtSignal(int)

    def __init__(self, myWin, agent, max_scan=100001, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.isRun = True
        self.myWin = myWin
        self.devices = set()
        self.max_scan = max_scan

        self.agent = agent

    def run(self):
        for i in range(1, self.max_scan):
            if not self.isRun:
                break
            self.agent.start(QtBt.QBluetoothDeviceDiscoveryAgent.DiscoveryMethod(2))
            # sleep(0.001)
            self.proc_signal.emit(i // (self.max_scan // 100))
        self.proc_signal.emit(0)
