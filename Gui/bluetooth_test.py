# not using now
import signal
import sys

from PyQt5 import QtBluetooth as QtBt
from PyQt5 import QtCore


class Application(QtCore.QCoreApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.scan_for_devices()
        self.exec()

    def display_status(self):
        dev = self.agent.discoveredDevices()[0]
        print(dev.name(), dev.address().toString(), sep=': ')

    def foo(self, *args, **kwargs):
        pass

    def scan_for_devices(self):
        self.agent = QtBt.QBluetoothDeviceDiscoveryAgent(self) # 00:21:13:04:8B:32
        self.agent.deviceDiscovered.connect(self.display_status)
        self.agent.finished.connect(self.foo)
        self.agent.error.connect(self.foo)
        self.agent.setLowEnergyDiscoveryTimeout(1000)

        timer = QtCore.QTimer(self.agent)
        timer.start(500)
        # timer.timeout.connect(self.display_status)

        self.agent.start()


if __name__ == '__main__':
    import sys

    app = Application(sys.argv)
