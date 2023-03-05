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
def open_serial(com, bod=9600, timeout=1):
    try:
        ser = serial.Serial(com, int(bod), timeout=timeout)
        return ser
    except serial.serialutil.SerialException:
        print("could not open port")



# Закрытие порта
def close_serial(ser):
    ser.close()


def parse_serial(ser):
    # 1011 это старт сообщения
    # 1011 90 1020 100 820 90
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
    ser = serial.Serial('COM8', timeout=1)
    print(parse_serial(ser))