# Tuple is a collection which is ordered and unchangeable. Once a tuple is created, we cannot change its values. In Python tuples are written with round brackets.

# 1. Create tuple
myTuple1 = (10, 1, 'dua', 200, 4.5, True, 'Hello World')
myTuple2 = 10, 1, 'dua', 200, 4.5, True, 'Hello World' # a tuple that consists of comma-separated values without brackets. We can create a tuple without brackets or parenthesis
myTuple4 = ('tuple',) # to create a tuple with only one item, we have to add a comma after the item, otherwise Python will not recognize it as a tuple.
print(myTuple1)
print(type(myTuple1))
print(myTuple2)
print(type(myTuple2))
print(myTuple4)
print(type(myTuple4))
print()

# 2. Access elements (items) and slicing
myTuple4 = [10, 1, 'dua', 200, 4.5, True, 'Hello World']
"""
               0  1    2     3    4    5          6       etc
            ----------------------------------------------
 myTuple4 = [10, 1, 'dua', 200, 4.5, True, 'Hello World']
            ----------------------------------------------
        etc   -7  -6    -5   -4   -3    -2       -1

"""
# We can access tuple items by referring to the index number, inside square brackets
print(myTuple4[0])  # using index to access the list items. the index is start from 0
print(myTuple4[0:5])  # by a colon, get the characters start from position 0 to position 5 (position 5 not included)
print(myTuple4[1:6])  # the last character is space
print(myTuple4[-4])  # negative indexes is start from -1
print(myTuple4[-5:-3])  # get the characters start from position -5 to position -3 (get position -4. position -3 not included)
print(myTuple4[4:])  # get the characters start from position 4 to the last character
print(myTuple4[:4])  # get the characters start from the first character to position 4 (position 4 not included)
print(myTuple4[-1:])  # get the characters start from position -1 to the last character
print(myTuple4[:-1])  # get the characters start from the first character to position -1 (position -1 not included)
print(myTuple4[-5:11])  # get the characters start from position -5 to the position 11 (etc and not included)
print(myTuple4[1:-2])   # get the characters start from position 1 to the position -2 (position -2 not included)
print()

# 3. Removing items
# We can't remove the items. But we can delete the tuple completely
# We also can't remove the items using built-in methods
myTuple5= (10, 1, 'dua', 200, 4.5, True, 'Hello World')
# del myTuple5(3)
# del myTuple5[1:3]
# print(myTuple5)
del myTuple5
# print(myTuple5) # this will cause an error because we have succsesfully deleted "myTuple4"
# myTuple5.remove('dua')
# myTuple5.pop(2)
# print(myTuple5)
print()

# 4. Operator in tuple
# addition
add1 = (10, 'dua', 200, 'Hello World')
add2 = (1, 4.5, True)
addTotal = add1 + add2
print(addTotal)

# multiplication
mul = (1, 4.5, True) * 3
print(mul)

# in, not in
membership = (10, 'dua', 200, 'Hello World')
print('Hello World' in membership)
print(10 not in membership)
print()



















# # 2. Access elements (items) and slicing
# myTuple4 = [10, 1, 'dua', 200, 4.5, True, 'Hello World']
# """
#                0  1    2     3    4    5          6       etc
#             ----------------------------------------------
#     myList = [10, 1, 'dua', 200, 4.5, True, 'Hello World']
#             ----------------------------------------------
#         etc   -7  -6    -5   -4   -3    -2       -1
#
# """
# print(myTuple4[0])  # using index to access the list items. the index is start from 0
# print(myTuple4[0:5])  # by a colon, get the characters start from position 0 to position 5 (position 5 not included)
# print(myTuple4[1:6])  # the last character is space
# print(myTuple4[-4])  # negative indexes is start from -1
# print(myTuple4[-5:-3])  # get the characters start from position -5 to position -3 (get position -4. position -3 not included)
# print(myTuple4[4:])  # get the characters start from position 4 to the last character
# print(myTuple4[:4])  # get the characters start from the first character to position 4 (position 4 not included)
# print(myTuple4[-1:])  # get the characters start from position -1 to the last character
# print(myTuple4[:-1])  # get the characters start from the first character to position -1 (position -1 not included)
# print(myTuple4[-5:11])  # get the characters start from position -5 to the position 11 (etc and not included)
# print(myTuple4[1:-2])   # get the characters start from position 1 to the position -2 (position -2 not included)
# print()
#
# # 3. Change items value
# myList3 = [10, 1, 'dua', 200, 4.5, True, 'Hello World']
# myList3[5] = False
# print(myList3)
# myList3[1:5] = [2, 'tiga', 67, 7.9]
# print(myList3)
# myList3[4:5] = ['saddam']
# print()
#
# # 4. Adding list
# # a. Using addition operator
# myList4 = [10, 1, 'dua', 200, 4.5, True, 'Hello World']
# myList5 = ['tiga', 67, 7.9, False]
# totalList = myList4 + myList5
# print(totalList)
#
# # b. Using index
# myList6 = [1, 2, 3]
# """
#                0  1  2  etc
#             ------------
#     myList3 = [1, 2, 3]
#             ------------
#         etc   -3 -2 -1
# """
# # myList6[3] = ['saddam'] # using this to add last item will be error
# # myList6[3:] = ['saddam']  # last
# # print(myList6)
# # myList6[:0] = ['rahmat'] # first
# # print(myList6)
# myList6[2:2] = ['fuad'] # third
# print(myList6)
# print()
#
# # 5. Removing items
# # a. Using empty list
# myTuple4 = [10, 1, 'dua', 200, 4.5, True, 'Hello World']
# # myTuple4[3] = [] # we can't remove the item by using this
# myTuple4[:1] = []
# print(myTuple4)
# myTuple4[1:3] = []
# print(myTuple4)
# # myTuple4[2:2] = [] # we can't remove the item by using this
# # print(myTuple4)
#
# # b. Using del keyword
# # we can also remove items using del keyword
# myTuple4 = [10, 1, 'dua', 200, 4.5, True, 'Hello World']
# del myTuple4[3] # remove index 3 item
# print(myTuple4)
# del myTuple4[1:3]
# print(myTuple4)
# # del myTuple4 # the del keyword can also delete the list completely
# # print(myTuple4) # # this will cause an error because you have succsesfully deleted "myTuple4".
# print()
#
# # 6. Multidimensional list and access items
# data1 = [1, 2, 3]
# data2 = [4, 5]
# x = [data1, data2]
# """
#          0         1    <----- rows
#     --------------------
#     [[1, 2, 3], [4, 5]]
#     --------------------
#       0  1  2    0  1
#       ^
#       |
#       |
#      cols
#
# """
# print(x)
# print(x[0])
# print(x[0][2])
# print(x[1])
# print(x[1][0])
# print()
#
# # 7. Operator in list
# # addition
# add1 = [10, 'dua', 200, 'Hello World']
# add2 = [1, 4.5, True]
# addTotal = add1 + add2
# print(addTotal)
#
# # multiplication
# mul = [1, 4.5, True] * 3
# print(mul)
#
# # in, not in
# membership = [10, 'dua', 200, 'Hello World']
# print('Hello World' in membership)
# print(10 not in membership)
# print()
#
# # 8. List reference
# data3 = [10, 'dua', 200, 'Hello World']
# z = data3 # z will be a reference to data3
# # z = data3[:]  # with colon mark, z will not be a reference to data3
# z[2] = 8 # changes made in z, will automatically also be made in data3
# print(data3)
# print(z)
