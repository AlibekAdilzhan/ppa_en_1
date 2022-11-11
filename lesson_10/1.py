class Car:
    def __init__(self, mark, color, year, engine_volume, dtp):
        self.car_mark = mark
        self.color = color
        self.year = year
        self.eng_volume = engine_volume
        self.dtp = dtp

    def get_attrs(self):
        print(self.car_mark)
        print(self.color)
        print(self.year)
        print(self.eng_volume)
        print(self.dtp)


car_1 = Car("bmw", "black", 2010, 3.0, False)
car_2 = Car("mersedes", "white", 1999, 2.6, True)
car_3 = Car("zhiguli", "pink", 1991, 1.6, False)

car_3.get_attrs()