'''
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843.
'''

# version 1
# slice
def reverse_num(n):
	return n[::-1]

# version 2
# recursion
def reverse_num2(n):
	if len(str(n)) == 1:
		print(n)
		return n
	print(int(n), int(n) % (10**(len(str(n)) - 1)))
	return int(n) % reverse_num2(int(n) % (10**(len(str(n)) - 1)))

def main():
	n = input('Введите число ')
	print(reverse_num2(n))


if __name__ == "__main__":
    main()