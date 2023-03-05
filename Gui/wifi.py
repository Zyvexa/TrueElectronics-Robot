import socket

def check_avalible(conn):  # доступные потоки данных
    conn.send(b'[check]')
    for i in range(5):
        inp = conn.recv(1024)
        if len(inp) > 0:
            return str(inp.decode()).split(' ')


def parse_server(conn, dev):  # получение данных
    pack = f'[get] {dev}'.encode('utf-8')
    print(pack)
    conn.send(pack)
    output = str(conn.recv(1024).decode()).split(' ')
    print(output)
    return output


def connect(ip, port=80):
    HOST = ip  # The server's hostname or IP address
    PORT = port  # The port used by the server
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        return s
    except ConnectionRefusedError:
        return None

