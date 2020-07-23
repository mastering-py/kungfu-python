# Sample of for with user input

ls = int(input('How many items of list did you want?: '))
empty1 = []

print('Insert list:')
for i in range(ls):
    item = input(f'{i + 1}. ')
    empty1.append(item)
print()
print('-' * 20, 'Your items:', '-' * 20, )
for j in empty1:
    print(j)
