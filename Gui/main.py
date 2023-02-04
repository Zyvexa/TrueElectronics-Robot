from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QRect
from PyQt5 import QtBluetooth as QtBt
from get_data_thread import dataHandler
from bluetooth_scanner import BLEHandler
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

        self.BLE_handl = BLEHandler(self)
        self.BLE_handl.started.connect(self.on_start_BL)
        self.BLE_handl.finished.connect(self.on_finish_BL)
        self.BLE_handl.mysignal.connect(self.add_device_on_screen, QtCore.Qt.QueuedConnection)
        self.BLE_handl.proc_signal.connect(self.scan_progress, QtCore.Qt.QueuedConnection)

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

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.MK_data.isRun = False
        self.BLE_handl.isRun = False

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
            # print(com)
            self.cur_connection = com
        self.MK_data.start()  # старт потока
        self.ui.label_9.setText(f'Current connection: {self.cur_connection}')

    def sensor_col(self, frame, value):
        color = (value * 255) // 1024
        sheet = f'border: 1px solid black;' \
                f'background-color: rgb({color}, {color}, {color});'

        frame.setStyleSheet(f'QFrame{sheet}')

    def data_from_MK(self, data_thread):  # изменение батареи и окнок датчиков от данных с МК
        if self.cur_connection.startswith('COM'):
            data = data_thread
            print(data)  # signal from thread
            if len(data) > 1:
                self.ui.progressBar.setValue(int(data[1]))

                # цвет в зависимости от показаний датчика от 0 до 1024
                self.sensor_col(self.ui.frame_6, int(data[2]))  # top sensor
                self.sensor_col(self.ui.frame_18, int(data[2]))

                self.sensor_col(self.ui.frame_7, int(data[3]))  # right sensor
                self.sensor_col(self.ui.frame_19, int(data[3]))

                self.sensor_col(self.ui.frame_8, int(data[4]))  # left sensor
                self.sensor_col(self.ui.frame_20, int(data[4]))

                self.sensor_col(self.ui.frame_9, int(data[5]))  # bottom sensor
                self.sensor_col(self.ui.frame_21, int(data[5]))

    def scan_com(self):  # сканирование комп портов и добавление в лист вью

        for com in serial_ports():
            out = f'{com["port"]}: {com["desc"]}'
            self.coms.add(out)
            self.add_device_on_screen(self.devices)

    def on_start_BL(self):
        self.ui.progressBar_2.setHidden(False)

    def on_finish_BL(self):
        self.ui.progressBar_2.setHidden(True)

    def scan_progress(self, v):
        self.ui.progressBar_2.setValue(v)

    def scan_BLE(self):  # сканирование БЛ с прогресс баром и добавлением в лист вью
        self.BLE_handl.start()


    def add_device_on_screen(self, devs):  # добавляем элементы в лист вью
        self.ui.listWidget_2.clear()
        self.devices = devs
        # for device in self.devices:
        #     self.ui.listWidget_2.addItem(f'{device[0]}: {device[1]}')
        # сокращённый цикл для добавления элементов в лист вью
        [self.ui.listWidget_2.addItem(f'(BL) {device[0]}: {device[1]}') for device in devs]
        [self.ui.listWidget_2.addItem(com) for com in self.coms]


if __name__ == "__main__":  # запуск всего
    app = QtWidgets.QApplication([])
    application = App()
    application.show()
    sys.exit(app.exec())
