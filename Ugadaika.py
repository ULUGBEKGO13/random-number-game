from random import *
again = 'NO'
count = 0
print('Добро пожаловать в числовую угадайку, вы можете выбрать диапазон чисел от 1 до вашего числа')
right = input()
def rightx2(right):
    while not(right.isdigit()):
        right = input('Может быть вы введете число больше 1?')
    else:
        while int(right) < 2:
            right = input('Может быть вы введете число больше 1?')
        else:
            return right
right = rightx2(right)
right = int(right)
r = randint(1, right)
n = input('Введите предполагаемое число от 1 до :' + str(right))
def is_valid_again(again):
    while not(again.isalpha()):
        again = input('Может быть все-таки введем ответ yes или no?')
    else:
        while again.lower() != 'yes' and again.lower() != 'no':
            again = input('Может быть все-таки введем ответ yes или no?')
        else:
            return again.lower()
def is_valid(number, right):
    while not(number.isdigit()):
        number = input('А может быть все-таки введем число от 1 до ' + str(right) + '?')
    else:
        while not(0 < int(number) < right + 1):
            number = input('А может быть все-таки введем число от 1 до ' + str(right) + '?')
        else:
            return number
n = is_valid(n, right)
n = int(n)
while n != r:
    if n < r:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        count += 1
        n = input()
        n = is_valid(n, right)
        n = int(n)
    elif n > r:
        print('Ваше число больше загаданного, попробуйте еще разок')
        count += 1
        n = input()
        n = is_valid(n, right)
        n = int(n)
else:
    count += 1
    print('Вы угадали, поздравляем!', 'Ваше количество попыток: ' + str(count), sep = "\n")
    again = input(('Желаете ли вы еще раз поиграть?'))
    again = is_valid_again(again)
while again.lower() == 'yes':
    count = 0
    print('Добро пожаловать в числовую угадайку, вы можете выбрать диапазон чисел от 1 до вашего числа')
    right = input()
    right = rightx2(right)
    right = int(right)
    r = randint(1, right)
    n = input('Введите предполагаемое число от 1 до :' + str(right))
    n = is_valid(n, right)
    n = int(n)
    while n != r:
        if n < r:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            count += 1
            n = input()
            n = is_valid(n, right)
            n = int(n)
        elif n > r:
            print('Ваше число больше загаданного, попробуйте еще разок')
            count += 1
            n = input()
            n = is_valid(n, right)
            n = int(n)
    else:
        count += 1
        print('Вы угадали, поздравляем!', 'Ваше количество попыток: ' + str(count), sep = "\n")
        again = input(('Желаете ли вы еще раз поиграть?'))
        again = is_valid_again(again)
