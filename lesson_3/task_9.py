'''
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
'''
import random


usr_matrix = []
min_nums = []
R = random.randint(2,5) # количетво рядов
C = random.randint(2,5) # количетво столбцов


# Подготовим матрицу
for r in range(R):
	t = []
	for c in range(C):
		t.append(random.randint(2,51))
	usr_matrix.append(t)

# Ищем минимальные значения по столбцам
for c in range(C):
	min_num = usr_matrix[0][c]
	for r in range(1, R):
		if usr_matrix[r][c] < min_num:
			min_num = usr_matrix[r][c]
	min_nums.append(min_num)

# Ищем максимальное среди минимальных значений
max_num = min_nums[0]
for i in range(1, len(min_nums)):
	if min_nums[i] > max_num:
		max_num = min_nums[i]


# Вывод получившейся матрицы
for item in usr_matrix:
	print(*item)

print()
print('Минимальные числа по столбцам\n', min_nums)
print('Максимальное число среди них: ', max_num)
print()