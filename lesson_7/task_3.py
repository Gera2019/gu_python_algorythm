'''
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
медианы, в другой – не больше медианы.
Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках.
'''
from random import randint


def find_median(arr):
    ''' Поиск медианы в масииве натуральных чисел без предварительной сортировки '''
    size = len(arr)
    half = size // 2
    median = None

    for i in range(size):
        left_half = 0
        right_half = 0

        for j in range(size):
            if j == i:
                continue
            if arr[j] < arr[i]:
                left_half += 1
                if left_half > half:
                    break
            if arr[j] > arr[i]:
                right_half += 1
                if right_half > half:
                    break

            if j == size - 1:
                median = arr[i]
                break

    return median


def main():
    m = randint(1, 10)
    user_array = [randint(0, 100) for _ in range(2*m + 1)]

    # Проверка работы скрипта
    print('Исходный массив', user_array)
    print('Медиана масива без использования сортировки', find_median(user_array))
    print('Для проверки:')
    print(f'Сортированный массив {sorted(user_array)}, медиана - {sorted(user_array)[m]}')


if __name__ == '__main__':
    main()
