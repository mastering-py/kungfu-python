# With the continue statement we can stop the current iteration of the loop, and continue with the next

# Sample 1
for i in range(1, 10):
    if i == 6:
        print(f'Number {i} founded')
        continue  # continue / jump to for and change to 7
    print('Current number:', i)  # on 6, this statement will not execute
else:  # this is part of for (not if). It will execute when the loop is over
    print('End of loop')

print('-' * 100)

# Sample 2: Using list as iterable
idFoods1 = ['bakso', 'nasi padang', 'soto']

for j in idFoods1:
    if j == 'nasi padang':
        continue  # jump to next for statement and don't print nasi padang
    print(j)

print('-' * 100)

# Sample 3: Total of space in a words
words1 = input('Input some words: ')
print(f'Your words is: \n"{words1}"')
count1 = 0

for k in range(len(words1)):
    if words1[k] !=' ':
        continue  # all characters jump to next for statement except ' '
    count1 += 1

print(f'\nThere are {count1} space character in the words')

print('-' * 100)

# Sample 4: Combine while boolean with break and continue
while True:
    press1 = input('Hello. Press Y to repeat or N to Stop: ')

    if press1 == 'N' or press1 == 'n':
        break
    else:
        continue
