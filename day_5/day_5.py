#1

empty_list = []
print(empty_list)

#2

list = [1, 2, 3, 4, 5, 6]
print(list)

#3

print(len(list))

#4

print(list[0], list[(int(len(list) / 2) - 1)], list[len(list)- 1])

#5

mixed_data_types = ['Clement', 25, 182, False, 'France']
print(mixed_data_types)

#6

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#7

print(it_companies)

#8

print(len(it_companies))

#9

print(it_companies[0], it_companies[(int(len(it_companies) / 2) - 1)], it_companies[len(it_companies)- 1])

#10

it_companies[4] = 'Starlink'
print(it_companies)

#11

it_companies.append('IT')
print(it_companies)

#12

it_companies.insert(((len(it_companies) // 2) - 1), 'IT')
print(it_companies)

#13

it_companies[1] = it_companies[1].upper()
print(it_companies)

#14

print('# '.join(it_companies))

#15

print('IT' in it_companies)

#16

it_companies.sort()
print(it_companies)

#17

it_companies.reverse()
print(it_companies)

#18

it_companies_copy = it_companies.copy()
del it_companies_copy[0:3]
print(it_companies_copy)

#19

it_companies_copy = it_companies.copy()
del it_companies_copy[-3:]
print(it_companies_copy)

#20

it_companies_copy = it_companies.copy()
del it_companies_copy[(len(it_companies_copy) // 2) - 1]
print(it_companies_copy)

#21

it_companies_copy = it_companies.copy()
it_companies_copy.remove('IT')
print(it_companies_copy)

#22

it_companies_copy = it_companies.copy()
first_it = it_companies_copy.index('IT')
last_it = it_companies_copy[::-1].index('IT')
del it_companies_copy[first_it + 1: last_it]

#23

del it_companies_copy[last_it]
print(it_companies_copy)

#24

it_companies_copy.clear()

#25

del it_companies_copy

#26

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)

#27

full_stack = front_end.copy()
index = full_stack.index('Redux') + 1
full_stack.insert(index, 'SQL')
full_stack.insert(index, 'Python')
print(full_stack)