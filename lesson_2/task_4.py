'''
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
'''


# version 1 RECURSION
def sum_num2(n):
    if n == 0:
        return n
    return 1 + (-1 / 2) * sum_num2(n - 1)


# version 2
def sum_num(n):
    element = 1
    result = 1

    for i in range(int(n) - 1):
        element *= (-1 / 2)
        result += element

    return result


def main():
    n = int(input('Введите число '))
    print(sum_num2(n))


if __name__ == "__main__":
    main()