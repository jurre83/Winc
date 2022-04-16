print(type(4))
print(type(3.14))
print(type('jurre'))

# PYTHON CASTING

x = int(5.6)
y = int(7)
z = int('8')

print(x, y, z)  # 5 7 8

x = float(5.6)
y = float(7)
z = float('8')

print(x, y, z)  # 5.6 7.0 8.0

x = str(5.6)
y = str(7)
z = str('8')

print(x, y, z)  # 5.6 7 8  (allemaal strings)


# ESCAPE SYMBOL

# \ is een escape symbool
print('Jurre\'s Guitars')
print('Jurre\'s \\Guitars')
#  unicodes voor characters
print('\u0127')
print('\u2133')
print('\u20ac')
print('N\{euro sign}')

# STRING OPERATIONS
print('Hello, ' + 'world!')
print('Jump! ' * 5)

# MEMBERSHIP OPERATIONS

sentence = 'We went out for dinner with with Anne, Samuel and Bob.'
print('Samuel' in sentence)  # True. Samuel is onderdeel van de zin

sentence2 = 'We went out for dinner with with Anne, Samuel and Bob.'
print('Shane' in sentence2)  # False. Shane staat niet in de zin

sentence3 = 'We were lucky that they had a table for 5.'
# kan niet want 5 is een int en kan geen onderdeel van een str zijn
# print(5 in sentence3)

print(str(5) in sentence3)  # True. str(5) bevind zich in sentence3

# COMPARE
print('Ik' == 'Ik')  # True
print('Jij' == 'Ik')  # False

# INDEX TO STRING  index begint bij 0

scale_of_c = ('CDEFGAB')
print(scale_of_c[0])  # C
print(scale_of_c[5])  # A

# index vanaf de eerste character terug naar het einde. dus -1 is B
print(scale_of_c[-1])  # B
print(scale_of_c[-3])  # G

# SLICING
counting = ('ONETWOTHREE')
print(counting[0:3])  # ONE want index 0 tot 3
# of
print(counting[:3])  # ONE want index begin tot 3
print(counting[3:6])  # TWO want index 3 tot 6
print(counting[6:11])  # THREE want index 6 tot 11
# of
print(counting[6:])  # THREE want index 6 tot einde

# LENGTH OF A STRING
# The length of ONETWOTHREE is 11
print('The length of', counting, 'is', len(counting))

# INSERT VARIABLE IN STRING (string interpolation)

answer = 42
qa = f'The answer is.. {answer}'
print(qa)  # The answer is.. 42
print(type(qa))  # string
