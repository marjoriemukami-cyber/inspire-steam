# Name : Marjorie Mukami
# Date : 18/02/2026
# Program to show dictionarys in python

car = {"Model": "Audi",
        "Make" : "Q8" ,
        "Color":"Cherry", 
        "Year" : "2025"}

print(car)      
print(car["Model"])

#using dict as the prompt
author = dict(name="Hazelwood", type="STEM romance")
print(author)

students = {"Naomi": 17,
                "Janet": 21,
                "Caren": 20,
                "Rita": 19}

for key in students:
    print(key)
for val in students.values():
    print(val)   