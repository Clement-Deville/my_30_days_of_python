# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Level 1

#1

print(len(it_companies))

#2

it_companies.add('Twitter')

#3

it_companies.update(('OpenAI', 'Samsung'))

#4

it_companies.remove('Facebook')

#5

#Discard will not return an error if the item does not exist.

print(it_companies)

##Level 2

#1

C = A.union(B)
print(C)

#2

print(A.intersection(B))

#3

print(A.issubset(B))

#4

print(A.isdisjoint(B))

#5

A.update(B)
B.update(A)

#6

print(A.symmetric_difference(B))

#7

del A, B

##Level 3

#1

set_age = set(age)
print(len(set_age) < len(age))

#2

#A string is a list of character
#A list is collection of different data types ordered and modifiable
#A tupple is collection of different data types ordered and non-modifiable
#A set is collection of unique item non_ordered, un-indexed modifiable

#3

unique = set('I am a teacher and I love to inspire and teach people.'.split())
print('Unique words:', unique, '\nAnd number of unique wrods:', len(unique))
