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
