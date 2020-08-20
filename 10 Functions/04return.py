# To let a return value outside the function, use the return statement

# Sample 1 (Basics)
def main1():
    jumlah = 2 + 3
    return jumlah

# Type 1
print(main1())
# Type 2
a = main1()
print('Nilai a adalah', a)

print('-' * 100)

# Sample 2 (Argument)
def main2(a, b):
    jumlah = a + b
    return jumlah


print(main2(7, 1))
print(main2(5, 10))

val1 = main2(1, 2)
val2 = main2(3, 4)

print(main2(val1, val2))
val3 = main2(val1, val2)
print(f'{val1} + {val2} = {val3}')
print(val3 - 2)
print(main2(val3, 5))

print('-' * 100)

# Sample 3 (Argument & input)
def args3(a, b):
    jumlah = a + b
    return jumlah


def view3(one, two, three):
    print(f'{one} + {two} = {three}')


def main3():
    val1 = int(input('Input value 1: '))
    val2 = int(input('Input value 2: '))
    a = args3(val1, val2)
    view3(val1, val2, a)


main3()

print('-' * 100)

# Sample 4 (Return string)
# Type 1
def main4():
    # text4 = 'hello world'
    # return text4
    return 'hello world'


print(main4())

print('-' * 100)

# Type2
def main4(lang):
    if lang =='en':
        return 'Good morning'
    elif lang =='idn':
        return 'Selamat pagi'
    else:
        return 'Bojour'


en = main4('en')
idn = main4('idn')
fr = main4('fr')

list4 = [en, idn, fr]

for i in list4:
    print(i, 'Mr. Saddam')

print('-' * 100)

# Sample 5 (Return list)
def items():
    list5 = ['satu', 'dua', 'tiga', 'empat']
    return list5


def main():
    for i in items():
        print(i)


main()

print('-' * 100)

# Sample 6 (Return tuple)
def Tampilkan():
    return 1, 2, 3, 'wadi', 3, 2, 1  # we can let the return value using tuple


print(Tampilkan())
print(type(Tampilkan()))