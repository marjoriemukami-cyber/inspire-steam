# Name : Marjorie Mukami
# Date : 23/02/2026
# Program to show classes in python

class Car():
    #attributes of the car
    def __init__(self,model,make,colour,year):
        self.model = model
        self.make = make
        self.colour = colour
        self.year = year

#print car details
def print_details(self, model, make, color, year):
    print(f"{self.make} {self.model} of colour {self.colour} was manufactured in the year {self.year}")



#instantiate a class project   

my_car = Car("Atenza", "Mazda", "Magenta", "2018")
dads_car = Car("Ford", "Raptor", "Gold", "2015")
my_car.print_details("Atenza", "Mazda", "Magenta", "2018")

