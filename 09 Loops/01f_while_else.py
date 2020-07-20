# Without if, we can also combine while loop with else

num1 = 0

while num1 < 5:
    print(num1)
    num1 += 1
    if num1 == 5:
        print('This is part of if')
else:
    print('This is part of while not if')