import socket
from settings import *
from buffer import Buffer
from time import time

# TODO: сделать таймаут для удаления девайса по его истечению
# TODO: сделать для робота команду [recive] <my_robot_name>

''' 
[data] - это флаг для отправки данных с esp, после чего идёт имя esp и дальше данные в формате: 
[data] robot_name battery_level sensor1 sensor2 sensor3 sensor4

[check] - получение актуальных потоков данных, пример: 'robot_1 robot_2...robot_n'

[get] - получение данных с потока, пример: [get] robot_name

[send] <target_robot_name> <any data>

[receive] <my_robot_name>

'''


class Server():
    def __init__(self, webServ=('localhost', 80), page_dir='pages', listen=4):
        self.Whost, self.Wport = webServ  # айпи и порт сервера
        self.page_dir = page_dir  # папка со страницами
        self.listen = listen  # макс. количество клиентов

        self.page_dir = page_dir

        self.available_robots = {}  # доступные роботы с данными

        self.WebServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создание сервера на сокете
        self.WebServer.bind((self.Whost, self.Wport))
        self.WebServer.listen(self.listen)

    def run(self):  # запуск сервера
        log(f'Web server successful started on {self.Whost}:{self.Wport}', 'success')
        try:
            while True:
                self.Wclient_socket, self.Waddres = self.WebServer.accept()  # подключение клиента
                Wdata = self.Wclient_socket.recv(512).decode('utf-8')  # получение данных от клиента

                self.data_handler(Wdata)  # обработка данных от клиента


        except KeyboardInterrupt:  # если прервана через Ctrl-C
            log('Server shutdown', 'warning')
            self.Wclient_socket.close()
            self.WebServer.close()  # остановка сервера

    def data_handler(self, data=str):  # обработка данных
        start_from = data.split(' ')[0]  # определение флага по типу [data], [get], [check]
        args = data.split(' ')  # аргументы
        if start_from not in cmds:
            log(data, 'unknown')
        elif start_from == 'GET':  # если зашли с браузера, то подгружаем страницу
            content = self.load_page(data)

            self.Wclient_socket.send(content)
            self.Wclient_socket.shutdown(socket.SHUT_WR)

        elif start_from == '[data]':  # флаг который отправляет еспшка вместе с данными
            if self.available_robots.get(args[1]) == None:  # если робота нету в списке доступных девайсов
                # TODO: добавить формат данных в словаре по типу:
                # {<robot_name>: [buffer_for_client, buffer_for_robot, timer]}
                # таймер бдует нужен для удалению робота по истечению тайм аута
                self.available_robots.update({args[1]: [Buffer(buffer_size=3), Buffer(buffer_size=3), 0]})
                # добавляем робота в словарь,
                # и добавляем ему свой личный буфер данных
            self.available_robots.get(args[1])[0].add(args[2:])  # добавляем данные в буфер
        elif start_from == '[send]':
            self.available_robots.get(args[1])[1].add(args[2:])  # добавляем данные в буфер
            print(f'>>>>{args[2:]}')

        print(data)
        try:
            if start_from == '[check]':
                # возвращаем клиенту список доступных роботов
                if len(self.available_robots) > 0:
                    response = ' '.join(self.available_robots)
                    self.Wclient_socket.send(response.encode())
                else:
                    self.Wclient_socket.send(b' ')
                    log('no robots available for user', 'info')
            elif start_from == '[get]':
                # отправляем клиенту данные из буфера
                response = ' '.join(self.available_robots[args[1]][0].get)
                self.Wclient_socket.send(response.encode())
            elif start_from == '[receive]':
                response = ' '.join(self.available_robots[args[1]][1].get) + '\n'
                # response = 'abs1234\n'
                print(response)
                self.Wclient_socket.send(response.encode())

        except ConnectionResetError:
            log("Connection reset ¯\_(ツ)_/¯", 'warning')

    def load_page(self, request):  # загрузка страницы
        responce = ''

        print(request)
        path = request.split(' ')[1]
        print(path)

        try:
            with open(self.page_dir + path, 'rb') as file:  # открываем страницу которую запросил пользовательв байтах
                responce = file.read()
            return HDRS.encode('utf-8') + responce  # отправяем запрос вместе с данными для браузера
        except FileNotFoundError:  # если страницу в файлах найти не смогли
            log('user request not existing page', 'info')
            return (HDRS_404 + 'page not exist)').encode('utf-8')  # ошибка 404
