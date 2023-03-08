import sys
from wifi import connect
from random import randint
from time import sleep

if __name__ == '__main__':
    ip = sys.argv[1]
    name = sys.argv[2]
    battery = 100
    delay = float(sys.argv[3])
    while True:
        if battery <= 0: battery = 100

        conn = connect(ip)
        message = f'[data] {name} {battery} {randint(0, 1024)} {randint(0, 1024)} {randint(0, 1024)} {randint(0, 1024)}'
        conn.send(message.encode())
        battery -= 1
        print(ip, name, battery)
        sleep(delay)
