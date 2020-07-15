# Elif statement that is used in Python when we need to choose between more than two alternatives

score = int(input('Input your passing grade (0 - 100): '))

if 80 <= score <= 100:
    print('You got A')
elif 70 <= score < 80:
    print('You got B')
elif 60 <= score < 70:
    print('You got C')
elif 50 <= score < 60:
    print('You got D, reexam')
elif score > 100:
    print('Enter the correct value')
else:
    print('Your passing grade is Unsatisfactory')