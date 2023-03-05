import socket
import subprocess

def scan_network():
    s = str(subprocess.run('arp -a', shell=False, capture_output=True).stdout).split(' ')
    out = [i for i in s if i.startswith('192')]
    return out

def parse_wifi(conn):
    # 1011 это старт сообщения
    # 1011 90 1020 100 820 90
    start = b'1011'
    out = []

    for i in range(2):
        inp = conn.recv(1024)
        print(inp)
        if inp.startswith(start):
            inp = inp.decode().replace('\r\n', '')
            out = inp.split(' ')
            break
    return out  # ['1011', '90', '1020', '100', '820', '90']

HOST = "192.168.4.1"  # The server's hostname or IP address
PORT = 80  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(b"Hello, world\n\r")
    data = s.recv(1024)
#
print(f"Received {data!r}")