from server import Server

if __name__ == '__main__':
    import os
    os.system('clear')
    serv = Server(webServ=('0.0.0.0', 80))
    serv.run()