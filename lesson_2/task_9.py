'''
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
'''
import random


def max_sum(num_list):
    num_sum = 0
    for item in num_list:
        item_sum = sum(int(i) for i in str(item))
        if item_sum >= num_sum:
            res, num_sum = item, item_sum

    return f'Число - {res}, сумма его цифр - {num_sum}'


num_list = [random.randint(1, random.randrange(1000)) for i in range(10)]
print(num_list)
print(max_sum(num_list))