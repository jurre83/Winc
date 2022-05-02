# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line


def main():

    alphabetical_order(['Jaws', 'Superman', 'Star Wars', 'Midway'])

    print(won_golden_globe('JAWS'))

    print(remove_toto_albums(['test', 'Fahrenheit', 'Old Is New']))


def alphabetical_order(list):
    list.sort()
    return list


golden_globes_won = ['Jaws', 'Star Wars: Episode IV - A New Hope',
                     'E.T. the Extra-Terrestrial', 'Memoirs of a Geisha']


def won_golden_globe(film_name):
    list_lower_case = (map(lambda x: x.lower(), golden_globes_won))
    if film_name.lower() in list_lower_case:
        return True
    else:
        return False


toto_albums = ['Fahrenheit', 'The Seventh One', 'Toto XX',
               'Falling in Between', 'Toto XIV', 'Old Is New']


def remove_toto_albums(album_list):
    print(album_list)
    if 'Fahrenheit' in album_list:
        album_list.remove('Fahrenheit')
        remove_toto_albums(album_list)

    if 'The Seventh One' in album_list:
        album_list.remove('The Seventh One')
        remove_toto_albums(album_list)

    if 'Toto XX' in album_list:
        album_list.remove('Toto XX')
        remove_toto_albums(album_list)

    if 'Falling in Between' in album_list:
        album_list.remove('Falling in Between')
        remove_toto_albums(album_list)

    if 'Toto XIV' in album_list:
        album_list.remove('Toto XIV')
        remove_toto_albums(album_list)

    if 'Old Is New' in album_list:
        album_list.remove('Old Is New')
        remove_toto_albums(album_list)

    return album_list


if __name__ == '__main__':
    main()
