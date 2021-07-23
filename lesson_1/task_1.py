'''
1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

Алгоритм
1 ввод данных
2 проверка данных, что пользователь ввел именно число и оно трехзначное,
3 выделение отдельных цифр через делители сотен, десятков и единиц
или
3 генерация списка чисел из строкового значения и этот вариант мне кажется более понятным, с точки зрения восприятия.
'''


def check_data(N):
    try:
        int(N)
        if len(N) != 3:
            raise ValueError
    except ValueError:
        print('Вы ввели неверные данные')
        return False
    else: return True

# версия 1
def sum_3_dig_1(N):
    if check_data(N):
        N = int(N)
        sum_digits =  N//100 + (N - 100*(N//100))//10 + N%10
        mul_digits = (N//100) * ((N - 100*(N//100))//10) * (N%10)
        return (f'Сумма равна {sum_digits}, произведение равно {mul_digits}')

# версия 2
def sum_3_dig_2(N):
    if check_data(N):
        digits = [int(n) for n in N]
        sum_digits =  digits[0] + digits[1] + digits[2]
        mul_digits = digits[0] * digits[1] * digits[2]
        return (f'Сумма равна {sum_digits}, произведение равно {mul_digits}')

def main():
    ## Запрашиваем ввод пользователя
    number = input('Введите трехзначное целое число: ')
    print(sum_3_dig_1(number))
    print(sum_3_dig_2(number))


if __name__ == "__main__":
    main()