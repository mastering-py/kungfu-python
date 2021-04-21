# Elif statement that is used in Python when we need to choose between more than two alternatives

# Sample 1
score = int(input('Input your passing grade (0 - 100): '))

if 80 <= score <= 100:
    print('You got A')
elif 70 <= score < 80:
    print('You got B')
elif 60 <= score < 70:
    print('You got C')
elif 50 <= score < 60:
    print('You got D, reexam')
elif score < 0 or score > 100:
    print('Enter the correct value')
else:
    print('Your passing grade is Unsatisfactory')

print('-' * 100)

# Sample 2
score2 = int(input('Input your other passing grade (0 - 100): '))
result = None

if score2 >= 80:
    result = 'You got A'
elif score2 >= 70:
    result = 'You got B'
elif score2 >= 60:
    result = 'You got C'
elif score2 >= 50:
    result = 'You got D, reexam'
else:
    result = 'Your passing grade is Unsatisfactory'

print(result)