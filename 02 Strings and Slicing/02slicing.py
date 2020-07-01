# 2. Slicing in strings
text1 = 'Hello World'

"""
      0    1   2   3   4   5   6   7   8   9   10  etc
------------------------------------------------------
     |H|  |e| |l| |l| |o| | | |W| |o| |r| |l| |d|
------------------------------------------------------
etc  -11  -10  -9  -8  -7  -6  -5  -4  -3  -2  -1
"""

example1 = text1[0] # the index is start from 0
example2 = text1[0:5] # by a colon, get the characters start from position 0 to position 5 (position 5 not included)
example3 = text1[1:6] # the last character is space
example4 = text1[-4] # negative is start from -1
example5 = text1[-5:-3] # get the characters start from position -5 to position -3 (position -3 not included)
example6 = text1[4:] # get the characters start from position 4 to the last character
example7 = text1[:4] # get the characters start from the first character to position 4 (position 4 not included)
example8 = text1[-1:] # get the characters start from position -1 to the last character
example9 = text1[:-1] # get the characters start from the first character to position -1 (position -1 not included)
example10 = text1[-5:11] # get the characters start from position -5 to the position 11 (etc and not included)
example11 = text1[1:-2] # # get the characters start from position 1 to the position -2 (position -2 not included)
example12 = f'{text1[0:6]}Indonesia' # formatted string and slicing

print(example1)
print(example2)
print(example3)
print(example4)
print(example5)
print(example6)
print(example7)
print(example8)
print(example9)
print(example10)
print(example11)
print(example12)