import socket
from settings import *
from buffer import Buffer

'''
TODO: сделать таймаут для удаления девайса по его истечению
 
[data] - это флаг для отправки данных с esp, после чего идёт имя esp и дальше данные в формате: 
[data] robot_name battery_level sensor1 sensor2 sensor3 sensor4

[check] - получение актуальных потоков данных, пример: 'robot_1 robot_2...robot_n'

[get] - получение данных с потока, пример: [get] robot_name

'''


class Server():
    def __init__(self, webServ=('localhost', 80), page_dir='/pages', listen=4):
        self.Whost, self.Wport = webServ  # айпи и порт сервера
        self.page_dir = page_dir  # папка со страницами
        self.listen = listen  # макс. количество клиентов

        self.page_dir = page_dir

        self.avalible_robots = {}  # доступные роботы с данными

        self.WebServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создание сервера на сокете
        self.WebServer.bind((self.Whost, self.Wport))
        self.WebServer.listen(self.listen)

    def log(self, text, status):  # логи в консоль
        print(warn_status[status], text)

    def run(self):  # запуск сервера
        self.log(f'Web server successful started on {self.Whost}:{self.Wport}', 'success')
        try:
            while True:
                self.Wclient_socket, self.Waddres = self.WebServer.accept()  # подключение клиента
                Wdata = self.Wclient_socket.recv(1024).decode('utf-8')  # получение данных от клиента

                self.data_handler(Wdata)  # обработка данных от клиента


        except KeyboardInterrupt:  # если прервана через Ctrl-C
            self.log('Server shutdown', 'warning')
            self.WebServer.close()  # остановка сервера

    def data_handler(self, data=str):  # обработка данных
        start_from = data.split(' ')[0]  # определение флага по типу [data], [get], [check]
        args = data.split(' ')  # аргументы
        if start_from == 'GET':  # если зашли с браузера, то подгружаем страницу
            content = self.load_page(data)

            self.Wclient_socket.send(content)
            self.Wclient_socket.shutdown(socket.SHUT_WR)

        if start_from == '[data]':  # флаг который отправляет еспшка вместе с данными
            if self.avalible_robots.get(args[1]) == None:  # если робота нету в списке доступных девайсов
                self.avalible_robots.update({args[1]: Buffer(buffer_size=3)})
                # добавляем робота в словарь,
                # и добавляем ему свой личный буфер данных
            self.avalible_robots.get(args[1]).add(args[2:])  # добавляем данные в буфер

            print(data)
        if start_from == '[check]':
            # возвращаем клиенту список доступных роботов
            response = ' '.join(self.avalible_robots)
            self.Wclient_socket.send(response.encode())
        if start_from == '[get]':
            # отправляем клиенту данные из буфера
            response = ' '.join(self.avalible_robots[args[1]].get)
            self.Wclient_socket.send(response.encode())

    def load_page(self, request):  # загрузка страницы
        responce = ''

        print(request)
        path = request.split(' ')[1]

        try:
            with open(self.page_dir + path, 'rb') as file:  # открываем страницу которую запросил пользовательв байтах
                responce = file.read()
            return HDRS.encode('utf-8') + responce  # отправяем запрос вместе с данными для браузера
        except FileNotFoundError or OSError:  # если страницу в файлах найти не смогли
            self.log('user request not existing page', 'warning')
            return (HDRS_404 + 'page not exist)').encode('utf-8')  # ошибка 404
