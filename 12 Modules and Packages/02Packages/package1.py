# Sample 1 Access package using import
# Type 1 Import multiple modules in package
# import geometrics.circle_area, geometrics.rectangle_area
#
# print('----- Circle Area -----')
# print(geometrics.circle_area.pi)
# radius = int(input('Input radius of the circle: '))
# print(f'Area of circle is: {geometrics.circle_area.circle(radius)}')
#
# print()
#
# print('----- Rectangle Area -----')
# length = int(input('Input length of the rectangle: '))
# width = int(input('Input width of the rectangle: '))
# print(f'Area of rectangle is: {geometrics.rectangle_area.rectangle(length, width)}')

# Type 2 Using aliases to aliasing modules
# import geometrics.circle_area as ca, geometrics.rectangle_area as ra
#
# print('----- Circle Area -----')
# print(ca.pi)
# radius = int(input('Input radius of the circle: '))
# print(f'Area of circle is: {ca.circle(radius)}')
#
# print()
#
# print('----- Rectangle Area -----')
# length = int(input('Input length of the rectangle: '))
# width = int(input('Input width of the rectangle: '))
# print(f'Area of rectangle is: {ra.rectangle(length, width)}')

# Sample 2 Access package using from
# Tyoe 1 Using from (packages) with import specific modules
# from geometrics import circle_area, rectangle_area
#
# print('----- Circle Area -----')
# print('Pi:', circle_area.pi)
# radius = int(input('Input radius of the circle: '))
# print(f'Area of circle is: {circle_area.circle(radius)}')
#
# print()
#
# print('----- Rectangle Area -----')
# length = int(input('Input length of the rectangle: '))
# width = int(input('Input width of the rectangle: '))
# print(f'Area of rectangle is: {rectangle_area.rectangle(length, width)}')

# Type 2 Using from (packages.modules) with import specific attributes
from geometrics.circle_area import pi, circle
from geometrics.rectangle_area import rectangle

print('----- Circle Area -----')
print('Pi:', pi)
radius = int(input('Input radius of the circle: '))
print(f'Area of circle is: {circle(radius)}')

print()

print('----- Rectangle Area -----')
length = int(input('Input length of the rectangle: '))
width = int(input('Input width of the rectangle: '))
print(f'Area of rectangle is: {rectangle(length, width)}')
