from City import City
import random


class GameWon(Exception):
    pass


class GameOver(Exception):
    pass


class CityController:
    def __init__(self, city : City):
        self.city = city

    def random_land_price(self):
        self.city.land_price = random.randint(15, 26)

    def modify_land(self, value):
        self.city.acres += value
        if value >= 0:
            self.city.stock -= value * self.city.land_price
        else:
            self.city.stock += value * self.city.land_price

    def feed_population(self, value):
        self.city.stock -= value
        t = self.city.population
        t -= value // 20
        if t > self.city.population // 2:
            raise GameOver
        self.city.people_starved = t
        self.city.population -= t
        if t == 0:
            self.city.population += random.randint(0,11)

    def plant_acres(self, value):
        pass

    def modify_land_prices(self):
        price = random.randint(15, 26)
        self.city.land_price = price

    def rats_eat(self):
        p = random.randint(1,101)
        if p in range(1,21):
            l = random.randint(1,11) # l/100
            l = l/100
            self.city.rats_units = int(self.city.stock*l)
            self.city.stock -= self.city.rats_units
        else:
            self.city.rats_units = 0

    def game_won(self):
        if self.city.population > 100 and self.city.acres > 1000:
            raise GameWon
