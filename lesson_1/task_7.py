'''
7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
составленного из этих отрезков.
Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.

Алгоритм
1. Ввод данных
2. Проверка условия возможности построения треугольника с указанными длинами сторон. Для чего проверяеися условия:
a < b + c
b < a + c
c < a + b
3. Далее определяем тип треугольника, если он существует, перебирая условия:
 - равенства всех сторон: (треугольник равносторонний),
 - равенства каких-либо двух сторон (равнобедренный треугольник),
 - неравенство всех сторон (треугольник разносторонний)
4. Вывод результатов
'''

def check_triangle(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        print('Треугольник с такими длинами сторон существует')
        if a == b == c:
            print('Треугольник равносторонний')
        elif a == b or a == c or b == c:
            print('Треугольник равнобедренный')
        else:
            print('Треугольник разносторонний')
    else:
        print('Треугольник с такими длинами сторон не существует')

def main():
    ## Запрашиваем ввод пользователя
    a, b, c = (int(n.strip()) for n in input('Введите длины трех отрезков: ').split(','))
    check_triangle(a,b,c)


if __name__ == "__main__":
    main()
