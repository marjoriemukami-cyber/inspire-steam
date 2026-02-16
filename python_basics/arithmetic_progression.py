# Name : Marjorie Mukami
# Date : 13/02/2026


# Program to calculate arithmetic progression


# calculating nth term

a = int(input("enter the first number :"))
n = int(input("enter the number of terms :"))
d = int(input("enter the common difference"))

nth_term = a + (n - 1) * d
print(f"the nth_term is: {nth_term}") 

sn = (n / 2) * (2 * a +(n - 1) * d)
print(f"the sum of terms is: {sn}")