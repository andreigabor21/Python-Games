from CityController import *


class UI:
    def __init__(self, controller : CityController):
        self.controller = controller

    def buy_sell(self):
        value = int(input("Acres to buy/sell(+/-) ->"))
        self.controller.modify_land(value)

    def feed_population_ui(self):
        value = int(input("Units to feed the population ->"))
        self.controller.feed_population(value)

    def acres_plant(self):
        value = int(input("Acres to plant ->"))
        self.controller.plant_acres(value)

    def start(self):
        try:
            while self.controller.city.year <= 5:
                self.controller.rats_eat()
                self.controller.city.announce()
                self.buy_sell()
                self.feed_population_ui()
                self.acres_plant()
                self.controller.city.year += 1
                self.controller.random_land_price()
        except GameWon as gw:
            print("Game Won!")
        except GameOver as go:
            print("Game Lost!")


if __name__ == '__main__':
    city = City()
    city_controller = CityController(city)
    ui = UI(city_controller)
    ui.start()