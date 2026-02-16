#  Marjorie
#  16/02/2026


number = int(input("Enter the number x:")) 
factorial = 1 # initiate factorial on 1
for x in range(0,number):
    factorial=(number)*(number-1)
print(f"{number}!={factorial}")


for x in range(1,number+1):
    factorial *=x
print(f"{number}!={factorial}")



    
