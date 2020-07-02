#List is a collection which is ordered and changeable. Allows duplicate members.

# 1. Create list
myList = [10, 1, 'dua', 200, 4.5, True, 'Hello World']
print(myList)
print()

# 2. Access items and slicing
myList = [10, 1, 'dua', 200, 4.5, True, 'Hello World']
"""
               0  1    2     3    4    5          6       etc
            ----------------------------------------------
    myList = [10, 1, 'dua', 200, 4.5, True, 'Hello World']
            ----------------------------------------------
        etc   -7  -6    -5   -4   -3    -2       -1

"""
print(myList[0]) # using index to access the list items. the index is start from 0
print(myList[0:5]) # by a colon, get the characters start from position 0 to position 5 (position 5 not included)
print(myList[1:6]) # the last character is space
print(myList[-4]) # negative indexes is start from -1
print(myList[-5:-3]) # get the characters start from position -5 to position -3 (position -3 not included)
print(myList[4:]) # get the characters start from position 4 to the last character
print(myList[:4]) # get the characters start from the first character to position 4 (position 4 not included)
print(myList[-1:]) # get the characters start from position -1 to the last character
print(myList[:-1]) # get the characters start from the first character to position -1 (position -1 not included)
print(myList[-5:11]) # get the characters start from position -5 to the position 11 (etc and not included)
print(myList[1:-2]) # # get the characters start from position 1 to the position -2 (position -2 not included)
print()

# 3. Change item value
myList = [10, 1, 'dua', 200, 4.5, True, 'Hello World']
myList[5] = False
print(myList)
myList[1:5] = [2, 'tiga', 67, 7.9]
print(myList)
myList[4:5] = ['saddam']
print()

# 4. Adding list
# a. Using operator
myList1 = [10, 1, 'dua', 200, 4.5, True, 'Hello World']
myList2 = ['tiga', 67, 7.9, False]
totalList = myList1 + myList2
print(totalList)
# b. Using index
myList3 = [1, 2, 3]
"""
               0  1  2  etc
            ------------
    myList3 = [1, 2, 3]
            ------------
        etc   -3 -2 -1
"""
# myList3[3] = ['saddam'] # using this to add last item will be error
myList3[3:] = ['saddam'] # last
# print(myList3)
# myList3[:0] = ['rahmat'] # first
# print(myList3)
# myList3[2:2] = ['fuad'] # third
print(myList3)
print()

# 5. Removing items
myList = [10, 1, 'dua', 200, 4.5, True, 'Hello World']
# myList[3] = [] # we can't remove the item by using this
myList[:1] = []
print(myList)
myList[1:3] = []
print(myList)
# myList[2:2] = [] # we can't remove the item by using this
print(myList)
print()

# 6. Multidimensional list and access items
data1 = [1, 2, 3]
data2 = [4, 5]
x = [data1, data2]
"""
         0         1    <----- rows
    --------------------     
    [[1, 2, 3], [4, 5]]
    --------------------
      0  1  2    0  1   
      ^
      |
      |
     cols 
                    
"""
print(x)
print(x[0])
print(x[0][2])
print(x[1])
print(x[1][0])
print()

#7. Operator in list
# addition
add1 = [10, 'dua', 200, 'Hello World']
add2 = [1, 4.5, True]
addTotal = add1 + add2
print(addTotal)

# multiplication
mul = [1, 4.5, True] * 3
print(mul)

# in, not in
membership = [10, 'dua', 200, 'Hello World']
print('Hello World' in membership)
print(10 not in membership)
print()

#8. List reference
# changes made in z, will automatically also be made in data
data = [10, 'dua', 200, 'Hello World']
# z = data
z = data[:] #with colon mark, z will not be a reference to data
z[2] = 8
print(data)
print(z)
