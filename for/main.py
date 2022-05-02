# from itertools import count
from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """


def shortest_names(countries):
    list_of_length_countries = []
    for country in countries:
        length_of_country = len(country)
        list_of_length_countries.append(length_of_country)

    min_value = min(list_of_length_countries)
    shortest_named_countries = []

    for i in range(len(list_of_length_countries)):
        if list_of_length_countries[i] == min_value:
            shortest_named_countries.append(countries[i])
    return shortest_named_countries


def most_vowels(countries):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_per_country = []
    for country in countries:
        lowercase_country = country.lower()
        count = 0
        for char in lowercase_country:
            if char in vowels:
                count = count + 1
        vowels_per_country.append(count)

    countries_sorted = [i for _, i in sorted(
        zip(vowels_per_country, countries))]
    countries_sorted.reverse()
    return countries_sorted[0:3]


def alphabet_set(countries):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                'y', 'z']
    countries_abc = []
    countries_sorted = sorted(countries, key=len, reverse=True)
    for country in countries_sorted:
        lowercase_country = country.lower()
        for char in lowercase_country:
            if char in alphabet:
                alphabet.remove(char)
                if country not in countries_abc:
                    countries_abc.append(country)
    return countries_abc


# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()


""" Write the calls to your functions here. """


def main():
    shortest_names(countries)
    most_vowels(countries)
    alphabet_set(countries)
