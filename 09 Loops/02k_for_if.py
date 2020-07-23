# Combine for with if

# Sample 1
idFoods1 = ['bakso', 'nasi padang', 'soto', 'coto makassar']

for j in idFoods1:
    print(j)
    if j == 'soto':
        print(f'--- {j} was found ---')

print('-' * 100)

# Sample 2
num1 = int(input('Input number that you want to find (0 - 10): '))

for j in range(11):
    print(j)
    if j == num1:
        print(f'--- {j} was found ---')

print('-' * 100)

# Sample 3
idFoods2 = ['bakso', 'nasi padang', 'soto', 'coto makassar']

for k in range(len(idFoods2)):
    print(idFoods2[k])
    if idFoods2[k] =='nasi padang':
        print(f'--- {idFoods2[k]} was found ---')
