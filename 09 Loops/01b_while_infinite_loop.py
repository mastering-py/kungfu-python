# A while loop becomes infinite loop if a condition never becomes False

iLoop = 0

while iLoop < 5:
    print(iLoop)

print('-' * 100)
"""
Sample 1 (Other: Infinite loop) notes:
- # Without the increment statement, the iteration is always on 0 and it will continue forever
"""