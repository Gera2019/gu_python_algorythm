'''
2. Закодировать любую строку по алгоритму Хаффмана.
'''
def huffman(str):
    repeats = []
    tree = {}
    counter = 0
    s_list = []
    for symbol in str:
        print(symbol)
        if symbol not in repeats:
            repeats.append(symbol)
            counter = 1
            s_list.append(symbol)
            tree[counter] = s_list

        elif tree.get(counter):
            counter = 1 + int(*(k for k, v in tree.items() if symbol in v))
            tree[counter - 1].remove(symbol)
            if not tree[counter - 1]:
                tree.pop(counter - 1)
            if tree.get(counter):
                tree[counter].append(symbol)
            else:
                tree[counter] = [symbol]

        print(counter)
        print(tree)

def main():
    text = 'hello'
    print(huffman(text))


if __name__ == '__main__':
    main()