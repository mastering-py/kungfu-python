"""
Default Arguments / Default Parameter Value Arguments:
Allow us to provide defaults for corresponding formal arguments in the function definition. Python
uses these defaults if corresponding actual arguments are not passed in the function call.
"""

# Sample 1 (Single argument)
def args(a = 10):
    print(f'This is number {a}')


args()  # If we call the function without argument, it uses the default parameter values
args(2)

print('-' * 100)

# Sample 2 (Many arguments)
def args(a, b = 'Morning'):
    print(f'Hello Mr. {a}. Good {b}!')


args('Rahmat')  # a = 'Rahmat'. If the b argument is not set, the default parameter given in the parameter will be used
args('Saddam', 'Evening')
args(b = 'Afternoon', a = 'fuad')  # the arguments set by keywords

# Sample 3 (Invalid default parameter value)
# def args(a = 'saddam', b):
# def args(a = 'saddam', b, c = 'rahmat'):
# def args(a, b = 'saddam', c):
