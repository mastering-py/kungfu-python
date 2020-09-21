class Heroes():
    # constructor
    def __init__(self, name, powerEnergy, healthEnergy):
        self.name = name
        self.power = powerEnergy
        self.health = healthEnergy

    def view_heroes(self):
        print('Name:', self.name)
        print('Power:', self.power)
        print('Health:', self.health)
        print('-' * 100)


sman = Heroes('Superman', 100, 100)
bman = Heroes('Batman', 98, 100)
cman = Heroes('Catwoman', 90, 91)
rbn = Heroes('Robin', 95, 95)

# view superman attributes
print(sman.name)
print(sman.power)
print(sman.health)

print()

# view all heroes attributes by manually
# sman.view_heroes()
# bman.view_heroes()
# cman.view_heroes()
# rbn.view_heroes()

# view all heroes attributes by for loop
list1 = [sman, bman, cman, rbn]

for i in list1:
    i.view_heroes()
