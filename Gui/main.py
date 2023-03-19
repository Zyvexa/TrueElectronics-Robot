from PyQt5 import QtCore, QtGui, QtWidgets
from wifi_data_thread import WifiDataHandler  # поток общения с сервером
from wifi_scan_thread import WifiScanHandler
from wifi_send_thread import WifiSendHandler

from gui import Ui_MainWindow
import sys


# TODO: сделать .cfg файл и файл с недавними настройками, например запоминание последнего подключения юзера
# TODO: сделать переключение языка

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setFixedSize(700, 467)

        self.devices = set()  # девайсы в списке

        self.host = '31.10.97.79'
        self.port = 80

        self.cur_connection = ''

        self.wifi_data = WifiDataHandler(self)
        self.wifi_data.mysignal.connect(self.data_from_MK, QtCore.Qt.QueuedConnection)

        self.wifi_scan = WifiScanHandler(self)
        self.wifi_scan.mysignal.connect(self.available_robots, QtCore.Qt.QueuedConnection)

        self.wifi_send = WifiSendHandler(self)
        self.wifi_send.mysignal.connect(self.display_status, QtCore.Qt.QueuedConnection)

        self.ui.label_7.setText('Current mode: Default')

        self.ui.actionNetScan.triggered.connect(self.check_available_thread)  # scan bluetooth devices
        self.ui.actionDirretcConnection.triggered.connect(self.show_conn_dialog)

        self.ui.listWidget_2.itemDoubleClicked.connect(self.connect_)  # подключение к айтему на который мы кликнули

        self.ui.verticalSlider.sliderMoved.connect(self.slidebar_label_1)
        self.ui.verticalSlider.sliderReleased.connect(self.slidebar_label_1)
        self.ui.verticalSlider_2.sliderMoved.connect(self.slidebar_label_2)
        self.ui.verticalSlider_2.sliderReleased.connect(self.slidebar_label_2)

        self.ui.pushButton.clicked.connect(self.apply_monitor)

        self.ui.label_14.setText(f'IP: {self.host}:{self.port}')

    def show_conn_dialog(self):  # ввод другого айпи и порта
        text, ok = QtWidgets.QInputDialog.getText(self, 'Dirrect Connection',
                                                  'Enter HOST:PORT')

        if ok:
            entered = text.split(':')
            dots = entered[0].split('.')
            if len(entered) == 2 and len(dots) == 4:  # если мы ввели хост и порт, а так же в айпи 4 цифры
                self.host, self.port = entered
                self.ui.label_14.setText(f'IP: {self.host}:{self.port}')
                # сделать очистку списка устроиств и подключения
                self.ui.listWidget_2.clear()
                self.devices.clear()
                self.cur_connection = ''
            else:
                QtWidgets.QMessageBox.critical(self, 'Incorretc format',  # если нет, то показываем пользователю пример
                                               'Example of parameters 192.168.1.1:80. Try again')
                self.show_conn_dialog()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:  # если закрываем прогу, то останавливаем поток
        self.wifi_data.isRun = False

    def slidebar_label_1(self):  # текст равен значению слайд бара
        self.ui.label_6.setText(str(self.ui.verticalSlider.value()))

    def slidebar_label_2(self):
        self.ui.label_5.setText(str(self.ui.verticalSlider_2.value()))

    def display_status(self, status):
        match status:
            case 'Ok':
                QtWidgets.QMessageBox.information(self, 'Success', 'Sent!\t\t')
            case 'Refused':
                QtWidgets.QMessageBox.critical(self, 'Connection Refused', 'Failed to connect to server')
            case 'No conn':
                QtWidgets.QMessageBox.warning(self, 'No connection', 'Connection not selected')
        if self.ui.checkBox.isChecked():
            self.ui.label_7.setText('Current mode: Test')
        else:
            self.ui.label_7.setText('Current mode: Default')

    def apply_monitor(self):  # если кнопку применения нажали, то пока что делаем визуальные изменения
        self.data_to_send = 'lol kek'
        self.wifi_send.run()

    def check_available_thread(self):
        self.wifi_scan.run()

    def available_robots(self, available):
        if available[0] != None:  # если всё ок, то проверяем актуальные потоки
            self.devices = available
            self.add_device_on_screen()  # добавляем робота в лист вью
        else:
            self.ui.label_9.setText('Connection refused')  # если не смогли подключиться

    def connect_(self, item):  # двойное нажатие на айтем в лист вью и адрес добавляется в текущее подключение
        i_text = str(item.text())
        self.cur_connection = i_text  # текущее подключение ровняется тексту айтема по которому кликнули
        self.ui.label_9.setText(f'Current Connection: {i_text}')
        self.wifi_data.start()  # запускаем поток

    def sensor_col(self, frame, value):  # изменение цвета от значения (от 0 до 1024)
        color = (value * 255) // 1024
        sheet = f'border: 1px solid black;' \
                f'background-color: rgb({color}, {color}, {color});'

        frame.setStyleSheet(f'QFrame{sheet}')

    def data_from_MK(self, data_thread):  # изменение батареи и окнок датчиков от данных с МК
        data = data_thread
        # print(data)  # signal from thread
        if len(data) > 1:
            self.ui.progressBar.setValue(int(data[0]))
            # цвет в зависимости от показаний датчика от 0 до 1024
            self.sensor_col(self.ui.frame_6, int(data[1]))  # top sensor
            self.sensor_col(self.ui.frame_18, int(data[1]))
            self.sensor_col(self.ui.frame_7, int(data[2]))  # right sensor
            self.sensor_col(self.ui.frame_19, int(data[2]))
            self.sensor_col(self.ui.frame_8, int(data[3]))  # left sensor
            self.sensor_col(self.ui.frame_20, int(data[3]))
            self.sensor_col(self.ui.frame_9, int(data[4]))  # bottom sensor
            self.sensor_col(self.ui.frame_21, int(data[4]))

    def add_device_on_screen(self):  # добавляем элементы в лист вью
        self.ui.listWidget_2.clear()
        # сокращённый цикл для добавления элементов в лист вью
        [self.ui.listWidget_2.addItem(f'{device}') for device in self.devices]


if __name__ == "__main__":  # запуск всего
    app = QtWidgets.QApplication([])
    application = App()
    application.show()
    sys.exit(app.exec())
