# A nested loop is a loop inside a loop.

# Sample 1
# Using default for
idFoods = [['bakso', 'nasi padang'], ['soto', 'coto makassar'], ['gule', 'rendang']]

for i in idFoods: # Layer 1
    print(i)
    for j in i: # Layer 2
        print(j)

print('-' * 100)

# Sample 2
enak1 = ['bakso', 'nasi padang']
enak2 = ['soto', 'coto makassar']
enak3 = ['gule', 'rendang']

idFoods2 = [enak1, enak2, enak3]

print(idFoods2)

for k in idFoods2:
    for m in k:
        print(m)

print('-' * 100)

# Sample 3
# Using for in range() function
idFoods3 = [['bakso', 'nasi padang'], ['soto', 'coto makassar'], ['gule', 'rendang', 'salome', 'cilok']]

for m in range(len(idFoods3)):
    print(f"{'-' * 5} Row {m + 1} {'-' * 5}")
    for n in range(len(idFoods3[m])):
        print(f"Column {n + 1}: {idFoods3[m][n]}")
