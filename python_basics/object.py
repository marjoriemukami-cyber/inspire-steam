# Name : Marjorie Mukami
# Date : 19/02/2026

class Human:
    #First we define the attributes of a human being
    type = "Mammals"
    legs = 2
    brain = True
    warm_blooded = True

    # We then create a constructor for the class/object
    # The constructor will be used to create copies of this project
    def __init__(self, name, age):
        self.human_name = name
        self.human_age = age

    def tell_story(self):
        print(f"Hello, I am {self.human_name} Here is a story")
        print(f"In the breezy wind of the morning at Mt Kilimanjaro")

#Create the humans
amani = Human("Amani", 17)
triza = Human("Triza", 18)

#Let the human created do things
amani.tell_story()
print("Amani's age is:", amani.human_age)

# Modify one of the objects, without modifying other objects
print("Triza's location: ",triza.city)
print("Amani's location: ",amani.city)

triza.city = "Lamu"

print("Triza's location: ",triza.city)
print("Amani's location: ",amani.city)
