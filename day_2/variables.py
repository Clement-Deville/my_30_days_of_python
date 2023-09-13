#Day 2: 30 Days of python programming

#declaring variables

first_name = 'Clement'
last_name = 'DEVILLE'
full_name = first_name + ' ' + last_name # or full_name = 'Clement DEVILLE'
country = 'France'
city = 'Paris'
age = 25
year = 2023
is_married = False
is_true = True
is_light = True

#Multiple declaration in one line

gender, has_dog, language = 'M', True, {'French', 'English', 'Spanish', 'Japenese'}

#   LEVEL 2

#1 Checking data types

print('first_name: ', type(first_name))
print('last_name: ', type(last_name))
print('full_name: ', type(full_name))
print('country: ', type(country))
print('city: ', type(city))
print('age: ', type(age))
print('year: ', type(year))
print('is_married: ', type(is_married))
print('is_true: ', type(is_true))
print('is_light: ', type(is_light))
print('gender: ', type(gender))
print('has_dog: ', type(has_dog))
print('language: ', type(language))

#2 Length of first_name

print(len(first_name))

#3 Compare it with last name

print(len(last_name))

#4 Some Maths

num_one = 5
num_two = 4
total = num_one + num_two
print('total : ', total)
diff = num_one - num_two
print('diff : ', diff)
product = num_one * num_two
print('product : ', product)
division = num_one / num_two
print('division : ', division)
remainder = num_two % num_one
print('remainder : ', remainder)
exp = num_one ** num_two
print('exp : ', exp)
floor_division = num_one // num_two
print('floor_division : ', floor_division)

#5 radius 

from math import * #importing pi

radius = 30
print('radius : ', radius)

area_of_circle = pi * (radius)**2
print('area_of_circle : ', area_of_circle)

circum_of_cercle = 2 * pi * radius
print('circum_of_cercle : ', circum_of_cercle)

#user input

radius = int(input('Write a radius to calculate an area of a cercel: '))
area_of_circle = pi * (radius)**2
print('Area : ', area_of_circle)

#6 Multiples variables as user input

first_name = input('first_name: ')
last_name = input('last_name: ')
full_name = input('full_name: ')
country = input('country: ')
city = input('city: ')
age = int(input('age: '))

print('first_name: ', first_name)
print('last_name: ', last_name)
print('full_name: ', full_name)
print('country: ', country)
print('city: ', city)
print('age: ', age)

#7 Help command for keywords

help('keywords')