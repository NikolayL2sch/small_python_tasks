from math import radians, sin, cos, acos


class Point:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def get_distance(self, other):
        cos_d = sin(self.latitude) * sin(other.latitude) + cos(self.latitude) \
                * cos(other.latitude) * cos(self.longitude - other.longitude)

        return 6371 * acos(cos_d)


class City(Point):
    def __init__(self, latitude, longitude, name, population):
        super().__init__(latitude, longitude)
        self.name = name
        self.population = population

    def get_name(self):
        return self.name


class Mountain(Point):
    def __init__(self, latitude, longitude, name, height):
        super().__init__(latitude, longitude)
        self.name = name
        self.height = height

    def get_name(self):
        return self.name


mountain = Mountain(49, 36, 'Эверест', 5392)
city = City(38, 22, 'Мурманск', 700000)

print(f'Расстояние от {mountain.get_name()} до {city.get_name()}:', end=' ')
print(city.get_distance(mountain))
