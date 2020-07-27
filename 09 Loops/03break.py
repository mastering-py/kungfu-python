# With the break statement we can stop the loop even if the while loop condition is true

# Sample 1: Break in while
num1 = 0

while num1 < 5:
    print(num1)
    num1 += 3
    break # exit in first loop

print('-' * 100)

# Sample 2: Break in for
idFoods1 = ['bakso', 'nasi padang', 'soto', 'coto makassar']

for i in idFoods1:
    print(i)
    break

print('-' * 100)

# Sample 2: Break in for
idFoods2 = ['bakso', 'nasi padang', 'soto', 'coto makassar']

for i2 in idFoods2:
    print(i2)
    if i2 == 'nasi padang':
        break  # exit the loop for when its position is on 'nasi padang'
    # print(i2)  # this time the break comes before the print

print('-' * 100)

# Sample 3: Combine break with if and else
# while
num2 = 0

while num2 < 5:
    print(f'{num2 + 1}. Hello')  # num2 + 1 only change the starting count of print statement not the variable counter value
    if num2 == 3:
        break
    num2 += 1  # this increment will not execute because the break statement
else:
    print('THE LOOP IS TOTALLY STOP')
print('This is not part of while loop')

print('-' * 100)

# for
idFoods2 = ['bakso', 'nasi padang', 'soto', 'coto makassar']

for j in idFoods2:
    if j == 'soto':
        break  # exit the for loop when j is 'soto'
    print(j)
else:  # This is part of for not if
    print('THE LOOP IS TOTALLY STOP')
print('This is not part of for loop')  # any statement outside the for loop will be execute

print('-' * 100)

# Sample 4: Login using for loop
for k in range(3):  # range 0 - 2
    usr1 = input('User: ')
    pswd1 = input('Password: ')

    if usr1 == 'admin' and pswd1 == '12345':
        print('Login Success')
        break
    else:
        print('Password Failed!')

    if k == 2:
        print('Your chance is over...')
        break

print('-' * 100)

# Sample 5: Login using while loop
count = 3

while count > 0:
    usr2 = input('User: ')
    pswd2 = input('Password: ')

    if usr2 == 'admin' and pswd2 == '12345':
        print('Login Success')
        break
    else:
        print('Password Failed!')

    if count == 1:
        print('Your chance is over...')
        break

    count -= 1
