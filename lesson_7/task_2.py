'''
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
'''
import random


def merge_sort(arr, start, end):
    ''' Сортировка вещественного массива методом слияния '''
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid, end)

        # слияние сортированных подсписков
        left = arr[start:mid]
        right = arr[mid:end]
        s = start
        i = 0
        j = 0
        while (start + i < mid and mid + j < end):
            if (left[i] <= right[j]):
                arr[s] = left[i]
                i += 1
            else:
                arr[s] = right[j]
                j += 1
            s += 1
        if start + i < mid:
            while s < end:
                arr[s] = left[i]
                i += 1
                s += 1
        else:
            while s < end:
                arr[s] = right[j]
                j += 1
                s += 1


def main():
    size = 15
    user_array = [round(random.uniform(0, 50), 2) for _ in range(size)]

    print('Исходный массив', user_array)
    merge_sort(user_array, 0, size)
    print('Сортированный массив:', user_array)


if __name__ == '__main__':
    main()