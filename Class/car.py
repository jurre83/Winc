class Car:
    def __init__(self, color: str, mileage: int):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f'The {self.color} car has {self.mileage:,} miles.'


# _ waar de , moet komen
car_1 = Car('blue', 20_000)
car_2 = Car('red', 30_000)

print(car_1)
print(car_2)


class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __str__(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old.'


person_1 = Person('Jurre', 'Zwaan', 39)
print(person_1)
