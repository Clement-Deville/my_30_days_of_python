#1

dog = {}

#2

dog = {'name':'peanuts', 'breed':'batard', 'legs':'medium', 'age':4}
print(dog)

#3

student = {'first_name':'Louis', 'last_name':'Melon', 'gender':'man', 'maried':True, 
           'skills':['cooking','basketball', 'japenese'], 'country':'New York', 'address':{'postal':2000, 'Street':'1 of 1st Avenue'}}
print(student)

#4

print(len(student))

#5

print(student['skills'])
print(type(student['skills']))

#6

student['skills'].append('judo')
student['skills'].append('sex')
print(student['skills'])

#7

print(student.keys())

#8

print(student.values())

#9

print(student.items())

#10

student.pop('maried')
print(student)

#11

del dog