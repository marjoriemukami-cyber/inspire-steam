#  Marjorie
#  12/02/2026
# String formatting
#Get string length

sentence = "I love Charlie Puth"

string_length = len(sentence)

print(f"The length is: {string_length}"))

# Splitting a string 
sentence_2 = "Cakes Biscuits"
split = sentence_2.split(" ")

print(f"the first subject is:", split[0])

# Make everything CAPS

mpesa_code = "ub21ddscfh"


capitalized = mpesa_code.upper()

print("New mpesa code:", capitalized)

# Make everything caps

mpesa_code = "ub21ddscfh"

uncapitalized = mpesa_code.lower()

print("New mpesa code:", uncapitalized)

# Replacing characters in a string

balance = "350Kes"
amount_added = "100Kes"

cleaned_balance = balance.replace("Kes", "")

print("Cleaned balance: ", cleaned_balance)

cleaned_amount_added = amount_added.replace("Kes", ""

print("Cleaned amount added: ", cleaned_amount_added)

# Daudi's answer

new_balance = int(cleaned_balance) + int(cleaned_amount_added)

print("The new balance is:", new_balance)

#sentence_3 = CONFIRMED you have received 475 Kes from Philip
balance = "315 Kes"
amount_added = "475 Kes"

cleaned_balance = balance.replace("Kes", "")

print(f"Cleaned balance:{cleaned_balance}")

cleaned_amount_added = amount_added.replace("Kes", "")

print("Cleaned amount added: ", cleaned_amount_added)

new balance = int(cleaned_balance) + int(cleaned_amount_added)

print(f"The new balance is :{new_balance}")

_
