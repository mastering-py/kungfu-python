# With the while loop we can execute a set of statements as long as a condition is true. It will stop when the increment is false.

# Sample 1 (Default while loop)
num1a = 0

while num1a < 5: # loop range is 0 - 4. Print num1 as long as num1 is less than 5
    print(num1a) # while loop is relies on indentation too
    num1a += 1 # this is increment. without it, the loop will continue forever
"""
Sample 1 note:
- print num1 as long as num1 is less than 5
- the while loop is start from 0 to 4
- 5 < 5 is false because 5 == 5
"""

print('-' * 100)

# Sample 1 (Other)
num1a = 1

while num1a <= 5: # the while range is 1 less than or equal to 5
    print(num1a)
    num1a += 1

print('-' * 100)

# Sample of wrong while loop:
# a. Without the increment statement, the iteration is always on 0 and it will continue forever
# num1a = 0
#
# while num1a < 5:
#     print(num1a)

# b. When the condition is false, the iteration will not to start
# num1b = 0
#
# while num1b > 5:
#     print(num1b)
#     num1b += 1
#
# print('-' * 100)

# Sample 2 (Combine with user input)
word1a = input('Set some words: ')
num2a = 0

print('Your word is sets in 5 times:')
while num2a < 5:
    print(f'{num2a + 1}. {word1a}')
    num2a += 1

print('-' * 100)

# Sample 2 (other)
word1a = input('Set some words: ')
rep1 = int(input('Hom much time do you want to repeat?: '))
num2a = 0

print(f"Your word '{word1a}' is sets in {rep1} times:")
while num2a < rep1:
    print(f'{num2a + 1}. {word1a}')
    num2a += 1

print('-' * 100)

# Sample 3 (Combine with if)
num3 = 0

while num3 < 5:
    print(num3)
    if num3 == 3:
        print('Number 3 was found')
    num3 += 1

print('-' * 100)

# Sample 4 (Combine with boolean)
num4 = True
count = 0

while num4:
    print('Number', count + 1)
    count += 1
    if count == 5:
        num4 = False

print('-' * 100)

# Sample 5 (Yes/No condition using while loop)
choice = 'y' # this condition is true

while choice == 'y':
    name = input('What is your name?: ')
    age = int(input('How old are you?: '))

    print('======== Your Data ========')
    print(f'Your name is {name}')
    print(f'You are {age} years old')

    choice = input('Want to repeat (y/n)?: ') # the while loop will stop except 'y' key

print('-' * 100)

# Sample 6 (Countdown)
num5 = int(input('Fill what number you want to countdown: '))
#k = 17

while num5 > 0 :
    print(num5)
    num5 -= 1