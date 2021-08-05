'''
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.
'''
from collections import deque
import math
import random
from time import time
from sys import getsizeof


print('Занимаемая память различными переменными для каждой из программ')


# @profile
def prime(n):
    n = int(n)

    primes = [2]
    number = 3
    while len(primes) < n:
        is_prime = True
        for i in primes:
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
        number += 2
    check_mem = [getsizeof(n), getsizeof(primes), getsizeof(i), getsizeof(is_prime)]
    print(f'Программа prime({n}) - {sum(check_mem)} Байт')
    return primes[-1]


# @profile
def erato(n):
    n = int(n)
    size = check_primes(n)
    arr = [_ for _ in range(size + 1)]
    arr[1] = 0
    i = 2
    if size == 1:
        return i

    while i <= size:
        if arr[i] != 0:
            j = i + i
            while j <= size:
                if arr[j] != 0:
                    arr[j] = 0
                j = j + i
        i += 1
    primes = [_ for _ in arr if _ != 0]
    while len(primes) > n:
        primes.pop()

    check_mem = [getsizeof(size), getsizeof(arr), getsizeof(i), getsizeof(n), getsizeof(primes)]
    print(f'Программа erato({n}) - {sum(check_mem)} Байт')
    return primes[-1]

#  пи(n) функция, которая показывает вероятностное количество простых чисел в указанном диапазоне.
#  Взято из теоремы о распределении простых чисел.
def check_primes(n):
    cnt_primes = 0
    number = n
    while cnt_primes < n:
        if math.log(number) == 0:
            break
        cnt_primes = number / math.log(number)
        number += 1
    return number


# @profile
def position_search(chr1, chr2):
    alphabet = [chr(i) for i in range(97,123)]
    chr1_position = alphabet.index(chr1) + 1
    chr2_position = alphabet.index(chr2) + 1
    chrs_num_between = abs(chr1_position - chr2_position) - 1
    # print(f'Позиция буквы {chr1} - {chr1_position},\n'
    #       f'Позиция буквы {chr2} - {chr2_position},\n'
    #       f'Количество букв междну ними {chrs_num_between}')
    check_mem = [getsizeof(alphabet), getsizeof(chr1_position), getsizeof(chr2_position), getsizeof(chrs_num_between)]
    print(f'Программа position_search({chr1}, {chr2}) - {sum(check_mem)} Байт')


# @profile
def max_negative(array):
    max_num = 0
    for item in array:
        if item < 0:
            if item < max_num:
                max_num = item
    check_mem = [getsizeof(max_num), getsizeof(item)]
    print(f'Программа max_negative("array") - {sum(check_mem)} Байт')
    return max_num


def main():
    s1 = time()
    prime(10000)
    e1 = time()
    s2 = time()
    erato(10000)
    e2 = time()

    s3 = time()
    prime(100)
    e3 = time()

    s4 = time()
    erato(100)
    e4 = time()

    s5 = time()
    position_search('u', 'v')
    e5 = time()

    s6 = time()
    arr = [random.randint(-50, 50) for i in range(20)]
    max_negative(arr)
    e6 = time()


    print(f'Программа prime(10000) выполнялась - {(e1 - s1)} сек.\n'
          f'Программа erato(10000) выполнялась - {e2 - s2} сек.\n'
          f'Программа prime(100) выполнялась - {(e3 - s3)} сек.\n'
          f'Программа erato(100) выполнялась - {e4 - s4} сек.\n'          
          f'Программа position_search() выполнялась - {e5 - s5} сек.\n'
          f'Программа max_negative() выполнялась - {e6 - s6} сек.')

    print()

if __name__ == '__main__':
    main()

