# Sample 1
# Without iterable
# Type 1
for i in range(5):  # From 0 to 4 (5 not including)
    print(i)

print('-' * 100)

# Type 2
for j in range(5, 10):  # Start from 5 to 9 (10 not including)
    print(j)

print('-' * 100)

# Type 3
for k in range(1, 10, 2):  # Increment the sequence with 2
    print(k)

print('-' * 100)

# Sample 2
# With iterable
idFoods1 = ['bakso', 'nasi padang', 'soto', 'coto makassar']
lenidF1 = len(idFoods1)  # using len() function to determine how many items a list has

for m in range(lenidF1):
    print(idFoods1[m])
