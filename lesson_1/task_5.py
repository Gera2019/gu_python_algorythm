'''
5. Пользователь вводит две буквы.
Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

Алгоритм
1. Ввод двух букв с приведением их в строчные символы
2. Определяем позицию каждого символа, используя индексы списка букв алфавита
3. Считаем количество букв между этими позициями
4. Вывод результата
'''
def position_search(chr1, chr2):
    alphabet = [chr(i) for i in range(97,123)]
    chr1_position = alphabet.index(chr1) + 1
    chr2_position = alphabet.index(chr2) + 1
    chrs_num_between = abs(chr1_position - chr2_position) - 1
    print(f'Позиция буквы {chr1} - {chr1_position},\n'
          f'Позиция буквы {chr2} - {chr2_position},\n'
          f'Количество букв междну ними {chrs_num_between}')

def main():
    ## Запрашиваем ввод пользователя
    chr1, chr2 = input('Введите две буквы через запятую: ').lower().split(',')
    position_search(chr1.strip(), chr2.strip())


if __name__ == "__main__":
    main()