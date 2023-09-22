##LEVEL 1

1

age = int(input('Enter your age: '))
if age < 18:
    print('You need', 18 - age, 'more years to learn to drive.')
else:
    print('You are old enough to learn to drive.')
    
#2
my_age = 24
your_age = int(input('Enter your age: '))
diff = my_age - your_age
year = 'years'
end = ''
if my_age == your_age:
    print('We got the same age!')
else:
    if abs(diff) == 1:
        year = 'year'
    if my_age - your_age < 0:
        end = 'older than me.'
    else:
        end = 'younger than me.'
    print('You are', abs(diff), year, end)
    
#3

numb_one = int(input('Enter number one: '))
numb_two = int(input('Enter number two: '))

if numb_one == numb_two:
    print(numb_one, 'is equal to', numb_two)
elif numb_one > numb_two:
    print(numb_one, 'is greater than', numb_two)
else:
     print(numb_two, 'is greater than', numb_one)
     
     
##LEVEL 2

#1

score = 89

if score >= 90 and score <= 100:
    print('A')
if score >= 70 and score <= 89:
    print('B')
if score >= 60 and score <= 69:
    print('C')
if score >= 50 and score <= 59:
    print('D')
if score >= 0 and score <= 49:
    print('F')
    
2

month = int(input('Enter a month as a number: '))

if month == 12 or (month >= 1 and month <= 2):
    print('It is Winter')
if month >= 3 and month <= 5:
    print('It is Spring')
if month >= 6 and month <= 8:
    print('It is Summer')
if month >= 9 and month <= 11:
    print('It is Autumn')

#3

fruits = ['banana', 'orange', 'mango', 'lemon']

fruit_add = input('Enter a fruit: ')

if fruit_add in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(fruit_add)
    print(fruits)

##LEVEL 3

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person:
    if len(person['skills']) % 2:
        print(person['skills'][len(person['skills']) // 2])
    else:
        print(person['skills'][len(person['skills']) // 2 - 1])

if 'skills' in person and 'Python' in person['skills']:
    print('Python')
    
if ('JavaScript' and 'React') in person['skills']:
    print('He is a front end developer')

if person['is_marred'] and person['country'] == 'Finland':
    print('%s %s lives in %s. He is married.' %(person['first_name'], person['last_name'], person['country']))