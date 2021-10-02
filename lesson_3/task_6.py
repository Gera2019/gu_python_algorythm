'''
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
'''
import random


def sum_nums(array):
    min_num = array[0]
    max_num = array[0]

    for item in array:
        if item > max_num:
            max_num = item
        if item < min_num:
            min_num = item

    print('Минимальный и максимальный элементы соответственно:', min_num, ',', max_num)

    if array.index(min_num) < array.index(max_num):
        start = array.index(min_num) + 1
        end = array.index(max_num)
        sum_ = sum(array[start:end])

        print('Срез элементов', array[start:end])

    else:
        start = array.index(max_num) + 1
        end = array.index(min_num)
        sum_ = sum(array[array.index(max_num) + 1:array.index(min_num)])
        print('Срез элементов', array[start:end])

    return sum_


usr_array = [random.randint(-50, 50) for i in range(20)]

print('Исходный массив\n', *usr_array)
print()
print('Сумма элементов между минимальным и максимальным элементами:', sum_nums(usr_array))