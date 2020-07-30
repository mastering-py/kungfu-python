# Sample of for with user input

# Sample 1
ls = int(input('How many items of list that you want?: '))
empty1 = []

print('Insert list:')
for i in range(ls):
    item = input(f'{i + 1}. ')
    empty1.append(item)
print()
print('-' * 20, 'Your items:', '-' * 20, )
for j in empty1:
    print(j)

print('-' * 100)

# Sample 2
num1 = int(input('Lower limit: '))
num2 = int(input('Upper limit: '))
rnum = int(input('Increment: '))

print('- Value -')
for k in range(num1, num2, rnum):
    print(k)
