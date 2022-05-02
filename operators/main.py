# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line

language_spoken_most_spain = 'Castilian Spanish'
language_spoken_most_switzerland = 'German'
print(language_spoken_most_spain == language_spoken_most_switzerland)

most_prevelent_religion_spain = 'Roman Catholic'
most_prevelent_religion_switzerland = 'Roman Catholic'
print(most_prevelent_religion_spain == most_prevelent_religion_switzerland)

len_capital_spain = len('madrid')
len_capital_switzerland = len('bern')
print(len_capital_spain != len_capital_switzerland)

gpd_spain = 1714.68
gpd_switzerland = 590.71
print(gpd_switzerland > gpd_spain)

population_grow_rate_spain = 0.13
population_grow_rate_switzerland = 0.65
print(population_grow_rate_spain and population_grow_rate_switzerland < 1)

population_spain = 47163418
population_switzerland = 8508698
at_least_one_greater = population_spain or population_switzerland > 10000000
print(bool(at_least_one_greater))

exact_one_greater = population_spain > 10000000 and population_switzerland > 10000000
print(bool(exact_one_greater) == False)
