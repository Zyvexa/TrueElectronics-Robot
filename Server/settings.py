from colorama import init
from colorama import Fore
init()


# Словарь для логов
warn_status = {'error': f'{Fore.RESET}[{Fore.RED}!{Fore.RESET}]{Fore.RED}',
               'warning': f'{Fore.RESET}[{Fore.YELLOW}Warn{Fore.RESET}]{Fore.YELLOW} ',
               'success': f'{Fore.RESET}[{Fore.GREEN}+{Fore.RESET}]{Fore.GREEN}',
               'info': f'{Fore.RESET}[{Fore.LIGHTBLUE_EX}i{Fore.RESET}]{Fore.LIGHTBLUE_EX}',
               'unknown': f'{Fore.RESET}[{Fore.MAGENTA}?{Fore.RESET}]{Fore.MAGENTA}'}


def log(text, status):  # логи в консоль
    print(warn_status[status], text + Fore.RESET)

cmds = ['[data]', 'GET', '[check]', '[get]']

# успешный ответ для браузера
HDRS = 'HTTP/1.1 200  OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
# ошибка 404
HDRS_404 = 'HTTP/1.1 404  OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
