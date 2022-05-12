# Do not modify these lines
__winc_id__ = "04da020dedb24d42adf41382a231b1ed"
__human_name__ = "classes"

# Add your code after this line


class Player:
    def __init__(self, name: str, speed: float, endurance:
                 float, accuracy: float):
        if speed < 0 or speed > 1:
            raise ValueError('speed must be between 0 and 1')
        if endurance < 0 or endurance > 1:
            raise ValueError('endurance must be between 0 and 1')
        if accuracy < 0 or accuracy > 1:
            raise ValueError('accuracy must be between 0 and 1')

        self.name = name
        self.speed = speed
        self.endurance = endurance
        self.accuracy = accuracy

    def introduce(self):
        return f'Hello everyone, my name is {self.name}.'

    def strength(self):
        dict = {'speed': self.speed, 'endurance': self.endurance,
                'accuracy': self.accuracy}
        max_key = max(dict, key=dict.get)
        max_value = max(dict.values())
        return (max_key, max_value)


class Commentator:
    def __init__(self, name: str):
        self.name = name

    def sum_player(self, player):
        speed = getattr(player, 'speed')
        endurance = getattr(player, 'endurance')
        accuracy = getattr(player, 'accuracy')
        return speed + endurance + accuracy

    def compare_players(self, player_1, player_2, attrib):
        attrib_player_1 = getattr(player_1, attrib)
        attrib_player_2 = getattr(player_2, attrib)
        player_1_name = getattr(player_1, 'name')
        player_2_name = getattr(player_2, 'name')

        if attrib_player_1 > attrib_player_2:
            return player_1_name
        if attrib_player_2 > attrib_player_1:
            return player_2_name
        if attrib_player_1 == attrib_player_2:
            strength_1 = player_1.strength()
            strength_2 = player_2.strength()
            if strength_1 > strength_2:
                return player_1_name
            if strength_2 > strength_1:
                return player_2_name
            if strength_1 == strength_2:
                ray = Commentator('Ray Hudson')
                sum_player_1 = ray.sum_player(player_1)
                sum_player_2 = ray.sum_player(player_2)
                if sum_player_1 > sum_player_2:
                    return player_1_name
                if sum_player_2 > sum_player_1:
                    return player_2_name
                if sum_player_1 == sum_player_2:
                    return 'These two players might as well be twins!'


def main():

    jurre = Player('Jurre', 1, 1, 1)
    print(jurre.speed)
    print(jurre.introduce())
    print(jurre.strength())
    ray = Commentator('Ray Hudson')
    print(ray.name)
    print(ray.sum_player(jurre))
    hilbert = Player('Hilbert', 1, 1, 1)
    print(ray.compare_players(jurre, hilbert, 'speed'))


if __name__ == "__main__":
    main()
