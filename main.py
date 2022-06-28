from colorama import Fore, Back, Style, init

init(autoreset=True)
print(Back.CYAN + 'Программа для вычисления ИМТ(индекс массы тела)' + "\n")
name = input('Как вас зовут? : ').title()


def defecit():
    print(name + Fore.YELLOW + Style.BRIGHT +
          ', у вас выраженый дефецит массы, иди в mc donadls')


def little():
    print(name + Fore.GREEN + Style.BRIGHT + ', у вас недостаточно массы тела')


def norm():
    print(name + Fore.BLUE + Style.BRIGHT + ', у вас нормальный вес тела')


def preobesity():
    print(name + Fore.YELLOW + Style.BRIGHT + ', у вас предожирение')


def obesity_1():
    print(name + Fore.RED + Style.BRIGHT +
          ', у вас ожирение 1-й степени, срочно иди в зал')


def obesity_2():
    print(name + Fore.RED + Style.BRIGHT +
          ', у вас ожирение 2-й степени, печально')


def obesity_3():
    print(name + Fore.RED + Style.BRIGHT +
          ', у вас ожирение 3-й степени, срочно в больницу')


def obesity_4():
    print(name + Fore.MAGENTA + Style.BRIGHT +
          ', у вас ожирение 4-й степени, как ты ещё живешь?')


IMT = 0
height = abs(int(input('Какой ваш рост?(см) : ')))
height *= 0.01
weight = abs(float(input('Какой ваш вес?(кг) : ')))
IMT = round(weight / height**2, 2)
print('Ваш индекс массы тела - ' + str(IMT))
if IMT < 16.5:
    defecit()
elif IMT > 16.5 and IMT <= 18.49:
    little()
elif IMT >= 18.5 and IMT <= 24.99:
    norm()
elif IMT <= 25 and IMT <= 29.99:
    preobesity()
elif IMT >= 30 and IMT <= 34.99:
    obesity_1()
elif IMT >= 35 and IMT <= 39.99:
    obesity_2()
elif IMT >= 40 and IMT <= 44.99:
    obesity_3()
else:
    obesity_4()
