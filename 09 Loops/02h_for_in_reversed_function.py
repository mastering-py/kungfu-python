# The reversed() function returns a reversed iterator object

idFoods1 = ['bakso', 'nasi padang', 'soto', 'coto makassar']

print(f"{'-' * 20} Before {'-' * 20}")
for i in idFoods1:
    print(i)

print(f"{'-' * 20} After {'-' * 20}")
for j in reversed(idFoods1):
    print(j)