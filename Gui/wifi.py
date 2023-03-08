import socket


def check_avalible(conn):  # доступные потоки данных
    if conn != None:
        conn.send(b'[check]')
        inp = conn.recv(1024)
        if len(inp) > 1:
            return str(inp.decode()).split(' ')
    else:
        return None


def parse_server(conn, dev):  # получение данных
    pack = f'[get] {dev}'.encode('utf-8')
    print(pack)
    conn.send(pack)
    output = str(conn.recv(1024).decode()).split(' ')
    print(output)
    return output


def connect(ip, port=80):
    HOST = ip  # The server's hostname or IP address
    PORT = int(port)  # The port used by the server
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        return s
    except ConnectionRefusedError:
        return None


if __name__ == '__main__':
    from time import sleep

    while True:
        conn = connect('31.10.97.79')
        conn.send(b'[data] me 10 321 32 44 55')
        # conn.send(b'[check]')
        # print(conn.recv(1024))
        sleep(0.5)
