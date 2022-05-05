# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line


def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    dict = {}
    dict['name'] = name
    dict['date_of_birth'] = date_of_birth
    dict['place_of_birth'] = place_of_birth
    dict['height'] = height
    dict['nationality'] = nationality
    return dict


def add_stamp(passport, country):
    stamps_list = []
    if 'stamps' not in passport.keys():
        stamps_list.append(country)
        passport['stamps'] = stamps_list
    elif 'stamps' in passport:
        existing_stamp = passport['stamps']
        stamps_list.append(existing_stamp)
        if country not in passport.values():
            if country != passport['nationality']:
                stamps_list.append(country)
                passport['stamps'] = stamps_list
    return passport


def add_biometric_data(passport, key, value, date):

    if 'biometric' not in passport.keys():
        passport['biometric'] = {key: {'date': date, 'value': value}}
    elif 'biometric' in passport.keys():
        new_biometric = {key: {'date': date, 'value': value}}
        passport['biometric'].update(new_biometric)
    return passport


jurre = create_passport('Jurre', '01-04-1983',
                        'Gorinchem', '1.84', 'Netherlands')


jurre = add_biometric_data(jurre, 'eye_color_left', 'brown', '2022-05-04')
print(jurre)
jurre = add_biometric_data(jurre, 'eye_color_right', 'brown', '2022-05-04')
print(jurre)
fingerprint_data = {
    "left_pinky": "2378945",
    "left_ring": "2349081",
    "left_middle": "132890",
    "left_index": "9823234",
    "left_thumb": "0924131",
    "right_thumb": "6234923",
    "right_index": "13249734",
    "right_middle": "34023784",
    "right_ring": "12332538",
    "right_pinky": "32458970", }
jurre = add_biometric_data(jurre, 'finger_prints',
                           fingerprint_data, "2022-01-12")
print(jurre)
