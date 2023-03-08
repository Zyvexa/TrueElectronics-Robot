from colorama import init
init()
from colorama import Fore, Back, Style
print(Fore.GREEN + 'зеленый текст')
print(Back.BLUE + '[+]'+ Style.RESET_ALL)
print(Style.BRIGHT + 'стал ярче' + Style.RESET_ALL)
print('обычный текст')