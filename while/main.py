from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    print(random_koala_fact())


def unique_koala_facts(number):
    i = 0
    unique_koala_facts_list = []
    while i < 1000:
        fact = random_koala_fact()
        i += 1
        if fact not in unique_koala_facts_list:
            if len(unique_koala_facts_list) != number:
                unique_koala_facts_list.append(fact)
            else:
                break
    return unique_koala_facts_list


def num_joey_facts():
    joey_facts = []
    joey_counter = 0
    random_fact = random_koala_fact()
    random_fact_counter = 0
    while random_fact_counter < 10:
        fact = random_koala_fact()
        if random_fact == fact:
            random_fact_counter += 1
        if "joey" in fact:
            if fact not in joey_facts:
                joey_facts.append(fact)
                joey_counter += 1
    return joey_counter


def koala_weight():
    i = 0
    while i < 1000:
        i += 1
        fact = random_koala_fact()
        if "kg" in fact:
            end_index = fact.find("kg")
            start_index = fact.rfind(" ", 0, end_index)
            koala_kg = fact[start_index:end_index]
    return int(koala_kg)
