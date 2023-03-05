from server import Server

if __name__ == '__main__':
    serv = Server(webServ=('31.10.97.79', 80))
    serv.run()