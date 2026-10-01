#write a Python Program that accepts a string and calculate the number of digits and letters.
text = input("Enter a string: ")
letters = 0
digits = 0

for ch in text:
   if ch.isalpha():
      letters += 1
   elif ch.isdigit():
       digits +=1
print("Letters ",letters)
print("Digits ",digits)
        

