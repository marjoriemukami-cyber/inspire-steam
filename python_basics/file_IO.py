# Name : Marjorie Mukami
# Date : 23/02/2026
# Program to perfom file operations

# create new file
new_file = open("student_data.txt","r+")

# write to new file
new_file.write("{Student name : Marjorie, ID : 111111 , email : manjo@gmail.com}")


# read to new file
data = new_file.read()

print(data)
new_file.close()

# remove a new file
# use os module 
 



