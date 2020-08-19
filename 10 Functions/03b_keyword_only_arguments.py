"""
Keyword Arguments:
Keyword arguments are passed by it’s name instead of their position as opposed to positional arguments in the function
call. As a result we don’t have to mind about position of arguments when calling a function.
"""
def args(a, b):
    print(f'My name is {a}. I am {b} years old')


args(a = 'Rahmat', b = 23)
args(b = 31, a = 'saddam')  # Since we are passing arguments by their names/keywords order or position doesn’t matter
args('fuad', b = 20)  # We can combine both positional and keyword arguments. but positional arguments should follows by keyword arguments

# invalid keyword only arguments
# args(50, 'mike')  # the position is incorrect
# args('saddam')  # the count between arguments and parameters don’t match
# args(b = 18, 'fitri')  # If we break the rule and pass arguments in such a way that keyword arguments follows by positional arguments which is a syntax error.
