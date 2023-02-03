import serial
import serial.tools.list_ports
import sys


# получение списка портов
def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            Операционная система не определена
        :returns:
            Список с доступными COM портами на компьютере
    """
    result = []
    ports = serial.tools.list_ports.comports()

    for port, desc, hwid in sorted(ports):
        result.append({'port': port, 'desc': desc, 'hwid': hwid})

    return result


# открытие порта
def open_serial(com, a1=9600):
    ser = serial.Serial(com, int(a1))
    return ser


# Закрытие порта
def close_serial(com):
    com.close()


def parse_serial(com, bod=9600):
    # 1011 90 1020 100 820 90
    ser = serial.Serial(com, int(bod), timeout=1)
    start = b'1011'
    out = []

    for i in range(2):
        inp = ser.readline()
        if inp.startswith(start):
            inp = inp.decode().replace('\r\n', '')
            out = inp.split(' ')
            break
    return out  # ['1011', '90', '1020', '100', '820', '90']


if __name__ == '__main__':
    print(parse_serial('COM8'))
