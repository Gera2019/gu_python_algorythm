'''
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''
import random


def swap_min_max(array):
    min_num = array[0]
    max_num = array[0]
    idx = 0

    for i in array:
        if i > max_num:
            max_num = i

        if i < min_num:
            min_num = i
    min_idx = array.index(min_num)
    max_idx = array.index(max_num)
    array[min_idx], array[max_idx] = max_num, min_num
    print(min_num, max_num)
    return array


usr_array = [random.randint(-50, 100) for _ in range(10)]
print(usr_array)
print()
print(swap_min_max(usr_array))