# Write a Python program to count the number of even and odd numbers from a series of number
numbers = (1,2,3,4,5,6,7,8,9,10,56,23,89,246)
even = 0
odd = 0
for n in numbers:
    if n%2 == 0:
        even += 1
    else:
        odd +=1
print("Number of even numbers: ", even) 
print("Number of odd numbers: ", odd)           
