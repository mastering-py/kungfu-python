#  Function can be used as return value in other functions in Python.

# Sample 1
def user1():
    print('Your super username is', admin.__name__)

def admin(func):  # func == user1
    print('You access as', func.__name__)
    return func  # -> user1

login = admin(user1)  # -> admin
login()

print('-' * 100)

# Sample 2
def sq(func, x):  # f == func. 2 == x
    y = x ** 2  # y = 4
    return func(y)  # -> f()

def f(x):  # y == x == 4
    return x ** 2  # = 16

main3 = sq(f, 2)  # -> sq()
print(main3)