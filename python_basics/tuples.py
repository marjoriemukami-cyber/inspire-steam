# Name : Marjorie Mukami
# Date : 18/02/2026
# Program to show tuples in python 
# tuples in fruits

fruits = ("Kiwi","Apple","Mangoes","Banana")

print(len(fruits))
print(fruits[0])
print(fruits[3])
print(fruits[-1])
print(fruits[-4])

# error -> append, tuples is immutable

fruits_list = list(fruits)
fruits_list.append("Guava")
print(fruits_list)
