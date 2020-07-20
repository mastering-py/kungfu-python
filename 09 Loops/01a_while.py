# With the while loop we can execute a set of statements as long as a condition is true. It will stop when the increment is false.

# Sample 1 (Default while loop)
num1 = 0 # variable counter

while num1 < 5:  # loop range is 0 - 4
    print(num1)  # while loop is relies on indentation too
    num1 += 1  # increment
print('Good bye')
"""
Sample 1 notes:
- print num1 as long as num1 is less than 5
- the while loop is start from 0 to 4
- 5 < 5 is false because 5 == 5
- without increment statement, the while loop is always true and cause the loop will continue forever (infinite loop) 
- print('Good bye') is not part of while loop
"""

print('-' * 100)

# Sample 2
num2 = 1 # Variable counter is start from 1

while num2 <= 5:  # the while range is start from 1 and less than or equal to 5
    print(num2)
    num2 += 1

print('-' * 100)

# Sample 3 (Condition with two variables)
num3 = 1
var1 = 5

while num3 <= var1:
    print(f'Hello {num3}')
    num3 += 1
