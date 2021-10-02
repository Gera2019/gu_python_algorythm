'''
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
'''


# version 1
def count_nums(n):
    evens = 0
    odds = 0
    for i in n:
        if int(i) % 2 == 0:
            evens += 1
        else:
            odds += 1

    msg = f'Количество четных чисел равно {evens}, а нечетеных {odds}'
    return msg


# version 2
def count_nums2(n):
    evens = len([i for i in n if int(i) % 2 == 0])
    odds = len(n) - evens

    msg = f'Количество четных чисел равно {evens}, а нечетеных {odds}'
    return msg


def main():
    n = input('Введите натуральное число ')
    print(count_nums(n))


if __name__ == "__main__":
    main()