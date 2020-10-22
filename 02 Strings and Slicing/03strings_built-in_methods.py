# Python has a set of built-in methods that you can use on strings

print('capitalize()')
# Converts the first character to upper case
text1 = 'my name is saddam'
print(text1.capitalize())
print()

print('casefold()')
# Converts string into lower case
text2 = 'MY NAME IS SADDAM'
print(text2.casefold())
print()

print('center()')
# Returns a centered string
text3 = 'My name is saddam'
print(text3.center(50))
print()

print('count()')
# Returns the number of times a specified value occurs in a string
text4 = 'my name is saddam, my father\'s name is bonda. my father is a mechanic'
print(text4.count('a'))
print(text4.count('my'))
print(text4.count('father'))
print(text4.count('my', 9, 30)) # from index 9 to index 30 in text4S
print()

print('find()')
# Searches the string for a specified value and returns the position of where it was found
text5 = 'My name is saddam'
print(text5.find('saddam'))
print()

print('format()')
# Formats specified values in a string
text6 = 'My name is {name}, i am {age} years old'
print(text6.format(name = 'saddam', age = '30'))
print()

print('index()')
# Searches the string for a specified value and returns the position of where it was found
text7 = 'My name is saddam'
print(text7.index('saddam'))
print()

print('lower()')
# Converts a string into lower case
text8 = 'MY NAME IS SADDAM'
print(text8.lower())
print()

print('upper()')
# Converts a string into upper case
text8 = 'my name is saddam'
print(text8.upper())
print()

print('join()')
# Joins the elements of an iterable to the end of the string
text9 = 'saddam', 'rahmat', 'fuad', 'fitri' # this is tuple
print(' -> '.join(text9))
print()

print('replace')
# Returns a string where a specified value is replaced with a specified value
text10 = 'My name is saddam'
print(text10.replace('saddam', 'adam'))
print()

print('center')
# The center() method will center align the string, using a specified character (space is default)
# as the fill character.
text11 = 'Saddam Husein'
print(text11.center(20, '-'))  # total of character include text11 string is 20
