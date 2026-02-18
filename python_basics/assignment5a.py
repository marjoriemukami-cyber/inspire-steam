# Name : Marjorie Mukami
# Date : 16/02/2026
# Program to calculate income tax assignment

user_input = input("Enter your gross salary: ")
salary = int(user_input)

tax = 0.0
net_salary = float(salary)


if 50000 <= salary <= 100000:
    tax = (4.5 * salary) / 100
    net_salary = salary - tax


print(f"Gross salary = {salary}")
print(f"Net salary = {net_salary}")
print(f"Tax = {tax}")
