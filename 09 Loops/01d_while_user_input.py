# We can set the variable counter by user input

# Sample 1
word1 = input('Set some words: ')
num1 = 0

print('Your word is sets in 5 times:')
while num1 < 5:
    print(f'{num1 + 1}. {word1}')
    num1 += 1

print('-' * 100)

# Sample 2
word2 = input('Set some words: ')
rep1 = int(input('Hom much time do you want to repeat?: '))
num2 = 0

print(f"Your word '{word2}' is sets in {rep1} times:")
while num2 < rep1:
    print(f'{num2 + 1}. {word2}')
    num2 += 1

print('-' * 100)