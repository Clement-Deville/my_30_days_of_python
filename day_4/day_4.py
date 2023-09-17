#1

str = ' '.join(['Thirty', 'Days', 'Of', 'Python'])
print(str)

#2

str = ' '.join(['Coding', 'For' , 'All'])
print(str)

#3

company = 'Coding For All'

#4

print(company)

#5

print(len(company))

#6

print(company.upper())

#7

print(company.lower())

#8

print(company.title())

#9

print(company[0:6])

#10

print(company.find('Coding') != -1)

#11

print('Coding For All'.replace('Coding', 'Python'))

#12

print('Python for Everyone'.replace('Everyone', 'All'))

#13

print('Coding For All'.split())

#14

print('Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'.split(','))

#15

print('Coding For All'[0])

#16

print('Coding For All'[-1])

#17

print('Coding For All'[9])

#18

strs = 'Python For Everyone'.split()
print(strs[0][0], strs[1][0], strs[2][0], sep='')

#19

strs = 'Coding For All'.split()
print(strs[0][0], strs[1][0], strs[2][0], sep='')

#20 

print('Coding For All'.index('C'))

#21

print('Coding For All'.index('F'))

#22

print('Coding For All People'.rindex('l'))

#23

print('You cannot end a sentence with because because because is a conjunction'.find('because'))

#24

print('You cannot end a sentence with because because because is a conjunction'.rfind('because'))

#25
sentance = 'You cannot end a sentence with because because because is a conjunction'

print(sentance.replace('because because because', ''))

#26

print('You cannot end a sentence with because because because is a conjunction'.find('because'))

#27

print('You cannot end a sentence with because because because is a conjunction'.replace('because because because', ''))

#28

print('Coding for all'.startswith('Coding'))

#29

print('Coding for all'.endswith('Coding'))

#30

print('  Coding For All      '.strip('  '))

#31

#The second one, the 1st is invaldid because it starts with a number.

#32

print(' '.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))

#33

print(''''I am enjoying this challenge.
I just wonder what is next.'''.split('\n'))

#34

print('Name\tAge\tCountry\tCity\nClement\t25\tFrance\tParis')

#35

radius = 10
area = 3.14 * radius ** 2
result = 'radius = {}\narea = 3.14 * radius ** 2\nThe area of a circle with radius {} is {} meters square.'.format(radius, radius, int(area))
print(result)

#36

a, b = 8, 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, (a / b)))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))