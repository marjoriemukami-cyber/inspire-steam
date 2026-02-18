# Name : Marjorie Mukami
# Date : 18/02/2026
# Program to show lists in python
# List of friends


friends = ["Rachel","Phoebe","Ross","Chandlier"]

print(friends)
friends.sort()
print(friends)

friends.reverse()
print(friends)

friends.append("Steph") 
print(friends)

new_friends = ["Kami","Jess","Imma","Gidi"]
print(len(new_friends))

#new list of students
students = friends + new_friends
print(students)

students.pop()
print(friends)

students.insert(5,"Frank")
print(students)

students.insert(9,"Valarie")
print(students)

students.extend("Don")
print(students)

students.remove("Ross")
print(students)

new_students = students.copy()
print(new_students)