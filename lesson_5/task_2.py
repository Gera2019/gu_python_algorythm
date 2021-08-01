'''
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
'''
from collections import deque


def calc_hex(a, b):
    HEX_MAP = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
               '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
               8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    if len(a) < len(b):
        a_, b_ = [HEX_MAP[_] for _ in b], [HEX_MAP[_] for _ in a]
    else:
        a_, b_ = [HEX_MAP[_] for _ in a], [HEX_MAP[_] for _ in b]

    def add_hex(x, y):
        result = deque()
        mem = 0

        while x:
            if y:
                sum_ = x.pop() + y.pop()
            else:
                sum_ = x.pop() + mem
                mem = 0

            if sum_ >= 16:
                result.appendleft(sum_ - 16 + mem)
                mem = 1
            else:
                result.appendleft(sum_ + mem)
                mem = 0
        if mem:
            result.appendleft(mem)

        result = list(HEX_MAP[i] for i in result)
        print(f'{a} + {b} =', *result)

    add_hex(a_.copy(), b_.copy())

    def mult_hex(x, y):
        result = deque()
        temp = deque(deque() for _ in range(len(y)))
        mem = 0

        for i in range(len(y)):
            n = y.pop()
            for j in range(len(x) - 1, -1, -1):
                temp[i].appendleft(n * x[j])
            for _ in range(i):
                temp[i].append(0)

        for _ in range(len(temp[-1])):
            mult = mem
            for i in range(len(temp)):
                if temp[i]:
                    mult += temp[i].pop()
            if mult >= 16:
                result.appendleft(mult % 16)
                mem = mult // 16
            else:
                result.appendleft(mult)
        if mem:
                result.appendleft(mem)

        result = list(HEX_MAP[i] for i in result)
        print(f'{a} * {b} =', *list(result))

    mult_hex(a_.copy(), b_.copy())

def main():
    # a, b = input('Введите первое число: ').upper(), input('Введите второе число: ').upper()
    a, b = '3AB', 'FFF4C'
    calc_hex(a, b)

if __name__ == '__main__':
    main()