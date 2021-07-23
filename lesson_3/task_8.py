'''
Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
'''

usr_matrix = []

for i in range(5):
    t = []
    raw_sum = 0
    print(f'{i + 1} строка')
    for j in range(3):
        t.append(int(input(f'{j + 1} элемент: ')))
        raw_sum += t[j]
    print(f'Сумма: {raw_sum}')
    t.append(raw_sum)
    usr_matrix.append(t)

# Вывод получившейся матрицы
for item in usr_matrix:
    print(*item)