# Sample 1: Using __dict__ built-in attribute to view class and object component
class Heroes1():
    # Class variables
    name = 'Bruce Wayne'
    power = '90'
    health = '100'

    def __init__(self, name, powerAttack, healthEnergy):
        # Object variables
        self.name = name
        self.power = powerAttack
        self.health = healthEnergy


superman = Heroes1('Clark Kent', 100, 100)

print('Class variables:')
print(Heroes1.__dict__)

print()
print('Object variables:')
print(superman.__dict__)

print('-' * 100)

# Sample 2: Operating between class and object variables
class Heroes2():
    # Class variables
    value = 0

    def __init__(self, name):
        # Object variables
        self.name = name
        Heroes2.value += 1


superman = Heroes2('Clark Kent')
print(f'{Heroes2.value}. Hero name: {superman.name}')

batman = Heroes2('Bruce Wayne')
print(f'{Heroes2.value}. Hero name: {batman.name}')

catwoman = Heroes2('Selina Kyle')
print(f'{Heroes2.value}. Hero name: {catwoman.name}')

