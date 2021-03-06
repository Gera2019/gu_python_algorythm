'''
3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b,
проходящей через эти точки.

Решение задачи сводится к расчету коэффициентов k и b линейного уравнения y=kx+b, где
k = 1/(x2 - x1)
b = y1/(y2 - y1) - x1/(x2 - x1)
'''

def get_equation(x1, y1, x2, y2):
    pnt1 = {'x': x1, 'y': y1}
    pnt2 = {'x': x2, 'y': y2}
    print(pnt1, pnt2)
    k = 1 / (pnt2['x'] - pnt1['x'])
    b = pnt1['y'] / (pnt2['y'] - pnt1['y']) - pnt1['x'] / (pnt2['x'] - pnt1['x'])
    equation = f'y={k}x{+b:+}'

def get_equation(x1, y1, x2, y2):
    if x1 == x2:
        equation = f'y={x1}'
    else:
        pnt1 = {'x': x1, 'y': y1}
        pnt2 = {'x': x2, 'y': y2}
        print(pnt1, pnt2)
        k = 1 / (pnt2['x'] - pnt1['x'])
        b = pnt1['y'] / (pnt2['y'] - pnt1['y']) - pnt1['x'] / (pnt2['x'] - pnt1['x'])
        equation = f'y={k}x{+b:+}'
    return equation


def main():
    ## Запрашиваем ввод пользователя и обрабатываем полученные значения, прежде чем передать в функцию
    x1, y1 = (int(n.strip()) for n in input('Введите координаты первой точки: ').split(','))
    x2, y2 = (int(n.strip()) for n in input('Введите координаты второй точки: ').split(','))

    print(get_equation(x1, y1, x2, y2))


if __name__ == "__main__":
    main()

