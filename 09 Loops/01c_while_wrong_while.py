# Sample of wrong while loops

# Sample 1
# wrg1 = 0
#
# while wrg1 > 5: # condition
#     print(wrg1)
#     wrg1 += 1
#
# print('-' * 100)
"""
Sample 1 notes:
- When the condition is False, the iteration will not to start
"""

# Sample 2
wrg2 = 0

while wrg2 < 5:
    print(wrg2)
wrg2 += 1
"""
Sample 2 notes:
- In line 21, the while loop must relies on indentation. The increment statement is outside or not part of while loop 
and it will cause infinite loop
- Without the increment statement, the iteration is always on 0 with True condition and it will continue forever
"""
