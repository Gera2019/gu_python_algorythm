'''
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
'''

numbers_range = range(2,100)

result = {n:0 for n in range(2,10)}

for number in range(2,100):
	for item in range(2,10):
		print(number, item)
		if number%item == 0:
			result[item] += 1


print(result)
