# Sample 1
class Heroes:
    # default attributes
    name = 'name'
    power = 'max'
    health = 'max'

    def skill(self, value):
        print(f'Attack: {value}')
        print(f'Defence: {value}')
        print(f'Speed: {value}')

# Create an object named superman
print('About Hero')
superman = Heroes()
superman.name = 'Superman'
superman.power = 100
superman.health = 100

print(f'Name: {superman.name}')
print(f'Power: {superman.power}')
print(f'Health: {superman.health}')

print()

# Methods
print('Skill')
superman.skill(100)