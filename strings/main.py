# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

scorer_name = 'Ruud Gullit'
scorer_name_2 = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = scorer_name + ' ' + str(goal_0) + ',' + ' ' + \
    scorer_name_2 + ' ' + str(goal_1)
print(scorers)

report = f'{scorer_name} scored in the {goal_0}nd minute\n{scorer_name_2} scored in the {goal_1}th minute'
print(report)

player = 'Wim Kieft'
print(player.find(' '))
space = player.find(' ')

first_name = player[0:space]
print(first_name)

first_letter_lastname = player.find(' ') + 1
last_name = player[first_letter_lastname:]
last_name_len = len(last_name)
print(last_name_len)

name_short = f'{player[0]}. {last_name}'
print(name_short)

chant = f'{first_name}! ' * 3
good_chant = " " != chant[-1]
print(good_chant)

chant = f'{first_name}! ' * (len(first_name) - 1) + f'{first_name}!'

print(chant)
