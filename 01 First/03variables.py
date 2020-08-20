# Variable is using to store some data

# 1. Assign value to variable
# Valid
data = 'This is my data'
Data = 'This is my data'
_data = 'This is my data'
my_data = 'This is my data' # Snake case
myData = 'This is my data' # Camel case

# Invalid
"""
1mydata = 'This is my data'
my-data = 'This is my data'
my data = 'This is my data'
"""

# 2. Output the variables
print(data)

print('-' * 100)

# 3. Variable names are case sensitive
aku = 'This is my data 1'
Aku = 'This is my data 2'

print(aku)
print(Aku)

print('-' * 100)

# 4. Swap values of variables
a = 1
b = 2

a, b = b, a

print(a)
print(b)

c, d = 'satu', 'dua'

print(c)
print(d)

e = 'tiga'
f = e

print(f)