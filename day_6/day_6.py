#Level 1

#1

empty_tuple = ()

#2

sisters = ('Camille', 'Eloise')
brothers = ('Marc', 'John')

#3

siblings = brothers + sisters

#4

print(len(siblings))

#5

family_members = siblings + ('Gerard', 'Alison')
print(family_members)

#Level 2 

#1

siblings, parents = family_members[0:4], family_members[4:]
print(siblings, parents)

#2

fruits = ('Orange', 'Lemon')
vegetables = ('Laitue', 'Oignon')
animal_products = ('Steak', 'Eggs', 'Milk')

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

#3

food_stuff_lt = list(food_stuff_tp)

#4

food_stuff_tp = food_stuff_lt[0:len(food_stuff_lt)//2] + food_stuff_lt[len(food_stuff_lt)//2 + 1:]
print(food_stuff_tp)

#5

print(food_stuff_lt[3:-3])

#6

del food_stuff_tp

#7

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)