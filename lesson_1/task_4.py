'''
4. Написать программу, которая генерирует в указанных пользователем границах:
- случайное целое число;
- случайное вещественное число;
- случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

Алгоритм задачи
1. Ввод значений диапазона
2. Определение типа введеных данных
3. Если типы данных были определены в рамках предложенных условием задачи
  (целые числа, вещественные числа или буквы алфавита), то выводится случайное значение из диапазона,
  указанного пользователем в соответствии с определенным типом
4. Если тип данных определить не удалось, то происходит исключение с выводом ошибки о некорректности введеных данных
'''
import random


def check_type(usr_range):
    a,b = usr_range
    alphabet = [chr(i) for i in range(97,123)]
    try:
        # сразу проверяем, не введены ли буквы алфавита
        if a.lower() in alphabet and b.lower() in alphabet:
            result = a.lower(),b.lower()
        else:
            # т.к. целые числа у нас являются подмножеством вещестевенных, пытаемся данные сразу перевести в тип float
            a = float(a)
            b = float(b)
            # в случае, если преобразование не привело к исключению, то далее проверяем границы диапазона
            if b < a:
                raise ValueError
            else:
                # здесь определяем были ли введены целые числа
                result = (int(a),int(b)) if int(str(a).split('.')[1]) == 0 else (a,b)
    except ValueError:
        print('Ошибка значений')
        return False
    else:
        return result

def gen_random (usr_range):
    data_range = check_type(usr_range)
    if data_range:
        a,b = data_range
        if isinstance(a, float):
            # высчитываем, сколько знаков должно быть после точки, в зависимости от введенных пользователем значений
            precision = len(str(a).split('.')[1])
            return round(random.uniform(a, b), precision)
        elif isinstance(a, int):
            return random.randrange(a, b)
        elif isinstance(a, str):
            return chr(random.randrange(ord(a), ord(b)))
    else:
        print('Введены некорректные значения диапазона')


def main():
    ## Запрашиваем ввод пользователя
    user_range = (item.strip() for item in input('Введите значения диапазона: ').split(','))
    print(gen_random(user_range))

if __name__ == "__main__":
    main()