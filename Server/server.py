import socket
from settings import *


class Server():
    def __init__(self, webServ=('localhost', 80), page_dir='pages', listen=4):
        self.Whost, self.Wport = webServ
        self.page_dir = page_dir
        self.listen = listen

        self.WebServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.WebServer.bind((self.Whost, self.Wport))
        self.WebServer.listen(self.listen)

    def log(self, text, status):
        print(warn_status[status], text)

    def run(self):
        self.log(f'Web server successful started on {self.Whost}:{self.Wport}', 'success')
        try:
            while True:
                Wclient_socket, Waddres = self.WebServer.accept()
                Wdata = Wclient_socket.recv(1024).decode('utf-8')
                print('/>', Wdata)
                if Wdata.split(' ')[0] == '[data]':
                    print('ok')
                    # do something with the data
                    continue
                else:
                    content = self.load_page(Wdata)

                    Wclient_socket.send(content)
                    Wclient_socket.shutdown(socket.SHUT_WR)
        except KeyboardInterrupt:
            self.log('Server shutdown', 'warning')
            self.WebServer.close()

    def data_handler(self, data):
        pass

    def load_page(self, request):
        responce = ''

        path = request.split(' ')[1]

        try:
            with open('pages' + path, 'rb') as file:
                responce = file.read()
            return HDRS.encode('utf-8') + responce
        except PermissionError or FileNotFoundError:
            self.log('user request not existing page', 'warning')
            return (HDRS_404 + 'page not exist)').encode('utf-8')

    def check_get_request(self, request):
        if len(request) > 2:
            get = request.split(' ')[1]

            return False

        else:
            return True
