# We can call function within other function

# Sample 1
def name():
    print('My name is saddam')


def hai():
    print('Hello :)')
    name()
    name()


hai()

print('-' * 100)

# Sample 2
def items():
    ls = int(input('How many items of list that you want?: '))
    empty1 = []

    print('Insert list:')
    for i in range(ls) :
        item = input(f'{i + 1}. ')
        empty1.append(item)

    print('-' * 10, 'Your items:', '-' * 10, )
    for j in empty1 :
        print(j)


def main():
    for k in range(3):
        print(f'Loop {k + 1}: Input Items')
        items()
        print()


main()
