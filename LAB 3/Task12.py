# Write a program which accepts a sequence of comma seperated 4 digit binary numbers as its input and print the numbers that are divisible by 5 in a comma seperated sequence 
numbers = input("Enter binary numbers: ").split(",")
for n in numbers:
    decimal = int(n,2)

    if decimal % 5 == 0:
        print(n,end=" ")