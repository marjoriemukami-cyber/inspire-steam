# Name : Marjorie Mukami
# Date : 23/02/2026
# Program to show inheritance in python 

class Animal():
    def __init__(self,species,food,weight):
        self.species = species
        self.food = food
        self.weight = weight

    def grow(self,weight):
        weight = 1.1 * weight
        print(f"The animal weighs{weight} in kgs")

    def eat(self,food):
        print(f"The animal eats {food}")

class Dog(Animal):
    def __init__(self,colour,breed,height):
        super().__init__(self,species,food,weight)
        self.colour = colour
        self.height = height
        self.breed = breed
       

    def barks(self):
        print(f"The dog says woof woof")

    def eat(self,food):
        print(f"The animal eats {food}")   


class Horse(Animal):
    def __init__(self,species,food,weight):
        self.species = species
        self.food = food
        self.weight = weight

    def eat(self):
        print(f"The horse says neigh neigh")           
