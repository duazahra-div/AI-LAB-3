# Write a Python Program to check the validity of password input by users
password = input("Enter password: ")

lower = False
upper = False
digit = False
special = False

for ch in password:
    if ch.islower():
        lower=True
    elif ch.isupper():
        upper=True
    elif ch.isdigit():
        digit=True
    elif ch in "$#@":
        special=True
if len(password)>=6 and len(password) <=16 and lower and upper and digit and special:
    print("valid Password")
else:
    print("Invalid Password")                    
            