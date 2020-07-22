# The sorted() function returns a sorted list of the specified iterable object

idFoods1 = [100, 43, 7, 200001, 1, 3, 588, 90, 3, 44, 58]

print(f"{'-' * 20} Before {'-' * 20}")
for i in idFoods1:
    print(i)

print(f"{'-' * 20} After {'-' * 20}")
for j in sorted(idFoods1):
    print(j)