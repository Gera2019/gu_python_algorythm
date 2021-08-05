'''
1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
'''
from random import randint


def bubble_sort(arr):
    ''' Сортировка целочисленного массива методом пузырька (двусторонний) '''
    N = len(arr)

    def swap(lst, a, b):
        lst[a], lst[b] = lst[b], lst[a]
        return lst

    if N == 1:
        return arr
    elif N == 2:
        return arr if arr[0] < arr[1] else swap(arr, 0, 1)

    i = 0
    while N - i >= 3:
        for j in range(i, N - 1):
            if arr[j + 1] < arr[j]:
                swap(arr, j, j + 1)
            if arr[-j - 2] > arr[-j - 1]:
                swap(arr, (-j - 2), (-j - 1))
        i += 1
        N -= 1

    return arr


def main():
    size = randint(3, 50)
    user_array = [randint(-100, 100) for _ in range(size)]
    print(f'{user_array}\n{bubble_sort(user_array)}')


if __name__ == '__main__':
    main()