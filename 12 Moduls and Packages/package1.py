from Geometrics.circle_area import phi, circle
from Geometrics.rectangle_area import rectangle

print('----- Circle Area -----')
print('Pi:', phi)
radius = int(input('Input radius of the circle: '))
print(f'Area of circle is: {circle(radius)}')

print()

print('----- Rectangle Area -----')
length = int(input('Input length of the rectangle: '))
width = int(input('Input width of the rectangle: '))
print(f'Area of rectangle is: {rectangle(length, width)}')
