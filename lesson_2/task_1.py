'''
Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений.
Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.
'''


def simple_calc():
    msg1 = '|  Введите выражение в виде "a [+.-.*,/] b, разделяя пробелами"  |\n'
    msg2 = 'Для выхода наберите 0\n\n'
    msg_delim = f'{(len(msg1) - 1) * "-"}\n'
    while True:

        user_data = input(msg_delim + msg1 + msg_delim + msg2)

        if user_data == '0':
            print('Программа завершена')
            return

        try:
            user_data = user_data.split(' ')
            a, op_type, b = user_data

            if op_type not in ('+', '-', '*', '/'):
                print('Введен некорректный тип операции!\n')
                op_type = input('Введите тип операции\n')
            elif op_type == '/' and b == '0':
                print('Ошибка деления на 0')
                simple_calc()

            a = float(a)
            b = float(b)

        except ValueError:
            print(f'Введены некорректные значения\n')

        else:
            if op_type == '+':
                result = a + b
            elif op_type == '-':
                result = a - b
            elif op_type == '*':
                result = a * b
            elif op_type == '/':
                result = a / b

            result = int(result) if str(result)[-1] == '0' else result
            print(f' --{len(str(result)) * "-"}--')
            print(f'|  {result}  |')
            print(f' --{len(str(result)) * "-"}--\n')
    return result


def main():
    simple_calc()


if __name__ == "__main__":
    main()