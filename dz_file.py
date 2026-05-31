import colorama

print("Атрибути та методи бібліотеки:")
for item in dir(colorama):
    print(item)

from colorama import init

init()
from colorama import Fore

print(Fore.RED + "Червоний текст")
print(Fore.GREEN + "Зелений текст")
from colorama import Back

print(Back.YELLOW + "Текст на жовтому фоні")
from colorama import Style

print(Style.BRIGHT + "Яскравий текст")
print(Style.RESET_ALL + "Звичайний текст")

colorama.deinit()

colorama.reinit()

from colorama import init, Fore, Back, Style

init()

print(Fore.RED + "Помилка")
print(Fore.GREEN + "Успіх")
print(Back.YELLOW + "Жовтий фон")
print(Style.BRIGHT + "Яскравий текст")
print(Style.RESET_ALL + "Звичайний текст")