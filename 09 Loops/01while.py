# With the while loop we can execute a set of statements as long as a condition is true. It will stop when the increment is false.

# Sample 1
num1 = 0

while num1 < 5: # loop range is 0 - 4. Print num1 as long as num1 is less than 5
    print(num1) # while loop is relies on indentation too
    num1 += 1 # this is increment. without it, the loop will continue forever
"""
Sample 1 note:
- print num1 as long as num1 is less than 5
- the while loop is start from 0 to 4
- 5 < 5 is false because 5 == 5
"""

print('-' * 100)

# Sample of wrong while loop:
# a. Without the increment statement, the iteration is always on 0 and it will continue forever
# num1a = 0
#
# while num1a < 5:
#     print(num1a)

# b. The condition is false, so the iteration is not to start
# num1b = 0
#
# while num1b > 5:
#     print(num1b)
#     num1b += 1
#
# print('-' * 100)

# Sample 2
word1 = input('Set some words: ')
num2 = 0

while num2 < 5:
    print(f'{num2 + 1}. {word1}')
    num2 += 1

print('-' * 100)

# Sample 3 (Combine with if)
num3 = 0

while num3 < 5:
    print(num3)
    if num3 == 3:
        print('Number 3 was found')
    num3 += 1

