'''
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
'''
import random


def max_negative(array):
	max_num = 0
	for item in array:
		if item < 0:
			if item < max_num:
				max_num = item
	return max_num


usr_array = [random.randint(-50,50) for i in range(20)]
print(usr_array)
print()
print(max_negative(usr_array))