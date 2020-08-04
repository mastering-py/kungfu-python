# Combine with boolean

# Sample 1
var1 = True
count = 0

while var1:
    print('Number', count + 1)
    count += 1
    if count == 10:
        var1 = False

"""
Sample 1 notes:
- This sample is how to stop the infinite loop by changing the condition to False using if statement
- count + 1 will make count start on 1
- with if condition the while loop will stop at 10 by changing the var1 to False
"""

print('-' * 100)

# Sample 2
choice = True

while choice:
    a = int(input('Input value 1: '))
    b = int(input('Input value 2: '))
    print(f'{a} + {b} = {a + b}')
    choice = input('Want to repeat (y/n)?: ')
    if 'Y' != choice != 'y':
        choice = False
    print()