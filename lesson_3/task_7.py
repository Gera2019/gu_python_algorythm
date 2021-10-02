'''
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
'''
import random


def find_2_min(array):
    min_num1 = array[0]
    min_num2 = min_num1

    for i in range(1, len(array)):
        if array[i] < min_num1:
            min_num2 = min_num1
            min_num1 = array[i]
        elif array[i] < min_num2:
            min_num2 = array[i]

    return min_num1, min_num2


usr_array = [random.randint(2, 50) for i in range(20)]

# Вывод результата
#
print('Исходный массив\n', usr_array)
print('Два наименьших элемента:', find_2_min(usr_array))
