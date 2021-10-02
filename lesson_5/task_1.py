'''
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
(за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести
наименования предприятий, чья прибыль ниже среднего.
'''
import collections
import random


def make_report(data):
    income_total = ()
    print(f'{"*" * 46} НАЧАЛО {"*" * 46}')
    print('Прибыль каждого из предприятий за год:')
    for name, income in data.items():
        print(f'{name} | прибыль за год | {sum(income)}')
        income_total += income
    print('*' * 100)

    income_total_avg = sum(income_total) / len(data)
    print(f'Средняя прибыль за год для всех предприятий: {income_total_avg}')
    print('*' * 100)

    print('Предприятия, у которых прибыль выше среднего:')
    for name, income in data.items():
        if sum(income) > income_total_avg:
            print(f'{name} - {sum(income)}')

    print('Предприятия, у которых прибыль ниже среднего:')
    for name, income in data.items():
        if sum(income) < income_total_avg:
            print(f'{name} - {sum(income)}')

    print(f'{"*" * 46} КОНЕЦ {"*" * 47}')


income_report = collections.namedtuple('income_report', ['q1', 'q2', 'q3', 'q4'])
enterprises = {}


def main():
    n = int(input('Количество предприятий: '))
    for i in range(n):
        # name = input(f'{str(_ + 1)}-е предприятие: ')
        # quarter_1 = int(input('Прибыль за 1-й квартал: '))
        # quarter_2 = int(input('Прибыль за 2-й квартал: '))
        # quarter_3 = int(input('Прибыль за 3-й квартал: '))
        # quarter_4 = int(input('Прибыль за 4-й квартал: '))

        name = f'Рога и копыта {i + 1}'
        quarter_1 = random.randint(20, 300)
        quarter_2 = random.randint(20, 300)
        quarter_3 = random.randint(20, 300)
        quarter_4 = random.randint(20, 300)

        enterprises[name] = income_report(
            q1=quarter_1,
            q2=quarter_2,
            q3=quarter_3,
            q4=quarter_4
        )
    make_report(enterprises)


if __name__ == '__main__':
    main()
