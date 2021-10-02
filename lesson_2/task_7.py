'''
Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется
равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.
'''
import random


def check_set(n):
	if n <= 1:
		return n
	return n + check_set(n - 1)


n = random.randint(1, 10)

print(f'Количество элементов {n}')
print(f'1+2+...+{n} = {n}({n}+1)/2 {check_set(n) == n*(n + 1)/2}')
print(check_set(n))
