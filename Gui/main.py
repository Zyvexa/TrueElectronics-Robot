from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QRect
from PyQt5 import QtBluetooth as QtBt
from get_data_thread import dataHandler
from gui import Ui_MainWindow
from _serial_ports import *
import sys


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.devices = set()
        self.coms = set()

        self.cur_connection = None

        self.MK_data = dataHandler(self)
        self.MK_data.mysignal.connect(self.data_from_MK, QtCore.Qt.QueuedConnection)

        self.ui.progressBar_2.setHidden(True)
        self.ui.label_7.setText('Current mode: Default')


        self.ui.actionBLEScan.triggered.connect(self.scan_BLE)  # scan bluetooth devices
        self.ui.actionCOMScan.triggered.connect(self.scan_com)

        self.ui.listWidget_2.itemDoubleClicked.connect(self.connect_)  # подключение к айтему на который мы кликнули

        self.ui.verticalSlider.sliderMoved.connect(self.slidebar_label_1)
        self.ui.verticalSlider.sliderReleased.connect(self.slidebar_label_1)
        self.ui.verticalSlider_2.sliderMoved.connect(self.slidebar_label_2)
        self.ui.verticalSlider_2.sliderReleased.connect(self.slidebar_label_2)

        self.ui.pushButton.clicked.connect(self.apply_monitor)

    def slidebar_label_1(self):
        self.ui.label_6.setText(str(self.ui.verticalSlider.value()))

    def slidebar_label_2(self):
        self.ui.label_5.setText(str(self.ui.verticalSlider_2.value()))

    def apply_monitor(self):
        if self.ui.checkBox.isChecked():
            self.ui.label_7.setText('Current mode: Test')
        else:
            self.ui.label_7.setText('Current mode: Default')

        # TODO: do something with sliders

    def connect_(self, item):  # двойное нажатие на айтем в лист вью и адрес добавляется в текущее подключение
        i_text = str(item.text())
        if i_text.startswith('(BL)'):
            mac = i_text[-17:-1]
            self.cur_connection = mac
        if i_text.startswith('COM'):
            com = i_text.split(':')[0]
            print(com)
            self.cur_connection = com
        self.MK_data.start()  # старт потока
        self.ui.label_9.setText(f'Current connection: {self.cur_connection}')

    def data_from_MK(self, data_thread):  # изменение батареи и окнок датчиков от данных с МК
        if self.cur_connection.startswith('COM'):
            data = data_thread
            print(data)# parse_serial(self.cur_connection)  # signal of thread
            if len(data) > 1:
                self.ui.progressBar.setValue(int(data[1]))

                col_6 = self.convert_col_sensors(int(data[2]))
                colf_6 = f'border: 1px solid black;' \
                         f'background-color: rgb({col_6}, {col_6}, {col_6});'

                self.ui.frame_6.setStyleSheet(f'QFrame{colf_6}')

                col_7 = self.convert_col_sensors(int(data[3]))
                colf_7 = f'border: 1px solid black;' \
                         f'background-color: rgb({col_7}, {col_7}, {col_7});'

                self.ui.frame_7.setStyleSheet(f'QFrame{colf_7}')

                col_8 = self.convert_col_sensors(int(data[4]))
                colf_8 = f'border: 1px solid black;' \
                         f'background-color: rgb({col_8}, {col_8}, {col_8});'

                self.ui.frame_8.setStyleSheet(f'QFrame{colf_8}')

                col_9 = self.convert_col_sensors(int(data[5]))
                colf_9 = f'border: 1px solid black;' \
                         f'background-color: rgb({col_9}, {col_9}, {col_9});'

                self.ui.frame_9.setStyleSheet(f'QFrame{colf_9}')

    def convert_col_sensors(self, value):  # конвертация диапазона датчиков диапазон rgb
        out = (value * 255) // 1024
        # print(out)
        return out

    def scan_com(self):  # сканирование комп портов и добавление в лист вью
        for com in serial_ports():
            out = f'{com["port"]}: {com["desc"]}'
            self.coms.add(out)
            self.ui.listWidget_2.addItem(out)

    def scan_BLE(self):  # сканирование БЛ с прогресс баром и добавлением в лист вью
        self.ui.progressBar_2.setHidden(False)
        for i in range(101):
            self.ui.progressBar_2.setValue(i)
            self.scan_for_devices()
        self.ui.progressBar_2.setHidden(True)

    def add_device_on_screen(self):  # добавляем элементы в лист вью
        self.ui.listWidget_2.clear()
        # for device in self.devices:
        #     self.ui.listWidget_2.addItem(f'{device[0]}: {device[1]}')
        # сокращённый цикл для добавления элементов в лист вью
        [self.ui.listWidget_2.addItem(f'(BL) {device[0]}: {device[1]}') for device in self.devices]
        [self.ui.listWidget_2.addItem(com) for com in self.coms]

    def display_status(self):  # добавление БЛ устроиств в список с ними
        dev = self.agent.discoveredDevices()
        if len(dev) > 0:
            # print(dev[0].name(), dev[0].address().toString())
            self.devices.add((dev[0].name(), dev[0].address().toString()))
            self.add_device_on_screen()

    def foo(self, *args, **kwargs):  # TODO: что это???
        ...

    def scan_for_devices(self):  # сканирование БЛ диапазона

        self.agent = QtBt.QBluetoothDeviceDiscoveryAgent(self)
        self.agent.deviceDiscovered.connect(self.display_status)
        self.agent.error.connect(self.foo)
        self.agent.finished.connect(self.foo)
        self.agent.canceled.connect(self.foo)
        self.agent.setLowEnergyDiscoveryTimeout(1000)

        self.agent.start(QtBt.QBluetoothDeviceDiscoveryAgent.DiscoveryMethod(2))


if __name__ == "__main__":  # запуск всего
    app = QtWidgets.QApplication([])
    application = App()
    application.show()
    sys.exit(app.exec())
