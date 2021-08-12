'''
1. Определить количество различных подстрок с использованием хеш-функции.
Задача: на вход функции дана строка, требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
'''
from hashlib import sha1

def substring_count(str):
    length = len(str)
    h = []
    i = 0
    j = length

    while i <= length:
        while j > i:
            substring = str[i:j]
            print(substring, end=', ')
            digest = sha1(substring.encode('utf-8')).hexdigest()
            if digest not in h:
                h.append(digest)
            j -= 1
        j = length
        i += 1

    return len(h) - 1











def main():
    text = 'elleelle'
    print(substring_count(text))


if __name__ == '__main__':
    main()