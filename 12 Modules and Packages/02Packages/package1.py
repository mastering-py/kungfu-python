# Sample 1
# from geometrics.circle_area import pi, circle
# from geometrics.rectangle_area import rectangle
#
# print('----- Circle Area -----')
# print('Pi:', pi)
# radius = int(input('Input radius of the circle: '))
# print(f'Area of circle is: {circle(radius)}')
#
# print()
#
# print('----- Rectangle Area -----')
# length = int(input('Input length of the rectangle: '))
# width = int(input('Input width of the rectangle: '))
# print(f'Area of rectangle is: {rectangle(length, width)}')

# Sample 2
from geometrics import circle_area, rectangle_area

print('----- Circle Area -----')
print('Pi:', circle_area.pi)
radius = int(input('Input radius of the circle: '))
print(f'Area of circle is: {circle_area.circle(radius)}')

print()

print('----- Rectangle Area -----')
length = int(input('Input length of the rectangle: '))
width = int(input('Input width of the rectangle: '))
print(f'Area of rectangle is: {rectangle_area.rectangle(length, width)}')