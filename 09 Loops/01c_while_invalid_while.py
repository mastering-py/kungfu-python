# Sample of invalid while loops

# Sample 1
# wrg1 = 0
#
# while wrg1 > 5: # condition
#     print(wrg1)
#     wrg1 += 1
#
"""
Sample 1 notes:
- When the condition is False, the iteration will not to start
"""

# print('-' * 100)

# Sample 2
wrg2 = 0

while wrg2 < 5:
    print(wrg2)
wrg2 += 1

"""
Sample 2 notes:
- In line 22, the while loop must relies on indentation. When the increment statement is outside or not part of while 
loop it will cause infinite loop
- Without the increment statement, the iteration is always stay on 0 with True condition and it will continue forever
"""
