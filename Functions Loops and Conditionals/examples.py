# # SIMPLE FUNCTIONS

# # length of a string
# len('Jurre')  # 5

# # writing your own functions

# # defining a function with name double and input variable x


# def double(x):
#     # do calculation
#     double_x = x * 2
#     # return answer
#     return double_x


# double(4)
# # answer 8

# # initials


# def initials(name):
#     first = name[0].upper()
#     last = name[name.find(' ')+1].upper()
#     return f'{first}. {last}.'


# initials_jurre = initials('Jurre Zwaan')
# print(initials_jurre)

# # FOR LOOPS

# names = ['Bob', 'Shaun', 'Preeti', 'Jeff']
# for name in names:
#     print(f'Hello, {name}!')

# # ITERABLES

# question = 'How many roads must one walk down?'
# # for every char in question print that character
# for c in question:
#     print(c)

# # RANGE

# for i in range(10):
#     print(i)

# list(range(10))

# # BREAK

# print('We have a long road ahead.')
# for i in range(1000):
#     print(i)
#     if i == 10:
#         break
#     print('Almost there...')
# print("That wasn't so bad after all.")

# # BREAK AND CONTINUE

# print('We have a long road ahead.')
# for i in range(1000):
#     if i % 2 == 0:
#         print(i)
#         continue
#     print('Almost there...')
# print("That wasn't half bad.")


list_a = ['b', 'd', 'f', 'e', 'h', 'q', 'i']
list_b = ['b', 'd', 'f', 'e']

if list_b in list_a:
    print('waar')

# LIST COMPREHENSIONS

example_names = ['Anna Ansville', 'Bob Bobsville', 'Carla Carlsville']
# met for loop
example_last_names = []
for name in example_names:
    example_last_names.append(name.split(' ')[-1])
print(example_last_names)

# zelfde met list comprehesion

example_last_names = [n.split(' ')[-1] for n in example_names]
print(example_last_names)

# WHILE LOOP

# infinte loop
# while True:
#     print('Woop woop, an infinite loop.')

i = 10
while i > 0:
    print(i)
    i -= 1

# DICTONARIES

student_ages = {
    'bob': 10,
    'sharon': 9,
    'eli': 10,
    'preeti': 11
}

print(student_ages['bob'])
print(student_ages['eli'])

# SETS

# list zonder duplicates

numbers = [1, 1, 2, 3, 4]
uniques = set(numbers)
print(uniques)  # {1, 2, 3, 4}
second = {1, 4}
second.add(5)
print(second)
second.add(2)
print(second)
