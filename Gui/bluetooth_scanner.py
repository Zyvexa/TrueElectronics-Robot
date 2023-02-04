from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtBluetooth as QtBt
from time import sleep

class BLEHandler(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(set)
    proc_signal = QtCore.pyqtSignal(int)

    def __init__(self, myWin, max_scan=100001, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.isRun = True
        self.myWin = myWin
        self.devices = set()
        self.max_scan = max_scan

        self.agent = QtBt.QBluetoothDeviceDiscoveryAgent(self)
        self.agent.deviceDiscovered.connect(self.display_status)
        self.agent.setLowEnergyDiscoveryTimeout(1000)

    def run(self):
        for i in range(1, self.max_scan):
            if not self.isRun:
                break
            self.scan()
            # sleep(0.001)
            self.proc_signal.emit(i // (self.max_scan // 100))
        self.mysignal.emit(self.devices)
        self.proc_signal.emit(0)

    def display_status(self):  # добавление БЛ устроиств в список с ними
        dev = self.agent.discoveredDevices()
        if len(dev) > 0:
            self.devices.add((dev[0].name(), dev[0].address().toString()))

    def scan(self):
        self.agent.start(QtBt.QBluetoothDeviceDiscoveryAgent.DiscoveryMethod(2))
