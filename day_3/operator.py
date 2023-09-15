age = 25
height = 1.83
comp = 5 + 3j

#4 Triangle script

base = float(input('Enter base: '))
height = float(input('Enter height: '))
area = int(0.5 * base * height)
print('The area of the triangle is: ', area)

#we could have use others ways to do it but here we learned that you cannot operate on data types that are different, as float and int

#5 Triangle script 2

a = int(input('Enter side a: '))
b = int(input('Enter side b: '))
c = int(input('Enter side c: '))
print('The perimeter of the triangle is ', (a + b + c))

#6 Rectangle script

length = int(input('Enter length: '))
width = int(input('Enter width: '))
print('The area of the rectancle is: ', (length * width), 'and his perimeter is: ', (2 * (length + width)))

#7 Circle script

radius = float(input('Enter radius :'))
print('The area of the circle is: ', (3.14 * (radius**2)))
print('The circumference of the circle is: ', (2 * 3.14 * radius))

#8

print('Slope = 2')
print('x-intercept = -2')
print('y-intercept = 1')

#9

slope = (10 - 2)/(6 - 2)

from math import *

eucli = (sqrt((10 - 2) ** 2 + (6 - 2) ** 2))

print('Slope is : ', slope)
print('Euclidian distance is : ', eucli)

#10 Compare

if slope < 2 :
    print('Slope of ex 8 is bigger')
elif slope == 2 :
    print('Slopes are equals')
else :
    print('Slope of ex 9 is bigger')
    
#11 

x = -30
while (x < 30) : 
    if (x**2 + (x * 6) + 9 == 0) :
        print('y = 0 for x = ', x)
    x += 1

#12

if len('dragon') == len('python') :
    print('Lengths are equals')
elif len('dragon') < len('python') :
    print('dragon is shorter')
else :
    print('python is shorter')

#13

if ('on' in 'python') and ('on' in 'dragon') :
    print('Sequence is in both words')
else :
    print('Sequence is not in both words')
    
#14

if ('jargon' in 'I hope this course is not full of jargon.') :
    print('Word is in setence')
else :
    print('Word is not in setence')

#15

print('on' not in ('python' and 'dragon'))

#16

print(str(float(len('python'))))

#17
number = 2
print(number % 2 == 0)

#18

print(7//3 == int(2.7))

#19

print(type('10') == type(10))

#20

print(int(9.8) == 10)

#21 Pay script

hours = int(input('Enter hours: '))
rate = int(input('Enter rate per hour: '))
print('Your weekly earning is: ', (hours * rate))

#22 Life script

years = int(input('Enter number of years you have lived: '))
print('You have lived for ', (years * 31536000), 'seconds.')

#23 Matrice script

print('1 1 1 1 1\n2 1 2 4 8\n3 1 3 9 27\n4 1 4 16 64\n5 1 5 25 125')