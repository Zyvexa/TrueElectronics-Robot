from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtBluetooth as QtBt
from time import sleep

class BLEHandler(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(set)
    proc_signal = QtCore.pyqtSignal(int)

    def __init__(self, myWin, max_scan=101, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.isRun = True
        self.myWin = myWin
        self.devices = set()
        self.max_scan = max_scan

    def run(self):
        for i in range(1, self.max_scan):
            self.scan()
            self.proc_signal.emit(i // (self.max_scan // 100))
            # sleep(0.01)
        self.mysignal.emit(self.devices)

    def display_status(self):  # добавление БЛ устроиств в список с ними
        dev = self.agent.discoveredDevices()
        if len(dev) > 0:
            self.devices.add((dev[0].name(), dev[0].address().toString()))

    def scan(self):
        self.agent = QtBt.QBluetoothDeviceDiscoveryAgent(self)
        self.agent.deviceDiscovered.connect(self.display_status)
        self.agent.setLowEnergyDiscoveryTimeout(1000)

        self.agent.start(QtBt.QBluetoothDeviceDiscoveryAgent.DiscoveryMethod(2))
