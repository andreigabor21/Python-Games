
class City:
    year = 1

    def __init__(self):
        self.population = 100
        self.acres = 1000
        self.units_grain = 3
        self.stock = 2800
        self.people_starved = 0
        self.new_people = 0
        self.rats_units = 0
        self.land_price = 0

    def announce(self):
        print("In year "+ str(self.year) +"," +str(self.people_starved) +" people starved")
        print(str(self.new_people) + " people came to the city")
        print("City owns " + str(self.acres) + " acres of land")
        print("City population is " + str(self.population))
        print("Harvest was "+ str(self.units_grain) + " units per acre")
        print("Rats ate " + str(self.rats_units) + " units ")
        print("Land price is " + str(self.land_price) + " units per acre")
        print("Grain stocks are " + str(self.stock)+ "units \n")
'''
city = City()
city.announce()
'''