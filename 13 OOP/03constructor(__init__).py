# All classes have a function called __init__(), which is always executed when the class is being initiated.

# Sample 1: Object == self
class Heroes1:
    def __init__(self):  # __init__() initializes each new object of the class
        print('Hello Superman')
        print(self)  # superman == self. The memory address of self is same with superman. It means the self argument is superman object.


superman = Heroes1()
print(superman)

print('-' * 100)

# Sample 2: Using for loop to access class variables
class Heroes2:
    def __init__(self, name, powerAttack, healthEnergy):
        self.name = name
        self.power = powerAttack
        self.health = healthEnergy


superman = Heroes2('Clark Kent', 100, 100)
batman = Heroes2('Bruce Wayne', 98, 100)

print('--- Superman Profile ---')
print(f'Name: {superman.name}')
print(f'Power: {superman.power}')
print(f'Health: {superman.health}')
print(superman.__dict__)
print()

# Using for, __dict__ and items() to access superman by its component
for i, j in superman.__dict__.items():
    print(f'{i.capitalize()} : {j}')

print()

print('--- Batman Profile ---')
print(f'Name: {batman.name}')
print(f'Power: {batman.power}')
print(f'Health: {batman.health}')
print(batman.__dict__)
print()

# Using for, __dict__ and items() to access batman by its component
for k, m in batman.__dict__.items():
    print(f'{k.capitalize()} : {m}')

print('-' * 100)

# Sample 3: Using list and nested loop to access class variables
class Heroes3:
    # constructor
    def __init__(self, name, powerEnergy, healthEnergy):
        self.name = name
        self.power = powerEnergy
        self.health = healthEnergy


sman = Heroes3('Superman', 100, 100)
bman = Heroes3('Batman', 98, 100)
cman = Heroes3('Catwoman', 90, 91)
rbn = Heroes3('Robin', 95, 95)

list1 = [sman, bman, cman, rbn]

for x in list1:
    for y, z in x.__dict__.items():
        print(f'{y.capitalize()} : {z}')
    print('-' * 10)
