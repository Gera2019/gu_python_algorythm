'''
В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, то вывести загаданное число.
'''

import random


def guess_the_number():
    secret = random.randrange(1, 100)
    guess_try = 1
    print('Угадайте число от 1 до 100 за 10 попыток')

    while guess_try <= 10:
        x = int(input('Ваше число '))
        if x == secret:
            print('Вы отгадали!')
            break
        elif x > secret:
            print('Предложенное число больше загаданного')
        else:
            print('Предложенное число меньше загаданного')
        print(f'У вас осталось {10 - guess_try} попыток')
        guess_try += 1

    else:
        print(f'Увы, вы не отгадали. Загаданное число {secret}')

    print(f'Загаданное число - {secret}, ваше число - {x}')


guess_the_number()