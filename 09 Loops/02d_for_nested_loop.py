# A nested loop is a loop inside a loop.

# Sample 1
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