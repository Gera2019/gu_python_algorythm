'''
6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

Алгоритм
1. Ввод номера буквы
2. Проверяем, что номер буквы лежит в диапазоне от 1 до 26 (количество букв в лаитнском алфавите)
3. Выводим нужную букву, используя список букв алфавита
'''

def letter_search(chr_index):
    if  chr_index < 1 or chr_index > 26:
        print('Нет буквы с таким порядковым номером')
    else:
        alphabet = [chr(i) for i in range(97,123)]
        return f'Буква {alphabet[chr_index - 1]}'

def main():
    ## Запрашиваем ввод пользователя
    chr_index = int(input('Введите номер буквы: '))
    print(letter_search(chr_index))


if __name__ == "__main__":
    main()
