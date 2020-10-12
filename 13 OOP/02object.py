# Instantiate Objects / Instances in Python

# Sample 1
class Heroes1:
    pass


# Create / instantiate an objects
a = Heroes1()
b = Heroes1()

print(a == b)  # a and b is different because they represent two distinct objects in memory
print(a)
print(b)

print('-' * 100)

# Sample 2
class Heroes2:
    # Without any attributes inside of the class
    pass


# Instantiate an object named superman
superman = Heroes2()

# Create attributes outside of the class by object named superman
superman.name = 'Clark Kent'
superman.power = 100
superman.health = 100

# Access the superman attributes
print(superman.name)
print(superman.power)
print(superman.health)

print('-' * 100)

# Sample 3
class Heroes3:
    # Default attributes inside of the class (class variables)
    name = 'Bruce'
    power = '50'
    health = '50'


# Instantiate an object named batman
batman = Heroes3()

# Access the class variables by class
print(Heroes3.name)
print(Heroes3.power)
print(Heroes3.health)
print()

# Access the class variables by object
print(batman.name)  # All objects of Heroes3 class can access into the class variables. It is because the class variables accessibility is public
print(batman.power)
print(batman.health)

print()

# Changing the class variables values
batman.name = 'Bruce Wayne'
batman.power = 90
batman.health = 99

print(batman.name)
print(batman.power)
print(batman.health)
