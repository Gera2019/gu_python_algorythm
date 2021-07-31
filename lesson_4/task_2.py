'''
Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования Решета Эратосфена;
Использовать алгоритм решето Эратосфена
'''
import math


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
    return primes[-1]


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


# O(n^2)
def main():
    print(prime(100)) # result 1299709 for n = 100000
    print(erato(100))  # result 1299709
    # print(check_primes(2))



if __name__ == '__main__':
    main()
