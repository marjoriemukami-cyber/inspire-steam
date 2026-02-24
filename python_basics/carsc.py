class Car():
    def __init__(self, model, make, colour, year):
        self.model = model
        self.make = make
        self.colour = colour
        self.year = year

    # This must be indented to be part of the class
    def print_details(self):
        print(f"{self.make} {self.model} of colour {self.colour} was manufactured in the year {self.year}")

my_car = Car("Atenza", "Mazda", "Magenta", "2018")
# No need to pass arguments here; the object already knows them!
my_car.print_details() 
