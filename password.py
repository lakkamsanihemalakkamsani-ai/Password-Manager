import random
import string

print("===== PASSWORD MANAGER =====")
n = int(input("Enter  number of accounts:"))
length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + string.punctuation
for i in range(n):
    account_name = input("\n Enter account name: ")
    password = ""
    for j in range(length):
        password += random.choice(characters)
        print("Account : ", account_name)
        print("Password : ", password)
        
