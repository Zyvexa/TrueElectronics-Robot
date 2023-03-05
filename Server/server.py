import socket
from settings import *
from buffer import Buffer


# TODO: добавить список с актуальными потоками, при запуске еспшка будет отправлять соответствующее сообщение
#  о включении, на сервер.
#  Еспшка будет отправлять данные на сервер которые он будет буферизировать(нужно подобрать оптимальный его размер).
#  Пользователь по запросу [check] будет получать список актуальных потоков.
#  При помощи [get] пользователь будет получать данные из буфера

class Server():
    def __init__(self, webServ=('192.168.51.227', 80), page_dir='pages', listen=4):
        self.Whost, self.Wport = webServ
        self.page_dir = page_dir
        self.listen = listen

        self.buff = Buffer(buffer_size=10)

        self.avalible_robots = {}

        self.WebServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.WebServer.bind((self.Whost, self.Wport))
        self.WebServer.listen(self.listen)

    def log(self, text, status):
        print(warn_status[status], text)

    def run(self):
        self.log(f'Web server successful started on {self.Whost}:{self.Wport}', 'success')
        try:
            while True:
                self.Wclient_socket, self.Waddres = self.WebServer.accept()
                Wdata = self.Wclient_socket.recv(1024).decode('utf-8')

                self.data_handler(Wdata)


        except KeyboardInterrupt:
            self.log('Server shutdown', 'warning')
            self.WebServer.close()

    def data_handler(self, data=str):
        start_from = data.split(' ')[0]
        args = data.split(' ')
        if start_from == 'GET':
            content = self.load_page(data)

            self.Wclient_socket.send(content)
            self.Wclient_socket.shutdown(socket.SHUT_WR)

        if start_from == '[data]':
            if self.avalible_robots.get(args[1]) == None:
                self.avalible_robots.update({args[1]: Buffer(buffer_size=3)})
            self.avalible_robots.get(args[1]).add(args[2:])

            print(data)
        if start_from == '[check]':
            response = ' '.join(self.avalible_robots)
            self.Wclient_socket.send(response.encode())
        if start_from == '[get]':
            response = ' '.join(self.avalible_robots[args[1]].get)
            self.Wclient_socket.send(response.encode())

    def load_page(self, request):
        responce = ''

        print(request)
        path = request.split(' ')[1]

        try:
            with open('pages' + path, 'rb') as file:
                responce = file.read()
            return HDRS.encode('utf-8') + responce
        except FileNotFoundError or OSError:
            self.log('user request not existing page', 'warning')
            return (HDRS_404 + 'page not exist)').encode('utf-8')

    def check_get_request(self, request):
        if len(request) > 2:
            get = request.split(' ')[1]

            return False

        else:
            return True
