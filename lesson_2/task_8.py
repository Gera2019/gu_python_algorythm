'''
Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
'''
import random


def count_digit(range_size, n):
    num_list = [random.randint(1, random.randrange(1000)) for i in range(range_size)]
    print(num_list)

    cnt = 0

    for item in num_list:
        if n in str(item):
            cnt += str(item).count(n)  # учитываем, что в числе может быть несколько одних и тех же цифр, например 334
    return cnt


def main():
    n = int(input('Введите количество генерируемых чисел '))
    x = input('Введите цифру, которую необходимо посчитать ')
    print(count_digit(n, x))


if __name__ == "__main__":
    main()
