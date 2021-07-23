'''
Определить, какое число в массиве встречается чаще всего.
'''
import random


def number_rate(array):
	repeats = {}
	cnt = 0
	num = 0
	for item in array:
		if item in repeats:
			repeats[item] += 1

		else:
		 	repeats[item] = 1
		if repeats[item] > cnt:
			cnt = repeats[item]
			num = item

	return num


usr_array = [random.randint(1,3) for _ in range(10)]
print(usr_array)
print()
print(number_rate(usr_array))